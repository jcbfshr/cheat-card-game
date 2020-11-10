from render import Hand,Card
from random import randrange

class Deck:
    def __init__(self):
        self.cards = []
        for suit in ["spades","hearts","clubs","diamonds"]:
            for i in range(1,14):
                self.cards.append(Card(str(i),suit))
    
    # fisher-yates shuffle algorithm
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            j = randrange(0,i+1)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
    
    def deal(self,players):
        while True:
            for player in players:
                if len(self.cards) == 0:
                    return
                else:
                    player.cards.append(self.cards[0])
                    self.cards.pop(0)

class Player:
    def __init__(self,name : str, ):
        self.name = name[:8]
        self.cards = []

players = [Player("lewis"),Player("jacob"),Player("louis"),Player("jack")]
d = Deck()
for i in range(100000):
    d.shuffle()
    if i % 5000 == 0:
        print(i)
d.deal(players)

for player in players:
    print(player.name)
    h = Hand(player.cards)
    for line in h.out():
        print(line)