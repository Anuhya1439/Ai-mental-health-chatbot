const chat = document.getElementById("chat");
const input = document.getElementById("input");
const sendBtn = document.getElementById("send");
const recordBtn = document.getElementById("record");
let mediaRecorder,
  audioChunks = [];

function addMessage(text, cls) {
  const d = document.createElement("div");
  d.className = `message ${cls}`;
  d.innerText = text;
  chat.appendChild(d);
  chat.scrollTop = chat.scrollHeight;
}

sendBtn.onclick = async () => {
  const t = input.value.trim();
  if (!t) return;
  addMessage(t, "user");
  input.value = "";
  const res = await fetch("/api/message", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text: t }),
  });
  const j = await res.json();
  addMessage(j.reply + "\n[emotion: " + j.emotion.top_label + "]", "bot");
};

recordBtn.onclick = async () => {
  if (!mediaRecorder) {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorder = new MediaRecorder(stream);
    mediaRecorder.ondataavailable = (e) => audioChunks.push(e.data);
    mediaRecorder.onstop = async () => {
      const blob = new Blob(audioChunks, { type: "audio/webm" });
      audioChunks = [];
      const fd = new FormData();
      fd.append("file", blob, "record.webm");
      addMessage("[voice message sent]", "user");
      const res = await fetch("/api/voice", { method: "POST", body: fd });
      const j = await res.json();
      addMessage(j.reply + "\n[emotion: " + j.emotion.top_label + "]", "bot");
    };
    mediaRecorder.start();
    recordBtn.innerText = "Stop";
  } else {
    mediaRecorder.stop();
    mediaRecorder = null;
    recordBtn.innerText = "Record Voice";
  }
};
