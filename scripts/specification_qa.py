"""Check grammar specification structure and generate the public tracker."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import posixpath
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LEARNING = PurePosixPath("docs/learning")
CAT = LEARNING / "grammar-catalogue"
CONCEPTS = LEARNING / "concepts"
INDEX = CONCEPTS / "index.md"
TRACKER = LEARNING / "specification-progress.md"
MANIFEST = "scripts/specification-status.json"
CID = r"G[0-9]{2}-[0-9]{3}"
LINK = re.compile(r"\[([^\]\n]+)\]\(([^()\s]+)\)")
HEADINGS = ["Concept identity","Learning outcomes","Meaning and usage","Formation rules","Variations and agreement","Contextual examples","Related constructions and contrasts","Anticipated mistakes and corrective feedback","Natural usage","Prerequisites","Teaching depth","Activity types","Mastery evidence","Reference integration","Content validation"]
DEPTH = ("Introduction", "Guided application", "Independent application", "Flexible application")


def fingerprint(ids):
    return hashlib.sha256(("\n".join(sorted(ids)) + "\n").encode()).hexdigest()


def target(path, relative):
    return PurePosixPath(posixpath.normpath(posixpath.join(str(path.parent), unquote(relative))))


def anchors(text):
    explicit = set(re.findall(r'\{#([^}\s]+)\}|id=["\']([^"\']+)["\']', text))
    result = {a or b for a, b in explicit}
    seen = {}
    for title in re.findall(r"^#{1,6}\s+(.+)$", text, re.M):
        title = LINK.sub(r"\1", re.sub(r"\s+\{#[^}]+\}$", "", title))
        slug = re.sub(r"[^\w\s-]", "", title.lower()).strip().replace(" ", "-")
        count = seen.get(slug, 0)
        result.add(f"{slug}-{count}" if count else slug)
        seen[slug] = count + 1
    return result


def inventory(files, errors):
    active = {}
    for path, text in files.items():
        if path.parent != CAT or path.stem in {"index", "reconciliation"} or path.stem.startswith("traceability-"):
            continue
        category = None
        for n, line in enumerate(text.splitlines(), 1):
            heading = re.match(r"^## (G\d{2})\.\s+(.+?)\s+\{#(g\d{2})\}$", line)
            if heading:
                category = heading.groups()
            if not re.match(r"^\|\s*G\d[^\s|]*-", line):
                continue
            fields = [field.strip() for field in line.strip("|").split("|")]
            if len(fields) != 4 or not re.fullmatch(CID, fields[0]):
                errors.append(f"{path}:{n}: malformed catalogue ID or row")
                continue
            cid, title, outcome, _ = fields
            if not category or category[0] != cid[:3]:
                errors.append(f"{path}:{n}: {cid} is outside its category")
                continue
            if cid in active:
                errors.append(f"{path}:{n}: duplicate active concept {cid}")
            link = LINK.fullmatch(title)
            active[cid] = (link[1] if link else title, outcome,
                           f"{category[0]} — {category[1]}", path, category[2],
                           target(path, link[2]) if link else None)
    original = set()
    for path, text in files.items():
        if path.parent != CAT or not path.stem.startswith("traceability-"):
            continue
        split = re.split(r"^## (G[^\s]+) (.*)$", text, flags=re.M)
        for cid, anchor, body in zip(split[1::3], split[2::3], split[3::3]):
            if cid in original or not re.fullmatch(CID, cid) or anchor != "{#" + cid.lower() + "}":
                errors.append(f"{path}: duplicate or invalid original ID or anchor {cid}")
            original.add(cid)
            owner = re.search(r"^\*\*Surviving destination or evidence owner\*\* · (.+)$", body, re.M)
            links = LINK.findall(owner[1]) if owner else []
            if not links:
                errors.append(f"{path}: {cid} has no traceability destination")
            for dest, uri in links:
                rel, _, fragment = uri.partition("#")
                if dest not in active or active[dest][3:5] != (target(path, rel), fragment):
                    errors.append(f"{path}: {cid} has invalid destination {dest} ({uri})")
    return active, original


def content_fingerprints(files, active):
    outcomes = (f"{cid}\t{row[1]}" for cid, row in active.items())
    destinations = []
    for path, text in files.items():
        if path.parent != CAT or not path.stem.startswith("traceability-"):
            continue
        blocks = re.split(r"^## (G[^\s]+) (.*)$", text, flags=re.M)
        for cid, body in zip(blocks[1::3], blocks[3::3]):
            owner = re.search(r"^\*\*Surviving destination or evidence owner\*\* · (.+)$", body, re.M)
            destinations.extend(f"{cid}\t{dest}\t{uri}" for dest, uri in LINK.findall(owner[1] if owner else ""))
    return {"outcomes_sha256": fingerprint(outcomes), "destinations_sha256": fingerprint(destinations)}


def check_content(files, active, manifest, errors):
    labels = {"outcomes_sha256": "learning outcomes", "destinations_sha256": "traceability destinations"}
    for key, digest in content_fingerprints(files, active).items():
        if digest != manifest[key]:
            errors.append(f"Catalogue: {labels[key]} differ from approved baseline {manifest['baseline']}")


def check_inventory(active, original, manifest, errors):
    if not set(active) <= original or len({cid[:3] for cid in active}) != 31:
        errors.append("Catalogue: expected 31 categories with each active ID traceable")
    for label, ids in (("active", active), ("original", original)):
        if len(ids) != manifest[f"expected_{label}"]:
            errors.append(f"Catalogue: unexpected {label} ID count ({len(ids)})")
        if fingerprint(ids) != manifest[f"{label}_sha256"]:
            errors.append(f"Catalogue: {label} ID set differs from baseline {manifest['baseline']}")


def specification(path, text, active, errors, legacy=False):
    parts = re.split(r"^## (\d+)\. ([^\n]+)$", text, flags=re.M)
    found = [(int(n), re.sub(r"\s+\{#[^}]+\}$", "", h)) for n, h in zip(parts[1::3], parts[2::3])]
    if found != list(enumerate(HEADINGS, 1)):
        errors.append(f"{path}: expected all 15 numbered sections in order")
    sections = {int(n): body.strip() for n, body in zip(parts[1::3], parts[3::3])}
    for n in range(1, 16):
        if not sections.get(n):
            errors.append(f"{path}: section {n} has no content")
    identity = sections.get(1, "")
    match = re.search(rf"Catalogue ID:\s*\*\*({CID})\*\*", identity)
    if not match:
        errors.append(f"{path}: missing catalogue ID")
        return None, identity
    cid = match[1]
    if cid not in active:
        errors.append(f"{path}: unknown or inactive specification concept {cid}")
    elif f"Catalogue learning outcome: {active[cid][1]}" not in identity:
        errors.append(f"{path}: learning outcome differs from the catalogue")
    elif not legacy and f"English title: {active[cid][0]}." not in identity:
        errors.append(f"{path}: English title differs from the catalogue")
    for field in ("English title:", "Concept type:", "Specification status:", "Validation status:", "CEFR assignment:"):
        if field not in identity:
            errors.append(f"{path}: missing identity field {field}")
    outcomes = re.findall(r"^- (LO[1-9]\d*):\s+\S", sections.get(2, ""), re.M)
    if not outcomes or len(outcomes) != len(set(outcomes)):
        errors.append(f"{path}: local outcomes must exist and be unique")
    depth = sections.get(11, "")
    for name in DEPTH:
        if not re.search(rf"^\|\s*{name}\s*\|", depth, re.M):
            errors.append(f"{path}: missing depth row {name}")
    refs = set(re.findall(r"\bLO[1-9]\d*\b", depth))
    for lo in sorted(set(outcomes) - refs):
        errors.append(f"{path}: teaching-depth mapping omits {lo}")
    for lo in sorted(refs - set(outcomes)):
        errors.append(f"{path}: undefined outcome {lo} in teaching-depth mapping")
    if not legacy:
        table = sections.get(6, "").splitlines()
        columns = "| Devanagari | Romanisation | English | Context and analysis to review |"
        rows = [line for line in table[table.index(columns) + 2:] if line.startswith("|")] if columns in table else []
        if not rows:
            errors.append(f"{path}: expected populated contextual table with all three representations")
        for line in rows:
            cells = [cell.strip() for cell in line.strip("|").split("|")]
            if len(cells) != 4 or not all(cells):
                errors.append(f"{path}: empty or malformed contextual example row")
            if "Research gap" in line and "representation" not in sections.get(15, "").lower():
                errors.append(f"{path}: missing representation needs a section 15 research entry")
    return cid, identity


def check_evidence(cid, record, files, errors):
    for key, value in record.items():
        if not key.endswith("_evidence"):
            continue
        if not isinstance(value, str):
            errors.append(f"{cid}: {key} must be a repository Markdown path with an explicit evidence anchor")
            continue
        uri = urlsplit(value)
        path = PurePosixPath(uri.path)
        if (uri.scheme or uri.netloc or uri.query or path.is_absolute() or ".." in path.parts
                or path not in files or not uri.fragment or unquote(uri.fragment) not in anchors(files[path])):
            errors.append(f"{cid}: {key} does not resolve to a repository Markdown evidence anchor: {value}")


def status(cid, identity, record, errors):
    defaults = {"linguistic": "Pending", "native": "Pending", "cefr": "Unassigned", "publication": "Unestablished"}
    approved = {"linguistic": "Approved", "native": "Approved", "cefr": "Mapped", "publication": "Eligible"}
    result = {}
    for key, default in defaults.items():
        value = record.get(key, default)
        if value not in {default, approved[key]}:
            errors.append(f"{cid}: invalid {key} status {value}")
        elif value != default and not record.get(f"{key}_evidence"):
            errors.append(f"{cid}: {key} status requires an evidence reference")
        result[key] = value
    if result["publication"] == "Eligible" and (result["linguistic"], result["native"]) != ("Approved", "Approved"):
        errors.append(f"{cid}: publication requires linguistic and native-speaker approval")
    if "Specification status: Draft" in identity and (
        "Approved" in (result["linguistic"], result["native"]) or result["publication"] == "Eligible"
    ):
        errors.append(f"{cid}: draft conflicts with approved validation or publication status")
    if result["cefr"] == "Unassigned" and "CEFR assignment: Unassigned" not in identity:
        errors.append(f"{cid}: CEFR assignment must be unassigned")
    if result["linguistic"] == result["native"] == "Pending":
        line = re.search(r"^-\s*Validation status:.*$", identity, re.M | re.I)
        if not line or not re.search(r"\bpending\b", line[0], re.I) or re.search(
            r"native-speaker approved|linguistically approved|eligible for publication", line[0], re.I
        ):
            errors.append(f"{cid}: pending status conflicts with validation identity")
    return result


def add_spec(specs, cid, path, identity, errors):
    if cid in specs:
        errors.append(f"{path}: duplicate canonical specification for {cid}")
    specs[cid] = path, identity


def check_links(root, files, errors):
    slugs = {path: anchors(text) for path, text in files.items()}
    for path, text in files.items():
        fence = chr(96) * 3
        body = re.sub(rf"^{fence}[^\n]*\n.*?^{fence}[ \t]*$", "", text, flags=re.M | re.S)
        for label, value in LINK.findall(body):
            uri = urlsplit(value)
            if uri.scheme or uri.netloc or uri.path.startswith("/"):
                continue
            dest = target(path, uri.path) if uri.path else path
            if dest not in files and not (root / dest).exists():
                errors.append(f"{path}: broken link [{label}]({value})")
            elif dest in slugs and uri.fragment and unquote(uri.fragment) not in slugs[dest]:
                errors.append(f"{path}: unresolved anchor [{label}]({value})")


def tracker(active, specs, batches, assigned, states):
    total, count = len(active), len(specs)
    lines = [
        "---", "title: Specification progress", "parent: Learning", "nav_exclude: true", "---", "",
        "# Specification progress", "",
        "Generated by [specification QA](specification-authoring.md#qa). "
        "See the [batch register](specification-batches.md) and [decision register](curriculum-decisions.md).", "",
        f"**{count} of {total} authored ({count / total:.1%}).** {total - count} remain unauthored.", "",
        "| Batch | Scope | Authoring | Structural review | PR |", "| --- | --- | --- | --- | --- |",
    ]
    for batch in batches:
        done = sum(cid in specs for cid in batch["ids"])
        lines.append(f"| [{batch['id']}](specification-batches.md#{batch['anchor']}) | "
                     f"{batch['title']} | {done}/{len(batch['ids'])} authored | {batch['structural']} | "
                     f"[Review]({batch['pr']}) |")
    previous = None
    for cid, (title, _, category, _, _, _) in sorted(active.items()):
        if category != previous:
            lines.extend(["", f"## {category}", "",
                          "| ID | Concept | Specification and research | Batch | Authoring | Structural | Linguistic | Native-speaker | CEFR | Publication |",
                          "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"])
        previous = category
        batch = assigned.get(cid)
        group = f"[{batch['id']}](specification-batches.md#{batch['anchor']})" if batch else "Unassigned"
        authored = cid in specs
        spec = "—"
        if authored:
            path = specs[cid][0].relative_to(LEARNING)
            spec = f"[Spec]({path}) · [Research]({path}#15-content-validation)"
        review = batch["structural"] if authored and batch else "Not started"
        validation = states.get(cid, dict.fromkeys(("linguistic", "native", "cefr", "publication"), "Not started"))
        columns = [cid, title, spec, group, "Authored" if authored else "Unauthored", review, *validation.values()]
        lines.append("| " + " | ".join(columns) + " |")
    return "\n".join(lines) + "\n"


def build(root):
    paths = [root / "README.md", *sorted((root / "docs").rglob("*.md"))]
    files = {PurePosixPath(path.relative_to(root)): path.read_text(encoding="utf-8")
             for path in paths if path.relative_to(root) != TRACKER}
    manifest = json.loads((root / MANIFEST).read_text(encoding="utf-8"))
    errors = []
    active, original = inventory(files, errors)
    check_inventory(active, original, manifest, errors)
    check_content(files, active, manifest, errors)
    assigned = {}
    batches = manifest["batches"]
    batch_ids = set()
    for batch in batches:
        if batch["id"] in batch_ids:
            errors.append(f"{batch['id']}: duplicate batch record")
        batch_ids.add(batch["id"])
        if batch["structural"] not in {"Approved", "Awaiting review", "Changes requested", "Not started"}:
            errors.append(f"{batch['id']}: invalid structural status")
        for cid in batch["ids"]:
            if cid not in active or cid in assigned:
                errors.append(f"{batch['id']}: duplicate or unknown batch concept {cid}")
            assigned[cid] = batch
    specs, states, orders = {}, {}, set()
    for path, source in files.items():
        if path.parent != CONCEPTS or path == INDEX:
            continue
        match = re.search(rf"Catalogue ID:\s*\*\*({CID})\*\*", source)
        legacy = bool(match and assigned.get(match[1], {}).get("id") == "Step 3A")
        cid, identity = specification(path, source, active, errors, legacy)
        if cid is None:
            continue
        add_spec(specs, cid, path, identity, errors)
        if cid not in assigned or cid not in active or active[cid][5] != path:
            errors.append(f"{path}: inconsistent batch assignment or catalogue link")
        record = manifest["validation"].get(cid, {})
        states[cid] = status(cid, identity, record, errors)
        check_evidence(cid, record, files, errors)
        front = source.split("---\n", 2)[1] if source.startswith("---\n") else ""
        order = re.search(r"^nav_order: (\d+)$", front, re.M)
        if not order or order[1] in orders or "parent: Grammar concept framework\n" not in front or "grand_parent: Learning\n" not in front:
            errors.append(f"{path}: invalid or duplicate specification navigation metadata")
        if order:
            orders.add(order[1])
    for cid in (set(assigned) | manifest["validation"].keys()) - specs.keys():
        errors.append(f"{cid}: batch or review record has no canonical specification")
    listed = [(cid, target(INDEX, uri)) for cid, uri in re.findall(
        rf"^\|\s*({CID})\s*\|\s*\[[^\]]+\]\(([^)]+)\)", files[INDEX], re.M
    )]
    if sorted(listed) != sorted((cid, path) for cid, (path, _) in specs.items()):
        errors.append(f"{INDEX}: concept IDs or paths differ from canonical specifications")
    result = tracker(active, specs, batches, assigned, states) if not errors else ""
    files[TRACKER] = result
    check_links(root, files, errors)
    return result, errors, (len(active), len(original), len(specs))


def check_tracker(path, generated, errors):
    if not path.exists() or path.read_text(encoding="utf-8") != generated:
        errors.append(f"{TRACKER}: stale tracker; run python3 scripts/specification_qa.py --write")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="regenerate the tracker")
    args = parser.parse_args()
    try:
        generated, errors, totals = build(ROOT)
        path = ROOT / TRACKER
        if not args.write:
            check_tracker(path, generated, errors)
        if errors:
            for error in errors:
                print(f"ERROR: {error}", file=sys.stderr)
            return 1
        if args.write:
            path.write_text(generated, encoding="utf-8")
        active, original, authored = totals
        print(f"Specification QA passed: {active} active, {original} original, "
              f"{authored} authored, {active - authored} unauthored.")
        return 0
    except (OSError, ValueError, KeyError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
