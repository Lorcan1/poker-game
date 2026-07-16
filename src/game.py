from random import choice

from deck import Deck
from player import Player


class Game:
    def __init__(self):
        self.deck = Deck()
        self.players = []
        self.cards = []
        self.small_blind_value = 10
        self.big_blind_value = 20
        self.small_blind = None
        self.big_blind = None
        self.button = None

    def create_players(self):
        self.players.append(Player("player1"))
        self.players.append(Player("player2"))
        self.players.append(Player("player3"))
        self.players.append(Player("player4"))

    def initilize_game(self):
        n = len(self.players)
        self.button = choice(self.players)
        button_idx = self.players.index(self.button)
        self.small_blind = self.players[(button_idx + 1) % n]
        self.big_blind = self.players[(button_idx + 2) % n]

        print(f"{self.button.name} is on the button")
        print(f"The small blind is {self.small_blind.name}")
        print(f"The big blind is {self.big_blind.name}")
            

    def pre_flop(self):
        for player in self.players:
            player.cards.append(self.deck.deal_card())
            player.cards.append(self.deck.deal_card())

    def flop(self):
        print("Here comes the flop!")
        self.cards.append(self.deck.deal_card())
        print(f"First up is the {self.cards[-1].rank} of {self.cards[-1].suit}! ")
        self.cards.append(self.deck.deal_card())
        print(f"Followed by the {self.cards[-1].rank} of {self.cards[-1].suit}! ")
        self.cards.append(self.deck.deal_card())
        print(f"Finally the {self.cards[-1].rank} of {self.cards[-1].suit}! ")

    def turn(self):
        self.cards.append(self.deck.deal_card())
        print(f"And the turn is the {self.cards[-1].rank} of {self.cards[-1].suit}!")

    def river(self):
        self.cards.append(self.deck.deal_card())
        print(f"And the river is the {self.cards[-1].rank} of {self.cards[-1].suit}!")

    def bet(self):
        print("First betting round")

    def next_hand(self):
        self.deck = Deck()
        self.reset_players()
        self.rotate_button()

    def reset_players(self):
        for player in self.players:
            player.cards = []
            player.cards = []

    def rotate_button(self):
        n = len(self.players)
        button_idx = self.players.index(self.button)
        self.button = self.players[(button_idx + 1) % n]
        self.small_blind = self.players[(button_idx + 2) % n]
        self.big_blind = self.players[(button_idx + 3) % n]

        print(f"{self.button.name} is on the button")
        print(f"The small blind is {self.small_blind.name}")
        print(f"The big blind is {self.big_blind.name}")




