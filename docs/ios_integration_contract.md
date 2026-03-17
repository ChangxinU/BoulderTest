# iOS Integration Contract

## Goal
Define the shape of algorithm output that the future iOS app can consume.

## Recommended inference output
Each prediction item should contain:

- `hold_id`: stable or sequential identifier
- `score`: confidence score from 0 to 1
- `bbox`: optional [x_min, y_min, x_max, y_max] in image pixel space
- `image_size`: [width, height]
- `contour_points`: ordered list of pixel-space points
- `normalized_contour_points`: ordered list normalized to [0, 1]
- `mask_size`: optional [mask_width, mask_height]
- `class_name`: e.g. `hold`
- `metadata`: optional dictionary

## Coordinate conventions
### Pixel-space points
Use image coordinates before any iOS view transform:
- origin at top-left
- x grows to the right
- y grows downward

### Normalized points
Normalize by original image width and height:
- `x_norm = x / image_width`
- `y_norm = y / image_height`

This is preferred for later iOS overlay rendering because the app can remap to any displayed image size.

## Contour requirements
- contour should be closed logically
- point order should be consistent
- contour should represent the hold boundary
- optional simplification is allowed if documented

## Example output
See `ios_contract/hold_output_schema.json` and `ios_contract/example_prediction.json`.

## Future iOS mapping note
The iOS app will likely:
1. receive normalized contour points
2. map them into preview image coordinates
3. draw them using CAShapeLayer, Core Graphics, or Metal

Therefore normalized contour points should always be present.
