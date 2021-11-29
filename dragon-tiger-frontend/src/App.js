import "./App.css";
import { useState, useEffect, useRef } from "react";
import io from "socket.io-client";

import {Route, Router} from "react-router-dom";
import Home from "./Home";
import Game from "./Game";

import route_history from "./router_history";

function App() {
  const socket = useRef(null);
  const [response, setResponse] = useState("");

  const clickHandle = () => {};

  useEffect(() => {
    socket.current = io("http://localhost:8000", {
      transports: ["websocket"],
      path: "/ws/socket.io",
      query:{'game_id': 12312313}
    });
  }, []);

  return (
      <Router history={route_history} >
      <div className="App">
          <Route path="/" exact component={Home} />
          <Route path="/game/:id" exact component={Game} />
      </div>
    </Router>
  );
}

export default App;
