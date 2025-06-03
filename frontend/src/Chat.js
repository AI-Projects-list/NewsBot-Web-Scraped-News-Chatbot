import React, { useState } from 'react';
import axios from 'axios';

function Chat() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    const res = await axios.post("http://localhost:5000/chat", { message: input });
    setMessages([...messages, { user: input, bot: res.data.response }]);
    setInput("");
  };

  return (
    <div>
      <h2>News Chatbot</h2>
      {messages.map((msg, i) => (
        <div key={i}>
          <b>You:</b> {msg.user}<br />
          <b>Bot:</b> {msg.bot}
        </div>
      ))}
      <input value={input} onChange={(e) => setInput(e.target.value)} />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
}

export default Chat;