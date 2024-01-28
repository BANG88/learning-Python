import collections
from random import choice
import json
Card = collections.namedtuple('Card', ['rank', 'suit'])
class FrenchDeck:
	ranks = [str(n) for n in range(2, 11)]+list('JQKA')
	suits = 'spades diamonds clubs hearts'.split()

	def __init__(self):
		self._card = [Card(rank, suit) for suit in self.suits
										for rank in self.ranks]

	def __len__(self):
		return len(self._card)

	def __getitem__(self, position):
		return self._card[position]
	

beer_card = Card('7', 'diamonds')
print(beer_card)
deck = FrenchDeck()
print(json.dumps(deck._card, default=lambda obj: obj.__dict__, sort_keys=True, indent=4))
print(len(deck))
print(deck[0])
print(deck[-1])

print(choice(deck))