import "./App.css";
import { useState, useEffect, useRef } from "react";
import io from "socket.io-client";
import GenerateCards from "./service/generate";
import ShuffleCards from "./service/shuffle";
function App() {
  const socket = useRef(null);
  const [response, setResponse] = useState("");

  const clickHandle = () => {};

  useEffect(() => {
    socket.current = io("http://localhost:8000", {
      transports: ["websocket"],
      path: "/ws/socket.io",
    });
  }, []);

  var deck = [];
  const forms = ["D", "S", "C", "H"];
  const numbers = [
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "J",
    "Q",
    "K",
    "A",
  ];

  GenerateCards(deck, forms, numbers);
  ShuffleCards(deck);
  console.log(deck);

  return (
    <div className="App">
      <div className="container">
        <div className="tiger">
          <span>tiger</span>
        </div>
        <div className="dragon">
          <span>dragon</span>
        </div>
        <div className="btn">
          <button>Deal</button>
        </div>
      </div>
    </div>
  );
}

export default App;
