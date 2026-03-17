from __future__ import annotations

from typing import Any, Dict, List, Sequence, Tuple

from .contours import normalize_points

Point = Tuple[float, float]


def build_hold_prediction(
    hold_id: str,
    score: float,
    class_name: str,
    contour_points: Sequence[Point],
    image_width: int,
    image_height: int,
    bbox: Sequence[float] | None = None,
    mask_size: Sequence[int] | None = None,
    metadata: Dict[str, Any] | None = None,
) -> Dict[str, Any]:
    return {
        "hold_id": hold_id,
        "score": float(score),
        "class_name": class_name,
        "bbox": list(bbox) if bbox is not None else None,
        "mask_size": list(mask_size) if mask_size is not None else None,
        "contour_points": [[float(x), float(y)] for x, y in contour_points],
        "normalized_contour_points": [
            [float(x), float(y)]
            for x, y in normalize_points(contour_points, image_width, image_height)
        ],
        "metadata": metadata or {},
    }


def build_prediction_response(
    image_width: int,
    image_height: int,
    holds: List[Dict[str, Any]],
) -> Dict[str, Any]:
    return {
        "image_size": [int(image_width), int(image_height)],
        "holds": holds,
    }
