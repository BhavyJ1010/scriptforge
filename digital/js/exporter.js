// =======================================================
// Exporter
// =======================================================

function downloadRecording(recording) {

    const json = JSON.stringify(recording, null, 4);

    const blob = new Blob(
        [json],
        { type: "application/json" }
    );

    const url = URL.createObjectURL(blob);

    const link = document.createElement("a");

    link.href = url;
    link.download = "recording.json";

    link.click();

    URL.revokeObjectURL(url);

}