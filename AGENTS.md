# AGENTS.md

## Mission
Build a climbing-hold segmentation module that can be trained, evaluated, exported to Core ML, and integrated later into an iOS app.

## Product intent
The current milestone is **algorithm preparation**, not iOS UI integration.
The output of the ML module must be easy to connect to an iOS app later.

Target task:
- Input: wall image or camera frame
- Output: per-hold segmentation mask and closed contour path
- Later iOS use: render contours on top of a preview image

## Operating rules
1. Read the repository before editing.
2. Prefer small, modular, reviewable changes.
3. Keep Python code runnable from the repo root.
4. Do not introduce heavy dependencies unless clearly justified.
5. Prefer lightweight models suitable for later Core ML export.
6. Preserve a clean separation between:
   - dataset parsing
   - training
   - evaluation
   - inference
   - postprocessing
   - export
7. When information is missing, make the most reasonable assumption and document it.

## Current scope
In scope:
- dataset inspection and adaptation
- training pipeline scaffolding
- evaluation pipeline scaffolding
- segmentation postprocessing
- contour extraction
- Core ML export scaffolding
- documentation for iOS integration contract

Out of scope for now:
- iOS UI implementation
- real-time camera integration
- backend services
- cloud training infra
- large-scale optimization beyond what the dataset supports

## Expected deliverables
- dataset adapter(s)
- config file(s)
- train/eval/export scripts
- postprocessing utilities
- documented output schema for iOS
- concise README updates

## Data assumptions
The dataset may arrive in one of these forms:
- COCO segmentation
- YOLO segmentation polygons
- binary masks per image
- custom JSON annotations

Support the actual format found in `ml/data/`.
If needed, add a conversion utility into `ml/tools/`.

## Model guidance
Default direction:
- lightweight instance segmentation first
- optimize for later iOS deployment
- prefer exportability over peak research accuracy

Suggested order of preference:
1. Ultralytics YOLO segmentation style pipeline
2. simple modular baseline if dataset is too custom
3. only introduce heavier frameworks if strongly justified

## Postprocessing guidance
The algorithm module should expose a clear path:
- image -> predictions
- predictions -> masks
- masks -> contour polygons
- contour polygons -> normalized output for iOS

Desired contour behavior:
- closed paths
- small-noise filtering
- optional simplification
- confidence thresholding

## Verification
For every meaningful implementation task:
- explain what changed
- list touched files
- describe how to run it
- describe known risks or open questions

## Working style
Before major edits:
- inspect relevant files
- produce a short plan
- then implement

After implementation:
- summarize
- include commands to validate

## Key docs to read first
- `README.md`
- `docs/project_brief.md`
- `docs/dataset_spec.md`
- `docs/ios_integration_contract.md`
- `docs/acceptance_criteria.md`
- `plans/current_plan.md`

## Directory intent
- `ml/data/` raw or sample data
- `ml/configs/` training and inference configs
- `ml/datasets/` dataset readers and transforms
- `ml/training/` train/eval/export entrypoints
- `ml/inference/` local prediction entrypoints
- `ml/postprocess/` contour extraction and formatting
- `ml/tools/` dataset conversion and utilities
- `docs/` product and engineering specs
- `prompts/` reusable Codex prompts

## Preferred output contract
Return a list of holds like:
- hold_id
- score
- bbox
- mask_size
- contour_points
- normalized_contour_points
- optional color metadata if inferable

See `docs/ios_integration_contract.md`.

## Completion bar for initial repo setup
A good first pass should:
- inspect the dataset shape
- decide a baseline format
- scaffold training/eval/export
- scaffold contour extraction
- leave clear run instructions
