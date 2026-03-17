# Dataset Spec

## Purpose
Describe the climbing dataset format used for training and evaluation.

## Current state
The repository is empty by default. Replace this document with concrete details once sample data is added.

## Expected information to fill in
- dataset source
- license / usage constraints
- directory layout
- class names
- annotation format
- train / val / test split
- image resolution range
- number of images
- representative edge cases

## Supported candidate formats
### Option A: COCO segmentation
Typical files:
- `images/train/*.jpg`
- `images/val/*.jpg`
- `annotations/instances_train.json`
- `annotations/instances_val.json`

### Option B: YOLO segmentation
Typical files:
- `images/train/*.jpg`
- `labels/train/*.txt`
- `images/val/*.jpg`
- `labels/val/*.txt`

### Option C: mask-per-instance or mask-per-image
Typical files:
- `images/*.jpg`
- `masks/*.png`

### Option D: custom JSON
Typical files:
- `images/*.jpg`
- `annotations/*.json`

## Annotation semantics to confirm
- Are volumes and holds separate classes?
- Are wall regions annotated?
- Are contour polygons already available?
- Are masks per hold or merged by class?
- Is hold color important for later route logic?

## Required outcome for Codex
Codex should inspect the actual data in `ml/data/`, identify the true format, and then:
- update this file
- implement the corresponding adapter in `ml/datasets/`
- document assumptions and risks

## Example fields to document
- classes:
  - hold
  - volume
  - wall
- split counts
- invalid annotation patterns
- expected preprocessing
