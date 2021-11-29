import React, { useEffect, useRef, useState } from "react";
import { useParams } from "react-router-dom";
import io from "socket.io-client";

const Game = () => {
  const { id } = useParams();
  const [gameSpec, setGameSpec] = useState({});
  const [card, setCard] = useState("");

  const socket = useRef(null);

  // aqedan davukavshirdit servers
  useEffect(() => {
    socket.current = io("http://localhost:8000", {
      path: "/ws/socket.io",
      query: { game_id: id },
      transports: ["websocket"],
    });
  }, []);

  // am efectis sashualebit simon mogvaq simon data romelsac ipovit backend/server/server.py shi kerdzod es  simon
  // send_data = {
  //     "min_bet": game.minBet,
  //     "max_bet": game.maxBet,
  //     "name": game.name,
  //     "game_round_id": str(game_round.id)
  // }
  // sadac game aris collectioni
  useEffect(() => {
    socket.current.on("on_connect_data", (data) => {
      setGameSpec(data);
    });
  }, []);

  // es aris kartis daskanerebis logika romelsac vugzavnit backs karti ki shemogvaq qvemot inputidan anu rasac inputshi vwert is iqneba karti da es logika agzavnis backendtan
  const sendCard = (e) => {
    e.preventDefault();
    socket.current.emit("scan_card", {
      card: card,
    });
  };

  return (
    <div>
      {/* aq ori xazi nishnavs tu ar gvaqvs minimum betis data mashin gvaq prosta "" eseni simon */}
      <h1>min_bet: {gameSpec.min_bet || ""}</h1>

      <h1>max_bet: {gameSpec.max_bet || ""}</h1>
      <div>
        <form onSubmit={sendCard}>
          {/* aqana shegvaq karti setcardit vimaxsovrebt karts rom magla gavatanot logikas sendCard simon)))) */}
          <input
            onChange={(event) => setCard(event.target.value)}
            value={card}
          />
        </form>
      </div>
    </div>
  );
};

export default Game;
