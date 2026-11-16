#!/usr/bin/env python3
"""ai-excited-01 entry: write the shark image to /output/entry.png.

The image beside this file is copied byte for byte to the output directory
($MAKEFUN_OUTPUT_DIR, default /output). Standard library only, no network,
deterministic: both grader runs write the same bytes.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    shutil.copyfile(SOURCE, dest)
    # Self-check: the copy must be byte-identical to the source image.
    if sha256_of(SOURCE) != sha256_of(dest):
        print("error: output does not match source image", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
