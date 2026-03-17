from __future__ import annotations

import argparse
from pathlib import Path
import yaml


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="ml/configs/baseline.yaml")
    args = parser.parse_args()

    config_path = Path(args.config)
    config = yaml.safe_load(config_path.read_text(encoding="utf-8"))

    print("Training scaffold only.")
    print("Implement actual training after dataset inspection.")
    print("Loaded config:")
    print(config)


if __name__ == "__main__":
    main()
