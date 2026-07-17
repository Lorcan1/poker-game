from random import choice

from deck import Deck
from player import Player


class GameState:
    def __init__(self, players: list):
        self.deck = Deck()
        self.players = []
        self.cards = []
        self.small_blind_value = 10
        self.big_blind_value = 20
        self.small_blind = None
        self.big_blind = None
        self.button = None
        self.players = players
        self.protag = players[0]
        self.protag_big_blind = False
        self.protag_small_blind = False
        self.pot = 0
        self.players_in_hand = self.players.copy()
        self.current_call_amount = self.big_blind_value



    def initialize_game(self):
        n = len(self.players)
        self.button = choice(self.players)
        button_idx = self.players.index(self.button)
        self.small_blind = self.players[(button_idx + 1) % n]
        self.big_blind = self.players[(button_idx + 2) % n]
        print("-" * 40)
        print(f"On the button is: {self.button.name}")
        print(f"The small blind is: {self.small_blind.name}")
        print(f"The big blind is: {self.big_blind.name}")
        print("-" * 40)

    
    def check_protag_blind(self):
        if self.big_blind_name == self.protag.name:
            self.protag_big_blind = True
        else:
            self.protag_big_blind = False

    def handle_blinds(self):
        self.small_blind.cash - self.small_blind_value
        print(f"{self.small_blind.name} posts small blind: {self.small_blind_value}")
        self.big_blind.cash - self.big_blind_value
        print(f"{self.big_blind.name} posts big blind: {self.big_blind_value}")
        self.pot += self.small_blind_value + self.big_blind_value


            

    def pre_flop(self):
        for player in self.players:
            player.cards.append(self.deck.deal_card())
            player.cards.append(self.deck.deal_card())

    def pre_flop_action(self): #what about bad inputs, need to check players money
        print(len(self.players))
        for player in self.players:
            print(f"{player.name} whats going on")
            if player.name == self.big_blind.name or player.name == self.small_blind.name:
                print()
                continue
            print("-" * 40)
            print(f"{player.name}'s turn")
            print(f"{player.name} Your cards are {player.cards[0]} and {player.cards[1]}")
            print("Do you want to fold, call or raise? \n" \
            f"Current call value: {self.current_call_amount} \n" \
            f"Current pot: {self.pot}")
            print("-" * 40)
            action = input("1) Press f for fold. \n" \
                          "2) Press c for call. \n"  \
                          "3) Press r for raise \n")

            if action == "f":
                action_name = "folds"
                self.players_in_hand.remove(player)
            elif action == "c":
                action_name = "calls"
                self.pot += self.current_call_amount
                player.cash -= self.current_call_amount 
            else:
                action_name = "raises"
                #get the amount to raise 
                
            print(f"{player.name} {action_name}")
        
        print(f"Number of players in hand: {len(self.players_in_hand)}")
        print(f"{'#':<4}{'Player Names:':<12}")
        print("-" * 16)
        for i, player in enumerate(self.players_in_hand, start=1):
            print(f"{i:<4}{player.name:<12}")

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




