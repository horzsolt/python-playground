class Card(object):

    SUITS = ["diamonds", "clubs", "hearts", "spades"]

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.suitIndex = self.SUITS.index(suit)

    def __str__(self):
        return self.getFileName()

    def getFileName(self):
        return f'{self.value}_of_{self.suit}'
    

