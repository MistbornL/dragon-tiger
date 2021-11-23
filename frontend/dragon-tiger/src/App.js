import "./App.css";
import { useState, useEffect, useRef } from "react";
import io from "socket.io-client";
function App() {
  const socket = useRef(null);
  const [response, setResponse] = useState("");
  useEffect(() => {
    socket.current = io("http://localhost:8000");
  }, []);

  return (
    <div className="App">
      <h1>Welcome</h1>
    </div>
  );
}

export default App;
