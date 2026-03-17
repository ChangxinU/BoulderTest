# BoulderTest
# Climb Hold Segmentation Starter

This repository is a starter scaffold for preparing a climbing-hold recognition and contour extraction algorithm that will later be integrated into an iOS app.

## Goal
Build an algorithm module that can:

- ingest climbing wall images
- detect or segment climbing holds
- extract closed contours for each hold
- export a model suitable for later iOS Core ML integration

## Current status
This repository is intentionally scaffolded for Codex-driven implementation.

It already includes:

- product and engineering specs
- a repository-level `AGENTS.md`
- reusable prompts for Codex
- placeholder Python modules for:
  - dataset reading
  - training
  - evaluation
  - inference
  - postprocessing
  - Core ML export
- iOS integration contract documentation


## Dataset download (Kaggle)
Use the helper script to download the requested dataset into `ml/data/`:

```bash
python ml/tools/download_kaggle_dataset.py --output-dir ml/data
```

Requirements:
- Kaggle CLI installed (`kaggle`)
- Kaggle API credentials configured (`~/.kaggle/kaggle.json` or env vars)

Dataset:
- `tomasslama/indoor-climbing-gym-hold-segmentation`

## Suggested workflow
1. Put a representative subset of the climbing dataset into `ml/data/`.
2. Update `docs/dataset_spec.md` with the real annotation format if known.
3. Give Codex `prompts/01_repo_inspection.md`.
4. Then run the prompts in order:
   - `prompts/02_dataset_adapter.md`
   - `prompts/03_training_pipeline.md`
   - `prompts/04_export_and_contract.md`
   - `prompts/05_eval_and_error_analysis.md`

## Repository structure
```text
docs/
prompts/
plans/
ios_contract/
ml/
  data/
  configs/
  datasets/
  training/
  inference/
  postprocess/
  tools/
```

## Intended algorithm output
The eventual inference result should be easy for iOS to consume:

- hold confidence score
- contour points
- normalized contour points
- optional bounding box
- optional mask metadata

See:
- `docs/ios_integration_contract.md`
- `ios_contract/hold_output_schema.json`

## Notes for Codex
Codex should first read:
- `AGENTS.md`
- `README.md`
- `docs/project_brief.md`
- `docs/dataset_spec.md`
- `docs/acceptance_criteria.md`
- `plans/current_plan.md`

## Next action
Start with `prompts/01_repo_inspection.md`.
