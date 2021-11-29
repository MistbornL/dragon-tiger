import React, {useEffect, useRef, useState} from 'react';
import {useParams} from "react-router-dom";
import io from "socket.io-client";


const Game = () => {
    const {id} = useParams()
    const [gameSpec, setGameSpec] = useState({})
    const [card, setCard] = useState("");

    const socket = useRef(null);

    useEffect(() => {
        socket.current = io("http://localhost:8000", {
            path: "/ws/socket.io",
            query:{'game_id': id},
            transports: ["websocket"],
        });
    }, []);

    useEffect(() => {
        socket.current.on("on_connect_data", (data) => {
            setGameSpec(data)
        })
    }, [])

    const sendCard = (e) => {
        e.preventDefault()
        socket.current.emit("scan_card", {
            "card": card
        })
    }

    return (
        <div>
            <h1>
                min_bet: {gameSpec.min_bet || ""}
            </h1>

            <h1>
                max_bet: {gameSpec.max_bet || ""}
            </h1>
            <div>
                <form onSubmit={sendCard}>
                <input
                    onChange={event => setCard(event.target.value)}
                    value={card}
                />
                </form>
            </div>
        </div>
    )
}

export default Game;
