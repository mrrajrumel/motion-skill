#!/usr/bin/env python3
"""Package the Motion Skill into a clean .zip bundle ready for upload to Claude.ai or Claude Desktop.
Usage: python scripts/package_skill.py [output_path]
"""
import os, sys, zipfile, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTPUT_ZIP = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else (ROOT / "motion-skill-claude.zip")

INCLUDE_DIRS = ["workflows", "engine", "scripts", "templates", "reference", "examples"]
INCLUDE_FILES = ["SKILL.md", "README.md", "LICENSE"]
EXCLUDE_EXTS = {".pyc", ".DS_Store", ".tmp", ".log"}
EXCLUDE_NAMES = {"__pycache__", "node_modules", ".git", ".object-separation", "work", "dist", "out"}

print(f"Packaging Motion Skill from: {ROOT}")
count = 0

with zipfile.ZipFile(OUTPUT_ZIP, "w", zipfile.ZIP_DEFLATED) as z:
    # Add root files
    for fn in INCLUDE_FILES:
        p = ROOT / fn
        if p.exists():
            z.write(p, arcname=fn)
            count += 1
            print(f"  + {fn}")

    # Add directories recursively
    for dname in INCLUDE_DIRS:
        dp = ROOT / dname
        if not dp.exists():
            continue
        for root, dirs, files in os.walk(dp):
            dirs[:] = [d for d in dirs if d not in EXCLUDE_NAMES]
            for f in files:
                if any(f.endswith(ext) for ext in EXCLUDE_EXTS):
                    continue
                fp = pathlib.Path(root) / f
                rel = fp.relative_to(ROOT)
                z.write(fp, arcname=str(rel).replace("\\", "/"))
                count += 1

print(f"\nDone! Packed {count} files into: {OUTPUT_ZIP.resolve()}")
print("You can now directly upload this .zip or its files into your Claude.ai Project Knowledge!")
