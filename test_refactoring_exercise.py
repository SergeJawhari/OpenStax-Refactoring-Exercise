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

        printToString = io.StringIO()                  # Create StringIO object
        sys.stdout = printToString   

        game._ask_question()

        sys.stdout = sys.__stdout__ 

        self.assertEqual(printToString.getvalue(), 'Pop Question 1\n')
        
    def test_player_position_is_zero(self):
        game = Game()

        game.add('Chet')

        self.assertEqual(game.places[game.current_player], 0)

    def test_player_purse_is_zero(self):
        game = Game()

        game.add('Chet') 

        self.assertEqual(game.purses[game.current_player], 0)

    def test_player_not_in_penalty(self):
        game = Game()

        game.add('Chet') 

        self.assertFalse(game.in_penalty_box[game.current_player])

    def test_odd_roll_gets_out_of_penalty(self):
        game = Game()

        game.add('Chet')

        game.in_penalty_box[game.current_player] = True

        game.roll(5)

        self.assertTrue(game.is_getting_out_of_penalty_box) 













if __name__ == '__main__':
    unittest.main()