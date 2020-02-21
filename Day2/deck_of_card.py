class Card:

    def __init__(self,value,suit):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f'{self.value} of {self.suit} '

c=Card('A','Hearts')
print(c) 