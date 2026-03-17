from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image

from ml.postprocess.format_output import build_prediction_response


def run_placeholder_prediction(image_path: str) -> dict:
    image = Image.open(image_path).convert("RGB")
    width, height = image.size

    # Placeholder empty response until model inference is implemented.
    return build_prediction_response(
        image_width=width,
        image_height=height,
        holds=[],
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", required=True, help="Path to input image")
    parser.add_argument("--output", required=False, help="Optional JSON output path")
    args = parser.parse_args()

    result = run_placeholder_prediction(args.image)

    if args.output:
        Path(args.output).write_text(json.dumps(result, indent=2), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
