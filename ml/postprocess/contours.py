from __future__ import annotations

from typing import List, Sequence, Tuple

import cv2
import numpy as np


Point = Tuple[float, float]


def mask_to_contours(
    mask: np.ndarray,
    min_area: float = 20.0,
    simplify_epsilon: float | None = 2.0,
) -> List[List[Point]]:
    """Convert a binary mask into contour point lists.

    Args:
        mask: 2D numpy array, non-zero treated as foreground.
        min_area: Drop small contours below this area.
        simplify_epsilon: If provided, apply polygon simplification.

    Returns:
        A list of contours, each contour is a list of (x, y) points in pixel space.
    """
    if mask.ndim != 2:
        raise ValueError("mask must be 2D")

    mask_u8 = (mask > 0).astype(np.uint8) * 255
    contours, _ = cv2.findContours(mask_u8, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    results: List[List[Point]] = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area < min_area:
            continue

        if simplify_epsilon is not None:
            contour = cv2.approxPolyDP(contour, epsilon=simplify_epsilon, closed=True)

        points: List[Point] = []
        for p in contour.reshape(-1, 2):
            x, y = float(p[0]), float(p[1])
            points.append((x, y))

        if points:
            results.append(points)

    return results


def normalize_points(points: Sequence[Point], width: int, height: int) -> List[Point]:
    if width <= 0 or height <= 0:
        raise ValueError("width and height must be positive")
    return [(float(x) / width, float(y) / height) for x, y in points]
