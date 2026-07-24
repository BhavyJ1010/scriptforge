// =======================================================
// App
// =======================================================

function createNewRecording() {

    return {

        schema_version: 1,

        prompt: getCurrentPrompt(),

        device: {

            pointer_type: "unknown",

            device_pixel_ratio: window.devicePixelRatio || 1,

            canvas_width: canvas.width,

            canvas_height: canvas.height

        },

        acquisition: {

            app_version: "0.1.0",

            recording_start_time: new Date().toISOString(),

            mode: "digital"

        },

        strokes: []

    };

}

function onStrokeFinished(stroke) {
    recording.strokes.push(stroke);
}

let recording = createNewRecording();

clearButton.addEventListener("click", () => {

    clearCanvas();

    recording = createNewRecording();

});

saveButton.addEventListener("click", () => {

    downloadRecording(recording);

});