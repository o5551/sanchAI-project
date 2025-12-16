import { useState } from "react";

function App() {
  const [input, setInput] = useState("");
  const [response, setResponse] = useState("");

  const sendMessage = async () => {
    const res = await fetch("http://127.0.0.1:8000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: input })
    });

    const data = await res.json();
    setResponse(data.response);
  };

  return (
    <div style={{ padding: "40px" }}>
      <h2>🌤️ Weather Assistant</h2>

      <input
        type="text"
        value={input}
        onChange={e => setInput(e.target.value)}
        placeholder="Ask weather of any city"
        style={{ width: "300px", padding: "8px" }}
      />

      <br /><br />

      <button onClick={sendMessage}>Send</button>

      <p><b>Response:</b> {response}</p>
    </div>
  );
}

export default App;
