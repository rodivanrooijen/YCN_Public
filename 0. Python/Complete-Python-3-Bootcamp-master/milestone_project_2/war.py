import random

values = {
    "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8,
    "Nine": 9, "Ten": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14
}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[self.rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
            for rank in values.keys():
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_one(self):
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def remove_card(self):
        return self.cards.pop(0)

    def add_cards(self, new_cards):
        if isinstance(new_cards, list):
            self.cards.extend(new_cards)
        else:
            self.cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.cards)} cards."


# Game setup
player1 = Player("One")
player2 = Player("Two")

deck = Deck()
deck.shuffle()

for _ in range(26):
    player1.add_cards(deck.deal_one())
    player2.add_cards(deck.deal_one())

# Game logic
game_on = True
round_num = 0

while game_on:
    round_num += 1
    print(f"Round {round_num}")

    if len(player1.cards) == 0:
        print("Player One, out of cards! Player Two wins!")
        game_on = False
        break

    if len(player2.cards) == 0:
        print("Player Two, out of cards! Player One wins!")
        game_on = False
        break

    # Start a new round
    player1_cards = [player1.remove_card()]
    player2_cards = [player2.remove_card()]
    at_war = True

    while at_war:
        if player1_cards[-1].value > player2_cards[-1].value:
            player1.add_cards(player1_cards)
            player1.add_cards(player2_cards)
            at_war = False
        elif player1_cards[-1].value < player2_cards[-1].value:
            player2.add_cards(player2_cards)
            player2.add_cards(player1_cards)
            at_war = False
        else:
            print("WAR!")

            if len(player1.cards) < 5:
                print("Player One unable to declare war")
                print("Player Two wins!")
                game_on = False
                break
            elif len(player2.cards) < 5:
                print("Player Two unable to declare war")
                print("Player One wins!")
                game_on = False
                break
            else:
                for _ in range(5):
                    player1_cards.append(player1.remove_card())
                    player2_cards.append(player2.remove_card())
