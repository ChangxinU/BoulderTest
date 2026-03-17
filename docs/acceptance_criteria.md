# Acceptance Criteria

## Repository setup success
The initial implementation is acceptable if it provides:

1. A clear dataset ingestion path
2. A baseline segmentation training path
3. A local evaluation path
4. A local inference path
5. A contour extraction path
6. A documented export path toward Core ML
7. A documented iOS-facing output contract

## Functional acceptance
### Dataset
- The dataset format is explicitly identified
- Sample loading works
- Split assumptions are documented

### Training
- There is a clear training entrypoint
- Config parameters are externalized where practical
- Model choice is justified for iOS deployment goals

### Evaluation
- There is a script or module for evaluation
- At minimum, mask or detection quality metrics are planned
- Failure cases can be logged for review

### Postprocessing
- Masks can be transformed into contours
- Small-noise regions can be filtered
- Contours can be simplified
- Output is stable and documented

### Export
- There is a script scaffold or implementation for Core ML export
- Input/output shape assumptions are documented
- Any blockers are documented clearly

### Documentation
- README explains the workflow
- Docs reflect actual implemented choices
- iOS contract is concrete enough for later app integration

## Nice-to-have
- sample unit tests
- sample visual debug output
- sample JSON prediction dump
