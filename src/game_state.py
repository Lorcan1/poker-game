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
        self.dead_indexes = set()

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

    def initialize_blinds(self):
        self.small_blind.cash =- self.small_blind_value
        print(f"{self.small_blind.name} posts small blind: {self.small_blind_value}")
        self.big_blind.cash =- self.big_blind_value
        print(f"{self.big_blind.name} posts big blind: {self.big_blind_value}")
        self.pot += self.small_blind_value + self.big_blind_value

    def pre_flop(self):
        for player in self.players:
            player.cards.append(self.deck.deal_card())
            player.cards.append(self.deck.deal_card())

    def pre_flop_action(self):
        return self.process_betting_round(
            self.players, self.players.index(self.big_blind) + 1 , True
        )  # technically current_action - 1

    def process_betting_round(  # how to handle all in
        self, players: list, current_action_index: int, pre_flop = False
    ):  # what about bad input and  need to validate against players money

        players_in_hand = players.copy()

        stopping_index = current_action_index -1 
        if stopping_index < 0: 
            stopping_index = len(players) - 1 
            
        round_active = True
        while round_active:
            current_action_index = current_action_index % len(players)

            print(
                f"Current Index: {current_action_index} \n"
                f"Stopping Index: {stopping_index} \n"
                f"Dead Indexes: {self.dead_indexes} \n",
                f"Current Player: {players[current_action_index].name}",
            )

            if current_action_index in self.dead_indexes:
                if current_action_index == stopping_index:
                    break
                current_action_index += 1 
                continue
            
            if current_action_index == stopping_index:
                break

            player = players[current_action_index]

            print("-" * 40)
            print(f"{player.name}'s turn")
            print(
                f"{player.name} Your cards are {player.cards[0]} and {player.cards[1]}"
            )
            print(
                "Do you want to fold, call or raise? \n"
                f"Current call value: {self.current_call_amount} \n"
                f"Current pot: {self.pot}"
            )
            print("-" * 40)
            action = input(
                "1) Press f for fold. \n2) Press c for call. \n3) Press r for raise \n"
            )

            if action == "f":
                action_name = "folds"
                players_in_hand.remove(player)
                self.dead_indexes.add(current_action_index)
            elif action == "c":
                action_name = "calls"
                self.pot += self.current_call_amount
                player.cash -= self.current_call_amount
            else:
                action_name = "raises"
                self.raises(player)
                stopping_index = current_action_index - 1

            print(f"{player.name} {action_name}")

 

            if len(players_in_hand) == 1: 
                print(f"Hand is over. {players_in_hand[0].name} wins {self.pot}!")
                return False

            current_action_index += 1

            if pre_flop:
                stopping_index += 1
                if stopping_index > len(players) -1: 
                    stopping_index = 0 
                pre_flop = False

        self.players_in_hand = players_in_hand

        print(f"Number of players in hand: {len(players_in_hand)}")
        print(f"{'#':<4}{'Player Names:':<12}")
        print("-" * 16)
        for i, player in enumerate(players_in_hand, start=1):
            print(f"{i:<4}{player.name:<12}")

    def raises(self, player: Player):
        print(f"Current pot: {self.pot}. Your stack: {player.cash}")
        raise_amount = input(
            "How much do you want to raise? "
        )  # has to be higher than current bet
        # do some validation here
        raise_amount = int(raise_amount)
        self.pot += raise_amount
        player.cash -= raise_amount
        self.current_call_amount = raise_amount

    def flop(self):
        print("Here comes the flop!")
        self.cards.append(self.deck.deal_card())
        print(f"First up is the {self.cards[-1].rank} of {self.cards[-1].suit}! ")
        self.cards.append(self.deck.deal_card())
        print(f"Followed by the {self.cards[-1].rank} of {self.cards[-1].suit}! ")
        self.cards.append(self.deck.deal_card())
        print(f"Finally the {self.cards[-1].rank} of {self.cards[-1].suit}! ")

    def post_flop_action(
        self,
    ):  # Action starts with the first active player to the left of the button — which is normally the small blind
        # how to get the first player still in to the left of the button

        button_index = self.players.index(self.button) + 1 
        for i in range(button_index, button_index + len(self.players)):
            curr_index_to_check = i % len(self.players)
            if curr_index_to_check not in self.dead_indexes:
                post_flop_index = curr_index_to_check
                break
        self.dead_indexes = set()
        return self.process_betting_round(self.players_in_hand, post_flop_index)

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

    
    def reset_game_state(self):
        print("Game has ended, this needs to be implemented")
