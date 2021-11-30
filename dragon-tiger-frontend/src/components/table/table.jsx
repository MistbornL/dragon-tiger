import "./index.css";

const Table = ({
  gameSpec,
  sendCard,
  card,
  handleChange,
  handleChangeBet,
  bet,
  sendBet,
  handleChangeTarget,
  target,
  sendTarget,
}) => {
  return (
    <div className="cr">
      <div className="table">
        <h1>welcome to the table</h1>
        <p>min_bet: {gameSpec.min_bet || ""}</p>
        <p>max_bet: {gameSpec.max_bet || ""}</p>
        <form onSubmit={sendCard}>
          <input
            placeholder="Place Your Bets..."
            type="text"
            class="form-control"
            aria-label="Sizing example input"
            aria-describedby="inputGroup-sizing-sm"
            onChange={handleChangeBet}
            value={bet}
          />
          <br />
          <input
            placeholder="place bets on dragon/tiger..."
            type="text"
            class="form-control"
            aria-label="Sizing example input"
            aria-describedby="inputGroup-sizing-sm"
            onChange={handleChangeTarget}
            value={target}
          />
          <br />
          <input
            placeholder="Deal card..."
            type="text"
            class="form-control"
            aria-label="Sizing example input"
            aria-describedby="inputGroup-sizing-sm"
            onChange={handleChange}
            value={card}
          />
        </form>
      </div>
    </div>
  );
};

export default Table;
