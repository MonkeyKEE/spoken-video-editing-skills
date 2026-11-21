import argparse, hashlib, json, re
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Check local skill dependencies without modifying or uploading files.")
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()
    manifest = json.loads(args.manifest.read_text(encoding="utf-8-sig"))
    items = manifest["assets"]
    if not isinstance(items, dict) or not items:
        parser.error("assets must be a nonempty object")
    failed = False
    for label, item in items.items():
        raw = item.get("path")
        digest = item.get("sha256")
        if not raw:
            required = item.get("required", True)
            print(f"{label}: {'missing' if required else 'optional, not configured'}")
            failed |= required
            continue
        path = args.manifest.parent / Path(raw).expanduser()
        if not path.is_file() or not path.stat().st_size:
            print(f"{label}: missing or empty")
            failed = True
            continue
        checksum = hashlib.sha256()
        with path.open("rb") as data:
            for block in iter(lambda: data.read(1024 * 1024), b""):
                checksum.update(block)
        actual = checksum.hexdigest()
        if digest and (not re.fullmatch(r"[0-9a-fA-F]{64}", digest) or digest.lower() != actual):
            print(f"{label}: SHA-256 mismatch")
            failed = True
        else:
            print(f"{label}: {'verified' if digest else 'present; not pinned'} ({actual})")
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())
