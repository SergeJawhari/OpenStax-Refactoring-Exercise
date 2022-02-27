from audioop import add
import unittest
from refactoring_exercise import Game

class TestRefactoringExercise(unittest.TestCase):
    def test_correct_player_added(self):
        game = Game()
        game.add('Chet')
        self.assertEqual(game.players[game.current_player],'Chet')

    def test_validate_player_position(self):
        game = Game()
        in_right_position = False

        game.add('Chet')
        in_right_position = len(game.players) == 1
        game.add('Bob')
        in_right_position = len(game.players) == 2
        game.add('Phil')
        in_right_position = len(game.players) == 3

        self.assertEqual(in_right_position, True)

    def test_player_matches_roll(self):
        game = Game()

        game.add('Chet')
        print(game.roll)

        self.assertEqual(game.players[game.current_player],game.roll(6))

if __name__ == '__main__':
    unittest.main()