from card import Card
import random

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def __len__(self):
        return len(self.cards)
    
    def show(self):
        for card in self.cards:
            print(card.show())

    def build(self):
        self.cards = []
        for suit in Card.SUITS:
            for value in range(2,15):
                self.cards.append(Card(suit, value))

    def shuffle(self):
       random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()