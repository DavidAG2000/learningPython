import random

suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
card_deck = []
random_cards = []

for suit in suits:
  for rank in ranks:
    card_deck.append(f'{rank} of {suit}')

print(f'There are {len(card_deck)} cards in the deck.')
print("Dealing...")

while len(random_cards) < 5:
    card = random.choice(card_deck)
    random_cards.append(card)
    card_deck.remove(card)
# print(random_cards)

print(f'There are {len(card_deck)} cards in the deck.')
# print(card_deck)

print("Player has the following cards in the deck:")
print(random_cards)