// =======================================================
// Prompts
// =======================================================

const promptText = document.getElementById("promptText");

let prompts = [];

let currentPromptIndex = 0;


// -------------------------------------------------------
// Load Prompt Library
// -------------------------------------------------------

async function loadPrompts() {

    const response = await fetch("prompts/prompts_v1.json");

    prompts = await response.json();

    currentPromptIndex = 0;

    updatePromptDisplay();

}


// -------------------------------------------------------
// Current Prompt
// -------------------------------------------------------

function getCurrentPrompt() {

    return prompts[currentPromptIndex];

}


// -------------------------------------------------------
// Next Prompt
// -------------------------------------------------------

function nextPrompt() {

    if (currentPromptIndex < prompts.length - 1) {

        currentPromptIndex++;

        updatePromptDisplay();

        return true;

    }

    promptText.textContent = "Done — Thanks!";

    return false;

}


// -------------------------------------------------------
// UI
// -------------------------------------------------------

function updatePromptDisplay() {

    promptText.textContent =
        prompts[currentPromptIndex].text;

}


// -------------------------------------------------------
// Initialize
// -------------------------------------------------------

loadPrompts().then(() => {

    initializeApp();

});