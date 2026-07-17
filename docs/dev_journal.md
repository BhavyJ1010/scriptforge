# ScriptForge Development Journal

## Milestone 0 - Project Bootstrap
### Built
- Designed initial project architecture.
- Initialized Git repository.
- Connected GitHub remote.
- Created Python virtual environment.
- Configured .gitignore.
- Added README and requirements.txt.
### Learned
- Git workflow
- Virtual environments
- Project structure
### Notes
- Established package-based project layout.

## Milestone 1 - Image Loader
### Built
- Implemented reusable image loader.
- Added input validation.
- Added preprocessing loader test.
### Learned
- cv2.imread()
- NumPy image representation
- Separation of engine and tests
### Notes
- First reusable preprocessing module completed.

## Milestone 2 - Image Resize
### Built
- Implemented aspect ratio preserving resize.
- Added configurable target width.
- Added resize test module.
### Learned
- Aspect ratio
- cv2.resize()
- Running modules using `python -m`
### Notes
- Verified resize mathematically and visually.

## Milestone 3 - Grayscale Conversion
### Built
- Implemented grayscale conversion module.
- Added grayscale preprocessing test.
- Verified image shape transformation and visual output.
### Learned
- `cv2.cvtColor()`
- BGR → Grayscale conversion
- Image channel representation
### Notes
- Grayscale removes the color channel while preserving image dimensions.

## Milestone 4 - Gaussian Blur
### Built
- Implemented Gaussian blur module.
- Added blur test module.
- Verified smoothing visually.
### Learned
- cv2.GaussianBlur()
- Kernel size
- Gaussian weighting
- Sigma
### Notes
- Blur reduces noise before edge detection.

## Milestone 5 - Document Contour Detection
### Built
- Implemented Canny edge detection.
- Added morphological closing for edge refinement.
- Implemented contour extraction and sorting.
- Added polygon approximation.
### Learned
- Canny edge detection
- Morphological closing
- Contour hierarchy and area
- Polygon approximation (approxPolyDP)
### Notes
- Clean contours require complete page boundaries.
- This stage prepares the image for perspective correction.

## Milestone 6 - Perspective Transform
### Built
- Implemented point ordering for document corners.
- Implemented four-point perspective transform.
- Added perspective transform test with contour validation.
### Learned
- Homography (cv2.getPerspectiveTransform)
- Perspective warping (cv2.warpPerspective)
- Importance of validating a quadrilateral before transforming.
### Notes
- Current implementation works when a valid 4-corner page contour is detected.
- Robust page selection will be improved in a later iteration.

## Milestone 7 - Lighting Normalization
### Built
- Added histogram equalization module.
- Added lighting normalization test.
### Learned
- cv2.equalizeHist()
- Contrast enhancement before thresholding.
### Notes
- Current implementation uses global histogram equalization; can later be upgraded to CLAHE.

## Milestone 8 - Adaptive Threshold
### Built
- Implemented adaptive threshold module.
- Added threshold preprocessing test.
### Learned
- Adaptive Gaussian thresholding.
- Local thresholding vs global thresholding.
### Notes
- Binary conversion performs well after lighting normalization.

## Milestone 9 - Unified Preprocessing Pipeline
### Built
- Added unified document preprocessing pipeline.
- Added end-to-end preprocessing test.
### Learned
- Integrating multiple preprocessing stages into a reusable pipeline.
- Color operations and grayscale operations require different image types.
### Notes
- Pipeline now returns intermediate outputs for debugging and reuse.

## Milestone 8 - Initial Character Segmentation
### Built
- Implemented initial character segmentation module.
- Detected connected components using contours.
- Returned bounding boxes for each detected component.
- Added visualization test for segmented components.
### Learned
- Connected components are not equivalent to complete characters.
- Broken handwriting strokes produce multiple contours for a single glyph.
### Notes
- Current implementation detects individual connected components only.
- Character grouping and glyph extraction will be handled in later modules.

# Current Pipeline
- [x] Image Loader
- [x] Image Resize
- [x] Grayscale
- [x] Gaussian Blur
- [x] Edge Detection
- [x] Morphology
- [x] Contour Detection
- [x] Perspective Transform
- [x] Lighting Normalization
- [x] Adaptive Threshold
- [x] Initial Character Segmentation
- [ ] Glyph Cleaning
- [ ] Glyph Library Builder
- [ ] Writer Profile Builder
- [ ] Layout Engine
- [ ] Handwriting Renderer
- [ ] Notebook Generator
- [ ] PNG/PDF 