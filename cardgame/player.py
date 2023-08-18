class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def sayHello(self):
        return f"Hi! My name is {self.name}"

    def win(self, card):
        self.hand.append(card)
    
    def lose(self):
        self.hand.pop()

    def isWinner(self, card):
        if (self.currentCard.value > card.value): 
            return True
        elif (self.currentCard.value == card.value):
            if (self.currentCard.suitIndex >= card.suitIndex):
                return True
            else:
                return False
        else:
            return False        
        
    def draw(self, deck):
        card = deck.deal()
        if card:
            self.hand.append(card)
            self.currentCard = card
        else: 
            return False
        return True

    def showHand(self):
        return len(self.hand)
