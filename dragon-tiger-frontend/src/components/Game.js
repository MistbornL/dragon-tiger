import React, { useEffect, useRef, useState } from "react";
import { useParams } from "react-router-dom";
import io from "socket.io-client";
import Table from "./table/table";

const Game = () => {
  const { id } = useParams();
  const [gameSpec, setGameSpec] = useState({});
  const [card, setCard] = useState("");
  const [bet, setBet] = useState(null);

  const socket = useRef(null);

  const handleChange = (e) => {
    setCard(e.target.value);
  };
  console.log(card);
  const handleChangeBet = (e) => {
    setBet(e.target.value);
  };

  useEffect(() => {
    socket.current = io("http://localhost:8000", {
      path: "/ws/socket.io",
      query: { game_id: id },
      transports: ["websocket"],
    });
  }, []);

  useEffect(() => {
    socket.current.on("on_connect_data", (data) => {
      setGameSpec(data);
    });
  }, []);

  const sendCard = (e) => {
    e.preventDefault();
    socket.current.emit("scan_card", {
      card: card,
    });
    console.log(card);
  };

  const sendBet = (e) => {
    e.preventDefault();
    socket.current.emit("receive_bet", {
      bet: bet,
    });
  };

  return (
    <div>
      <Table
        gameSpec={gameSpec}
        sendCard={sendCard}
        sendBet={sendBet}
        card={card}
        handleChange={handleChange}
        handleChangeBet={handleChangeBet}
        bet={bet}
      />
    </div>
  );
};

export default Game;
