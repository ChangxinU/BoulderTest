# Project Brief

## Overview
We are building an iOS app that will eventually identify climbing holds on a climbing wall and draw contours along each hold boundary.

At the current stage, the iOS front end is being developed separately.
This repository is for preparing the algorithm module first.

## Product objective
Prepare a reusable ML module that can later be connected to iOS with minimal friction.

## Functional target
Input:
- single wall image or single camera frame

Output:
- list of detected holds
- segmentation-derived contour for each hold
- coordinates usable by iOS overlay rendering

## Phase 1 focus
- dataset understanding
- baseline segmentation pipeline
- contour extraction
- evaluation
- export path toward Core ML

## Non-goals in phase 1
- real-time video tracking
- route recommendation
- hold color grouping unless trivial
- full iOS integration
- production optimization on-device

## Quality priorities
1. correct hold contours
2. modularity
3. exportability
4. lightweight deployment path
5. easy future iOS integration

## Expected engineering outcome
A future engineer should be able to:
- place data in `ml/data/`
- train a baseline model
- evaluate it
- run local inference
- export toward Core ML
- hand the output contract to the iOS app
