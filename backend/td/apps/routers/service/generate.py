from typing import List


def generate_deck(deck: List, forms: List, numbers: List) -> List:
    for form in forms:
        for number in numbers:
            deck.append(f"{form}{number}")

    deck = deck * 8
    return deck
