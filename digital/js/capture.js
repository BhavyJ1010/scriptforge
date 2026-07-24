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

    updatePointerType(event.pointerType || "unknown");

    previousX = event.offsetX;
    previousY = event.offsetY;

    currentStroke = [];
    strokeStartTime = performance.now();

    currentStroke.push({

    x: event.offsetX,
    y: event.offsetY,
    t: 0,

    pressure: event.pressure ?? 0,

    tilt_x: event.tiltX ?? 0,
    tilt_y: event.tiltY ?? 0,

    twist: event.twist ?? 0

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
    t: performance.now() - strokeStartTime,

    pressure: event.pressure ?? 0,

    tilt_x: event.tiltX ?? 0,
    tilt_y: event.tiltY ?? 0,

    twist: event.twist ?? 0

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