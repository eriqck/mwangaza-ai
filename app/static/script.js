
const chatForm = document.getElementById("chat-form");
const questionInput = document.getElementById("question-input");
const sendButton = document.getElementById("send-button");
const chatMessages = document.getElementById("chat-messages");
const suggestionButtons = document.querySelectorAll(".suggestion-button");

// Add a message to the chat window.
function addMessage(text, sender) {
    const message = document.createElement("div");
    message.classList.add("message", `${sender}-message`);

    const content = document.createElement("div");
    content.classList.add("message-content");

    const label = document.createElement("div");
    label.classList.add("message-label");
    label.textContent = sender === "assistant" ? "MWANGAZA AI" : "YOU";

    const bubble = document.createElement("div");
    bubble.classList.add("message-bubble");
    bubble.textContent = text;

    content.appendChild(label);
    content.appendChild(bubble);

    if (sender === "assistant") {
        const avatar = document.createElement("div");
        avatar.classList.add("message-avatar");
        avatar.textContent = "M";

        message.appendChild(avatar);
    }

    message.appendChild(content);
    chatMessages.appendChild(message);


    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Send the user's question to the FastAPI backend.
async function askAssistant(question) {
    addMessage(question, "user");

    sendButton.disabled = true;
    sendButton.textContent = "Thinking...";

    try {
        const response = await fetch("/assistant/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                question: question
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "Something went wrong.");
        }

        addMessage(data.answer,"assistant");

    } catch (error) {
        addMessage(
            `I'm sorry, I couldn't process your request. ${error.message}`,
            "assistant"
        );
    } finally {
        sendButton.disabled = false;
        sendButton.innerHTML = 'Send <span>→</span>';
        questionInput.focus();
    }
}

// Handle questions submitted through the input field.
chatForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const question = questionInput.value.trim();

    if (!question) {
        return;
    }

    questionInput.value = "";

    await askAssistant(question);
});

// Handle the sample question buttons.
suggestionButtons.forEach((button) => {
    button.addEventListener("click", async () => {
        const question = button.dataset.question;

        if (!sendButton.disabled) {
            await askAssistant(question);
        }
    });
});
