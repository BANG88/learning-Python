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
print(deck[0])
print(deck[-1])

print(choice(deck))

print()

print(len(deck))

for card in deck:
	print(card)


# “牌面大小按点数（A 最大），以及黑桃（最大）、红心、方块、梅花（最小）的顺序排列。下面按照这个规则定义扑克牌排序函数，梅花 2 返回 0，黑桃 A 返回 51。”
print('sorted\n')

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)	
def spades_high(card):
	rank_value = FrenchDeck.ranks.index(card.rank)
	return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
	print(card)