const input = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");
const chatBox = document.getElementById("chat-box");
const micBtn = document.getElementById("mic-btn");

function addMessage(text, sender) {
    const div = document.createElement("div");
    div.className = sender;
    div.textContent = text;
    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
}

// ==========================
// Text to Speech
// ==========================

function speak(text) {
    if (!("speechSynthesis" in window)) {
        console.log("Text-to-speech not supported in this browser.");
        return;
    }

    window.speechSynthesis.cancel();

    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = "en-US";
    utterance.rate = 1;
    utterance.pitch = 1;

    window.speechSynthesis.speak(utterance);
}

// ==========================
// Greet user on page load
// ==========================

window.addEventListener("load", () => {
    const greeting = "Hello! How can I help you today?";
    addMessage(greeting, "bot");
    speak(greeting);
});

async function sendMessage(message) {

    if (message === "") return;

    addMessage(message, "user");
    addMessage("🤖 Thinking...", "bot");
    input.value = "";

    try {

        const response = await fetch("http://127.0.0.1:8000/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message
            })
        });

        if (!response.ok) {
            throw new Error("Server returned " + response.status);
        }

        const data = await response.json();
        const thinking = document.querySelector(".bot:last-child");

        thinking.innerText = data.response;

        speak(data.response);

    } catch (error) {

        console.error(error);

        addMessage("Error: " + error.message, "bot");
    }

}

sendBtn.onclick = function () {
    const message = input.value.trim();
    sendMessage(message);
};

/// ==========================
// Speech to Text
// ==========================

const SpeechRecognition =
    window.SpeechRecognition || window.webkitSpeechRecognition;

if (SpeechRecognition) {

    const recognition = new SpeechRecognition();

    recognition.lang = "en-US";
    recognition.continuous = false;
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;

    micBtn.addEventListener("click", () => {

        micBtn.innerHTML = "🎙️ Listening...";

        recognition.start();

    });

    recognition.onstart = () => {
        console.log("Listening...");
    };

    recognition.onresult = (event) => {

        const transcript = event.results[0][0].transcript;

        console.log("You said:", transcript);

        input.value = transcript;

        micBtn.innerHTML = "🎤";

        sendMessage(transcript);
    };

    recognition.onend = () => {

        micBtn.innerHTML = "🎤";

        console.log("Stopped listening.");

    };

    recognition.onerror = (event) => {

        micBtn.innerHTML = "🎤";

        console.log(event.error);

        if (event.error !== "no-speech") {
            alert("Error: " + event.error);
        }

    };

} else {

    alert("Speech Recognition is not supported in this browser.");

}