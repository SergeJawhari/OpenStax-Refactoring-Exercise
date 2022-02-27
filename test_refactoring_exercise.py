import io
import sys
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

        self.assertTrue(in_right_position)

    def test_how_many_players(self):
        game = Game()

        game.add('Chet')
        game.add('Bob')
        game.add('Sal')

        self.assertEqual(game.how_many_players, 3)

    def test_game_is_playable(self):
        game = Game()

        game.add('Chet')
        game.add('Bob')

        self.assertTrue(game.is_playable())

    def test_game_is_not_playable(self):
        game = Game()

        game.add('Chet')

        self.assertFalse(game.is_playable())

    def test_next_question_up(self):
        game = Game()

        game._current_category == 'Pop'

        game._ask_question()

        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput   

        game._ask_question()

        sys.stdout = sys.__stdout__ 

        self.assertEqual(capturedOutput.getvalue(), 'Pop Question 1\n')
        


if __name__ == '__main__':
    unittest.main()