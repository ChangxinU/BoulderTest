from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path

DATASET = "tomasslama/indoor-climbing-gym-hold-segmentation"


def run_download(output_dir: Path, force: bool = False) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    kaggle_bin = shutil.which("kaggle")
    if kaggle_bin is None:
        raise RuntimeError(
            "`kaggle` CLI was not found. Install it first and configure Kaggle API credentials "
            "(~/.kaggle/kaggle.json or KAGGLE_USERNAME/KAGGLE_KEY)."
        )

    cmd = [
        kaggle_bin,
        "datasets",
        "download",
        "-d",
        DATASET,
        "-p",
        str(output_dir),
        "--unzip",
    ]
    if force:
        cmd.append("--force")

    subprocess.run(cmd, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Download Kaggle hold-segmentation dataset into ml/data")
    parser.add_argument("--output-dir", default="ml/data", help="Target directory")
    parser.add_argument("--force", action="store_true", help="Force redownload if cached archive exists")
    args = parser.parse_args()

    run_download(output_dir=Path(args.output_dir), force=args.force)
    print(f"Dataset download complete: {args.output_dir}")


if __name__ == "__main__":
    main()
