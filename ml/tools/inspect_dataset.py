from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="ml/data", help="Dataset root")
    args = parser.parse_args()

    root = Path(args.root)
    summary = {
        "root_exists": root.exists(),
        "files": [],
    }

    if root.exists():
        for path in sorted(root.rglob("*")):
            if path.is_file():
                summary["files"].append(str(path.relative_to(root)))

    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
