// =======================================================
// Canvas
// =======================================================

const canvas = document.getElementById("drawingCanvas");
const context = canvas.getContext("2d");

const PEN_WIDTH = 3;
const PEN_COLOR = "#000000";

function configureCanvas() {

    const rect = canvas.getBoundingClientRect();

    canvas.cssWidth = rect.width;
    canvas.cssHeight = rect.height;
    
    const dpr = window.devicePixelRatio || 1;

    canvas.width = rect.width * dpr;
    canvas.height = rect.height * dpr;

    context.resetTransform();
    context.scale(dpr, dpr);

    context.lineWidth = PEN_WIDTH;
    context.lineCap = "round";
    context.lineJoin = "round";
    context.strokeStyle = PEN_COLOR;

}

function drawSegment(x1, y1, x2, y2) {

    context.beginPath();
    context.moveTo(x1, y1);
    context.lineTo(x2, y2);
    context.stroke();

}

function clearCanvas() {

    context.clearRect(
        0,
        0,
        canvas.width,
        canvas.height
    );

}

configureCanvas();

window.addEventListener("resize", configureCanvas);