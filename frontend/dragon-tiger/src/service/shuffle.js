const ShuffleCards = (deck) => {
  deck.sort(() => Math.random() - 0.5);
};

export default ShuffleCards;
