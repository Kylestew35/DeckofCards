# Kyle Stewart CIS261 DeckofCards

import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.deck = [Card(rank, suit) for rank in ranks for suit in suits]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self, num_cards):
        dealt_cards = self.deck[:num_cards]
        self.deck = self.deck[num_cards:]
        return dealt_cards

    def count(self):
        return len(self.deck)

def main():
    deck = Deck()
    print("I have shuffled a deck of 52 cards.")
    
    while True:
        num_cards = int(input("How many cards would you like? "))
        if num_cards > deck.count():
            print(f"Sorry, only {deck.count()} cards left in the deck.")
            continue

        dealt_cards = deck.deal(num_cards)
        print("\nHere are your cards:")
        for card in dealt_cards:
            print(card)

        print(f"\nThere are {deck.count()} cards left in the deck.")
        print("Good luck!")
        
        cont = input("\nPress any key to continue or 'n' to exit: ").lower()
        if cont == 'n':
            break

if __name__ == "__main__":
    main()
