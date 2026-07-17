from game_state import GameState
from player import Player
from game_loop import GameLoop

if __name__ == '__main__':
    #  game = Game()
    #  game.create_players()
    #  game.initilize_game()
    #  game.pre_flop()
    #  game.flop()
    #  game.turn()
    #  game.river()
    #  game.next_hand()
    # players = GameLoop.create_players()
    players = GameLoop.preset_players()
    game = GameState(players)
    game_loop = GameLoop(game)
    # game.initilize_game()
    # game.pre_flop()
    # game.flop()
    # game.turn()
    # game.river()
    # game.next_hand()
    game_loop.initialize_game()