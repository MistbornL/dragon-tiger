import React, {useEffect, useState} from 'react';
import axios from "axios";


const Home = () => {
    const [games, setGames] = useState([])

    const getGames = async () => {
        const response = await axios.get("http://localhost:8000/api/get/all/game")
        setGames(response.data)
    }


    useEffect(() => {
        getGames()
    }, [])


    const renderGames = () => {
        return games.map(game => {
            return (
                <div>
                    <h1>{game.name}</h1>
                    <h2>{game._id}</h2>
                    <a href={`http://localhost:3000/game/${game._id}`}>GADAVEDIT </a>
                </div>
            )
        })
    }

    return (
        <div>
            <h1>
                Home
                {renderGames()}
            </h1>
        </div>

    )
}

export default Home;
