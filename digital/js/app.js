// =======================================================
// App
// =======================================================

let recording;
let currentPointerType = "unknown";
let strokeCounter = 0;

function createNewRecording() {

    strokeCounter = 0;

    return {

        schema_version: 1,

        prompt: getCurrentPrompt(),

        device: {

            pointer_type: currentPointerType,

            device_pixel_ratio: window.devicePixelRatio || 1,

            canvas_width: canvas.cssWidth,

            canvas_height: canvas.cssHeight

        },

        acquisition: {

            app_version: "0.1.0",

            recording_start_time: new Date().toISOString(),

            mode: "digital"

        },

        strokes: []

    };

}

function initializeApp() {

    recording = createNewRecording();

}

function onStrokeFinished(stroke) {

    strokeCounter++;

    recording.strokes.push({

        id: strokeCounter,

        points: stroke

    });

}

function updatePointerType(type) {

    recording.device.pointer_type = type;

}

clearButton.addEventListener("click", () => {

    clearCanvas();

    recording = createNewRecording();

});

saveButton.addEventListener("click", () => {

    downloadRecording(recording);

    if (nextPrompt()) {

        clearCanvas();

        recording = createNewRecording();

    } else {

        clearCanvas();

    }

});