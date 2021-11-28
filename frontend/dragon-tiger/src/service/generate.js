const GenerateCards = (deck, forms, numbers) => {
  for (var i = 0; i <= 7; i++) {
    forms.forEach((form) =>
      numbers.forEach((number) => deck.push(`${form}${number}`))
    );
  }

  return deck;
};

export default GenerateCards;
