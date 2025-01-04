document.addEventListener('DOMContentLoaded', function () {
    const userInput = document.getElementById("user-input");
    userInput.focus();

    const chatForm = document.getElementById("chat-form");
    const chatBox = document.getElementById("chat-box");
    const sendButton = document.getElementById("send-button");

    chatForm.addEventListener("submit", async (e) => {
        e.preventDefault();
        const message = userInput.value;

        userInput.value = "";
        sendButton.disabled = true;

        chatBox.classList.add('has-content');

        const userMessage = document.createElement("p");
        userMessage.innerHTML = `<strong>${message}</strong> <span class="spinner"></span>`;
        chatBox.appendChild(userMessage);

        const loadingSpinner = userMessage.querySelector(".spinner");
        loadingSpinner.style.display = "inline-block";

        const response = await fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message })
        });

        const data = await response.json();

        loadingSpinner.style.display = "none";
        const botMessage = document.createElement("p");
        botMessage.textContent = data.response;
        chatBox.appendChild(botMessage);

        chatBox.scrollTop = chatBox.scrollHeight;

        sendButton.disabled = false;
    });
});
