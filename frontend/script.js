const chat = document.getElementById("chat");
const form = document.getElementById("chat-form");
const input = document.getElementById("message");

function addMessage(text, role) {
  const div = document.createElement("div");
  div.className = `message ${role}`;
  const span = document.createElement("span");
  span.textContent = text;
  div.appendChild(span);
  chat.appendChild(div);
  chat.scrollTop = chat.scrollHeight;
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const message = input.value.trim();
  if (!message) return;
  addMessage(message, "user");
  input.value = "";

  try {
    const res = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message }),
    });
    const data = await res.json();
    if (data.response) {
      addMessage(data.response, "assistant");
    } else {
      addMessage(data.error || "Error", "assistant");
    }
  } catch (err) {
    addMessage("Network error", "assistant");
  }
});
