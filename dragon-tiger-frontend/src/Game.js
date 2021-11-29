import React, {useEffect, useRef} from 'react';
import {useParams} from "react-router-dom";
import io from "socket.io-client";


const Game = () => {
    const {id} = useParams()

    const socket = useRef(null);

    useEffect(() => {
        socket.current = io("http://localhost:8000", {
            transports: ["websocket"],
            path: "/ws/socket.io",
            query:{'game_id': id}
        });
    }, []);
    return (
        <div>
            Game
        </div>
    )
}

export default Game;
