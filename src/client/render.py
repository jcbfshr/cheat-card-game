# render.py

class Card:
  def __init__(self,value : str ="",suit : str =""):
    self.value = {
      "1":"1",
      "2":"2",
      "3":"3",
      "4":"4",
      "5":"5",
      "6":"6",
      "7":"7",
      "8":"8",
      "9":"9",
      "10":"X",
      "j":"J",
      "11":"J",
      "q":"Q",
      "12":"Q",
      "k":"K",
      "13":"K",
      "": " "
    }[value.lower()]
    self.suit = suit.lower()
    self.suit_unicode = {
      "spades":"♠",
      "hearts":"♥",
      "clubs":"♣",
      "diamonds":"♦",
      "":" "
    }[self.suit]

class Hand:
  def __init__(self,cards):
    self.cards = cards

  def out(self):
    output = [""]
    for i in range(len(self.cards)):
      card = self.cards[i]
      if i == len(self.cards)-1:
        for x in range(len(output)):
          if x == 0:
            output[x] += "┌───────┐"
          elif x == 1:
            output[x] += f"|{card.value}      |"
          elif x == 2:
            output[x] += f"|{card.suit_unicode}      |"
          elif x == len(output)-1:
            output[x] += "└───────┘"
          elif x == len(output)-2:
            output[x] += f"|      {card.value}|"
          else:
            output[x] += "|       |"
      elif i == 0:
        output = [
          "┌─",
          f"│{card.value}",
          f"│{card.suit_unicode}",
          "│ ",
          "│ ",
          "└─"
        ]
      else:
        for x in range(len(output)):
          if x == 0:
            output[x] += "┌─"
          elif x == 1:
            output[x] += f"|{card.value}"
          elif x == 2:
            output[x] += f"|{card.suit_unicode}"
          elif x == len(output)-1:
            output[x] += "└─"
          else:
            output[x] += "| "
    return output