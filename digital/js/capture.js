// =======================================================
// Capture
// =======================================================

let isDrawing = false;

let previousX = 0;
let previousY = 0;

let currentStroke = [];
let strokeStartTime = 0;

canvas.addEventListener("pointerdown", startStroke);
canvas.addEventListener("pointermove", continueStroke);
canvas.addEventListener("pointerup", finishStroke);
canvas.addEventListener("pointerleave", finishStroke);

function startStroke(event) {

    isDrawing = true;

    previousX = event.offsetX;
    previousY = event.offsetY;

    currentStroke = [];
    strokeStartTime = performance.now();

    currentStroke.push({
        x: event.offsetX,
        y: event.offsetY,
        t: 0
    });

}

function continueStroke(event) {

    if (!isDrawing) return;

    drawSegment(
        previousX,
        previousY,
        event.offsetX,
        event.offsetY
    );

    currentStroke.push({
        x: event.offsetX,
        y: event.offsetY,
        t: performance.now() - strokeStartTime
    });

    previousX = event.offsetX;
    previousY = event.offsetY;

}

function finishStroke() {

    if (!isDrawing) return;

    if (currentStroke.length > 0) {
        onStrokeFinished(currentStroke);
    }

    isDrawing = false;

}