from game import Game

if __name__ == '__main__':
     game = Game()
     game.create_players()
     game.initilize_game()
     game.pre_flop()
     game.flop()
     game.turn()
     game.river()
     game.next_hand()