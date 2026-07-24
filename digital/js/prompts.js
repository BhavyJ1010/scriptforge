// =======================================================
// Prompts
// =======================================================

const promptText = document.getElementById("promptText");

function getCurrentPrompt() {

    return {
        text: promptText.textContent.trim()
    };

}