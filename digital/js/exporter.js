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
    const safePrompt = recording.prompt.text
    .replace(/\s+/g, "_")
    .replace(/[^a-zA-Z0-9_]/g, "");

    link.download =
        `${String(recording.prompt.id).padStart(3, "0")}_${safePrompt}.json`;

    link.click();

    URL.revokeObjectURL(url);

}