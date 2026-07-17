from player import Player

class GameLoop():
    def __init__(self, game):
        self.game = game

    @staticmethod
    def create_players():
        players = []
        create = True
        while create: 
            print("Hello, welcome to Poker!")
            print("Create a player!")
            name = input("What's their name?: ")
            player = Player(name)
            players.append(player)
            print(f"Player {name} created succesfully!")
            cancel = input("Press 'n' key to stop creating players otherwise press any other key to continue")
            if cancel == 'n':
                create = False
                print(f"Number of players: {len(players)}")
                print("Player Names:")
                for player in players: 
                    print(f"{player.name}")
        return players
    
    @staticmethod
    def preset_players(): 
        player_name = ["Lorcan", "Arthur", "John", "Will", "Sally", "Sadie", "Bernadice"]
        players = [Player(name) for name in player_name]
        print(f"Number of players: {len(players)}")
        print(f"{'#':<4}{'Player Names:':<12}")
        print("-" * 16)
        for i, player in enumerate(players, start=1):
            print(f"{i:<4}{player.name:<12}")

        return players 
    

    def initialize_game(self): #need to act pre_flop if protag is the small or big blind
        self.game.initialize_game()
        self.game.handle_blinds()
        self.game.pre_flop()
        self.game.pre_flop_action()

        


    

    