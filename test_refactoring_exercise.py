from asyncio.windows_events import NULL
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

        printToString = io.StringIO() 
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

    def test_odd_roll_sets_get_out_variable_to_true(self):
        game = Game()

        game.add('Chet')

        game.in_penalty_box[game.current_player] = True

        game.roll(5)

        self.assertTrue(game.is_getting_out_of_penalty_box)

    def test_even_roll_sets_get_out_variable_to_False(self):
        game = Game()

        game.add('Chet')

        game.in_penalty_box[game.current_player] = True

        game.roll(4)

        self.assertFalse(game.is_getting_out_of_penalty_box)

    def test_player_position(self):
        game = Game()

        game.add('Chet')

        game.roll(5)
        game.roll(3)

        self.assertEqual(game.places[game.current_player], 8)

    def test_player_position_looping(self):
        game = Game()

        game.add('Chet')

        game.roll(6)
        game.roll(5)
        game.roll(4)

        self.assertEqual(game.places[game.current_player], 3)

    def test_position_zero_pop(self):
        game = Game()

        game.add('Chet')

        self.assertEqual(game._current_category, 'Pop')

    def test_position_four_pop(self):
        game = Game()

        game.add('Chet')

        game.roll(4)

        self.assertEqual(game._current_category, 'Pop')

    def test_position_eight_pop(self):
        game = Game()

        game.add('Chet')

        game.roll(4)
        game.roll(4)

        self.assertEqual(game._current_category, 'Pop')

    def test_position_one_science(self):
        game = Game()

        game.add('Chet')

        game.roll(1)

        self.assertEqual(game._current_category, 'Science')

    def test_position_five_science(self):
        game = Game()

        game.add('Chet')

        game.roll(1)
        game.roll(4)

        self.assertEqual(game._current_category, 'Science')

    def test_position_nine_science(self):
        game = Game()

        game.add('Chet')

        game.roll(1)
        game.roll(4)
        game.roll(4)

        self.assertEqual(game._current_category, 'Science')

    def test_position_two_sports(self):
        game = Game()

        game.add('Chet')

        game.roll(2)

        self.assertEqual(game._current_category, 'Sports')

    def test_position_six_sports(self):
        game = Game()

        game.add('Chet')

        game.roll(2)
        game.roll(4)

        self.assertEqual(game._current_category, 'Sports')

    def test_position_ten_sports(self):
        game = Game()

        game.add('Chet')

        game.roll(2)
        game.roll(4)
        game.roll(4)

        self.assertEqual(game._current_category, 'Sports')

    def test_position_three_rock(self):
        game = Game()

        game.add('Chet')

        game.roll(3)

        self.assertEqual(game._current_category, 'Rock')

    def test_position_seven_rock(self):
        game = Game()

        game.add('Chet')

        game.roll(3)
        game.roll(4)

        self.assertEqual(game._current_category, 'Rock')

    def test_position_eleven_rock(self):
        game = Game()

        game.add('Chet')

        game.roll(3)
        game.roll(4)
        game.roll(4)

        self.assertEqual(game._current_category, 'Rock')

    def test_right_question_asked_pop(self):
        game = Game()

        game.add('Chet')

        game.places[game.current_player] = 0

        printToString = io.StringIO() 
        sys.stdout = printToString   

        game._ask_question()

        sys.stdout = sys.__stdout__ 

        self.assertEqual(printToString.getvalue(), 'Pop Question 0\n')

    def test_right_question_asked_science(self):
        game = Game()

        game.add('Chet')

        game.places[game.current_player] = 1

        printToString = io.StringIO() 
        sys.stdout = printToString   

        game._ask_question()

        sys.stdout = sys.__stdout__ 

        self.assertEqual(printToString.getvalue(), 'Science Question 0\n')

    def test_right_question_asked_sports(self):
        game = Game()

        game.add('Chet')

        game.places[game.current_player] = 2

        printToString = io.StringIO() 
        sys.stdout = printToString   

        game._ask_question()

        sys.stdout = sys.__stdout__ 

        self.assertEqual(printToString.getvalue(), 'Sports Question 0\n')

    def test_right_question_asked_rock(self):
        game = Game()

        game.add('Chet')

        game.places[game.current_player] = 3

        printToString = io.StringIO() 
        sys.stdout = printToString   

        game._ask_question()

        sys.stdout = sys.__stdout__ 

        self.assertEqual(printToString.getvalue(), 'Rock Question 0\n')

    def test_question_gets_popped(self):
        game = Game()

        game.add('Chet')

        game.roll(4)

        self.assertEqual(len(game.pop_questions),49)

    def test_getting_out_of_penalty_correct_answer(self):
        game = Game()

        game.add('Chet')

        game.in_penalty_box[game.current_player] = True
        game.is_getting_out_of_penalty_box = True

        printToString = io.StringIO() 
        sys.stdout = printToString   

        game.was_correctly_answered()

        sys.stdout = sys.__stdout__ 

        self.assertEqual(printToString.getvalue(),'Answer was correct!!!!\nChet now has 1 Gold Coins.\n')

    def test_not_getting_out_of_penalty_correct_answer(self):
        game = Game()

        game.add('Chet')

        game.in_penalty_box[game.current_player] = True
        game.is_getting_out_of_penalty_box = False

        printToString = io.StringIO() 
        sys.stdout = printToString   

        game.was_correctly_answered()

        sys.stdout = sys.__stdout__ 

        self.assertEqual(printToString.getvalue(), '')

    def test_move_on_to_next_player(self):
        game = Game()

        game.add('Chet')
        game.add('Phil')
        game.add('Bob')
        game.add('Tom')

        game.was_correctly_answered()
        game.was_correctly_answered()
        game.was_correctly_answered()

        self.assertEqual(game.current_player, 3)

        














if __name__ == '__main__':
    unittest.main()