import io # This module is used for catching output streams and converting them to a string. Reference: https://docs.python.org/3/library/io.html
import sys # This module is used for getting the output of the print() statements. Reference: https://docs.python.org/3/library/sys.html
import unittest # Unit testing framework used for building custom tests for methods. Reference: https://docs.python.org/3/library/unittest.html
from refactoring_exercise import Game # Importing the Game class from the main refactoring exercise python file.

# This class consists of all test scenarios for the Game class
class TestRefactoringExercise(unittest.TestCase):

    # Verify that the correct player was added to the roster.
    def test_correct_player_added(self):
        game = Game()
        game.add('Chet')
        self.assertEqual(game.players[game.current_player],'Chet')

    # Verify that player’s number corresponds to their position and when they were added.
    def test_validate_player_position(self):
        game = Game()
        in_right_position = False

        game.add('Chet')
        in_right_position1 = len(game.players) == 1
        game.add('Bob')
        in_right_position2 = len(game.players) == 2
        game.add('Phil')
        in_right_position3 = len(game.players) == 3

        if in_right_position1 and in_right_position2 and in_right_position3:
            in_right_position = True
        else:
            in_right_position = False

        self.assertTrue(in_right_position)

    # Verify that the how many players function will return the number of players in the game.
    def test_how_many_players(self):
        game = Game()

        game.add('Chet')
        game.add('Bob')
        game.add('Sal')

        self.assertEqual(game.how_many_players, 3)

    # Verify that the game can be played with 2 or more players. 
    def test_game_is_playable(self):
        game = Game()

        game.add('Chet')
        game.add('Bob')

        self.assertTrue(game.is_playable())

    # Verify that the game cannot be played with less than 2 players. 
    def test_game_is_not_playable(self):
        game = Game()

        game.add('Chet')

        self.assertFalse(game.is_playable())

    # Verify that the question will be incremented every time the category is called upon.
    def test_next_question_up(self):
        game = Game()

        game._current_category == 'Pop'

        game._ask_question()

        # Initialize a variable as a StringIO object that can be used to catch the output.
        printToString = io.StringIO() 
        # This will 'redirect' the stdout and make it equal to the printToString variable.
        sys.stdout = printToString   

        game._ask_question()

        # This will signal the end of the stdout segment and capture it.
        sys.stdout = sys.__stdout__ 

        # printToString.getValue() will get the string value of the stdout and compare it to the expected value.
        self.assertEqual(printToString.getvalue(), 'Pop Question 1\n')

    # Verify that the position (places) of a new player added is 0.    
    def test_player_position_is_zero(self):
        game = Game()

        game.add('Chet')

        self.assertEqual(game.places[game.current_player], 0)

    # Verify that the purse of a new player added is 0.
    def test_player_purse_is_zero(self):
        game = Game()

        game.add('Chet') 

        self.assertEqual(game.purses[game.current_player], 0)

    # Verify that a new player does not start inside of the penalty box.
    def test_player_not_in_penalty(self):
        game = Game()

        game.add('Chet') 

        self.assertFalse(game.in_penalty_box[game.current_player])

    # Verify that (in penalty box) rolling an odd number will set the penalty box variable to True.
    def test_odd_roll_sets_get_out_variable_to_true(self):
        game = Game()

        game.add('Chet')

        game.in_penalty_box[game.current_player] = True

        game.roll(5)

        self.assertTrue(game.is_getting_out_of_penalty_box)

    # Verify that (in penalty box) rolling an even number will set the penalty box variable to False.
    def test_even_roll_sets_get_out_variable_to_false(self):
        game = Game()

        game.add('Chet')

        game.in_penalty_box[game.current_player] = True

        game.roll(4)

        self.assertFalse(game.is_getting_out_of_penalty_box)

    # Verify that (in penalty box) a roll will be added to the current position of the player (+=)
    def test_player_position(self):
        game = Game()

        game.add('Chet')

        game.roll(5)
        game.roll(3)

        self.assertEqual(game.places[game.current_player], 8)

    # Verify that (in penalty box) rolling more than an 11 will result in the board resetting and 
    # starting from the beginning with the additional positional increases from the roll. i.e., 
    # being on 11 and rolling a 4 will result in a new position of 3.
    def test_player_position_looping(self):
        game = Game()

        game.add('Chet')

        game.roll(6)
        game.roll(5)
        game.roll(4)

        self.assertEqual(game.places[game.current_player], 3)

    # Verify that position 0 corresponds to the Pop category.
    def test_position_zero_pop(self):
        game = Game()

        game.add('Chet')

        self.assertEqual(game._current_category, 'Pop')

    # Verify that position 4 corresponds to the Pop category.
    def test_position_four_pop(self):
        game = Game()

        game.add('Chet')

        game.roll(4)

        self.assertEqual(game._current_category, 'Pop')

    # Verify that position 8 corresponds to the Pop category.
    def test_position_eight_pop(self):
        game = Game()

        game.add('Chet')

        game.roll(4)
        game.roll(4)

        self.assertEqual(game._current_category, 'Pop')
 
    # Verify that position 1 corresponds to the Science category.
    def test_position_one_science(self):
        game = Game()

        game.add('Chet')

        game.roll(1)

        self.assertEqual(game._current_category, 'Science')

    # Verify that position 5 corresponds to the Science category.
    def test_position_five_science(self):
        game = Game()

        game.add('Chet')

        game.roll(1)
        game.roll(4)

        self.assertEqual(game._current_category, 'Science')

    # Verify that position 9 corresponds to the Science category.
    def test_position_nine_science(self):
        game = Game()

        game.add('Chet')

        game.roll(1)
        game.roll(4)
        game.roll(4)

        self.assertEqual(game._current_category, 'Science')

    # Verify that position 2 corresponds to the Sports category.
    def test_position_two_sports(self):
        game = Game()

        game.add('Chet')

        game.roll(2)

        self.assertEqual(game._current_category, 'Sports')

    # Verify that position 6 corresponds to the Sports category.
    def test_position_six_sports(self):
        game = Game()

        game.add('Chet')

        game.roll(2)
        game.roll(4)

        self.assertEqual(game._current_category, 'Sports')

    # Verify that position 10 corresponds to the Sports category.
    def test_position_ten_sports(self):
        game = Game()

        game.add('Chet')

        game.roll(2)
        game.roll(4)
        game.roll(4)

        self.assertEqual(game._current_category, 'Sports')

    # Verify that position 3 corresponds to the Rock category.
    def test_position_three_rock(self):
        game = Game()

        game.add('Chet')

        game.roll(3)

        self.assertEqual(game._current_category, 'Rock')

    # Verify that position 7 corresponds to the Rock category.
    def test_position_seven_rock(self):
        game = Game()

        game.add('Chet')

        game.roll(3)
        game.roll(4)

        self.assertEqual(game._current_category, 'Rock')

    # Verify that position 11 corresponds to the Rock category.
    def test_position_eleven_rock(self):
        game = Game()

        game.add('Chet')

        game.roll(3)
        game.roll(4)
        game.roll(4)

        self.assertEqual(game._current_category, 'Rock')

    # Verify that the right question being asked for the Pop category.
    def test_right_question_asked_pop(self):
        game = Game()

        game.add('Chet')

        game.places[game.current_player] = 0

        printToString = io.StringIO() 
        sys.stdout = printToString   

        game._ask_question()

        sys.stdout = sys.__stdout__ 

        self.assertEqual(printToString.getvalue(), 'Pop Question 0\n')

    # Verify that the right question being asked for the Science category.
    def test_right_question_asked_science(self):
        game = Game()

        game.add('Chet')

        game.places[game.current_player] = 1

        printToString = io.StringIO() 
        sys.stdout = printToString   

        game._ask_question()

        sys.stdout = sys.__stdout__ 

        self.assertEqual(printToString.getvalue(), 'Science Question 0\n')

    # Verify that the right question being asked for the Sports category.
    def test_right_question_asked_sports(self):
        game = Game()

        game.add('Chet')

        game.places[game.current_player] = 2

        printToString = io.StringIO() 
        sys.stdout = printToString   

        game._ask_question()

        sys.stdout = sys.__stdout__ 

        self.assertEqual(printToString.getvalue(), 'Sports Question 0\n')

    # Verify that the right question being asked for the Rock category.
    def test_right_question_asked_rock(self):
        game = Game()

        game.add('Chet')

        game.places[game.current_player] = 3

        printToString = io.StringIO() 
        sys.stdout = printToString   

        game._ask_question()

        sys.stdout = sys.__stdout__ 

        self.assertEqual(printToString.getvalue(), 'Rock Question 0\n')

    # This test will test if pop questions are being iterated.
    def test_pop_questions_being_iterated(self):
        game = Game()

        game.add('Chet')

        game.places[game.current_player] = 0

        printToString = io.StringIO() 
        sys.stdout = printToString   

        game._ask_question()

        sys.stdout = sys.__stdout__ 

        verify_first = printToString.getvalue() == 'Pop Question 0\n'

        game.places[game.current_player] = 4

        printToString = io.StringIO() 
        sys.stdout = printToString   

        game._ask_question()

        sys.stdout = sys.__stdout__ 

        verify_first = printToString.getvalue() == 'Pop Question 1\n'

        self.assertTrue(verify_first)

        game.places[game.current_player] = 8

        printToString = io.StringIO() 
        sys.stdout = printToString   

        game._ask_question()

        sys.stdout = sys.__stdout__ 

        verify_first = printToString.getvalue() == 'Pop Question 2\n'

        self.assertTrue(verify_first)

    # This test will test if science questions are being iterated.
    def test_science_questions_being_iterated(self):
        game = Game()

        game.add('Chet')

        game.places[game.current_player] = 1

        printToString = io.StringIO() 
        sys.stdout = printToString   

        game._ask_question()

        sys.stdout = sys.__stdout__ 

        verify_first = printToString.getvalue() == 'Science Question 0\n'

        game.places[game.current_player] = 5

        printToString = io.StringIO() 
        sys.stdout = printToString   

        game._ask_question()

        sys.stdout = sys.__stdout__ 

        verify_first = printToString.getvalue() == 'Science Question 1\n'

        self.assertTrue(verify_first)

        game.places[game.current_player] = 9

        printToString = io.StringIO() 
        sys.stdout = printToString   

        game._ask_question()

        sys.stdout = sys.__stdout__ 

        verify_first = printToString.getvalue() == 'Science Question 2\n'

        self.assertTrue(verify_first)

    # This test will test if sports questions are being iterated.
    def test_sports_questions_being_iterated(self):
        game = Game()

        game.add('Chet')

        game.places[game.current_player] = 2

        printToString = io.StringIO() 
        sys.stdout = printToString   

        game._ask_question()

        sys.stdout = sys.__stdout__ 

        verify_first = printToString.getvalue() == 'Sports Question 0\n'

        game.places[game.current_player] = 6

        printToString = io.StringIO() 
        sys.stdout = printToString   

        game._ask_question()

        sys.stdout = sys.__stdout__ 

        verify_first = printToString.getvalue() == 'Sports Question 1\n'

        self.assertTrue(verify_first)

        game.places[game.current_player] = 10

        printToString = io.StringIO() 
        sys.stdout = printToString   

        game._ask_question()

        sys.stdout = sys.__stdout__ 

        verify_first = printToString.getvalue() == 'Sports Question 2\n'

        self.assertTrue(verify_first)

    # This test will test if rock questions are being iterated.
    def test_rock_questions_being_iterated(self):
        game = Game()

        game.add('Chet')

        game.places[game.current_player] = 3

        printToString = io.StringIO() 
        sys.stdout = printToString   

        game._ask_question()

        sys.stdout = sys.__stdout__ 

        verify_first = printToString.getvalue() == 'Rock Question 0\n'

        game.places[game.current_player] = 7

        printToString = io.StringIO() 
        sys.stdout = printToString   

        game._ask_question()

        sys.stdout = sys.__stdout__ 

        verify_first = printToString.getvalue() == 'Rock Question 1\n'

        self.assertTrue(verify_first)

        game.places[game.current_player] = 11

        printToString = io.StringIO() 
        sys.stdout = printToString   

        game._ask_question()

        sys.stdout = sys.__stdout__ 

        verify_first = printToString.getvalue() == 'Rock Question 2\n'

        self.assertTrue(verify_first)

    # Verify that once a question is asked, it is popped from the stack.
    def test_question_gets_popped_from_stack(self):
        game = Game()

        game.add('Chet')

        game.roll(4)

        self.assertEqual(len(game.pop_questions),49)

    # Verify that if the getting out of penalty variable is true, the answer will be correct and the player will be rewarded.
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

    # Verify that if the getting out of penalty variable is false, nothing will happen, the player will not be rewarded.
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

    # Verify that if the getting out of penalty variable is not true, it will move on to the next player.
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

    # Verify that if the answer is correct, the current players purse will be rewarded with one coin added to their purse.
    def test_correct_answer_reward(self):
        game = Game()

        game.add('Chet')

        game.was_correctly_answered()
        game.was_correctly_answered()

        self.assertEqual(game.purses[game.current_player], 2)
    
    # Verify that if the current player’s index is the same value as the length of the list, it will restart the cycle of 
    # players at the index of 0. 3 players will be indexed as [0,1,2]; therefore, if the current player’s index is 3, it 
    # does not exist and must restart from 0.
    def test_players_list_order_loops(self):
        game = Game()

        game.add('Chet')
        game.add('Phil')
        game.add('Bob')
        game.add('Tom')

        game.was_correctly_answered()
        game.was_correctly_answered()
        game.was_correctly_answered()
        game.was_correctly_answered()

        self.assertEqual(game.current_player, 0)

    # Verify that if a player has 6 coins in their purse, it will result in their victory.
    def test_if_six_coins_wins(self):
        game = Game()

        game.purses[game.current_player] = 6

        self.assertFalse(game._did_player_win())

    # Verify that if a player has less than 6 coins, they do not win.
    def test_if_less_than_six_coins_does_not_win(self):
        game = Game()

        game.purses[game.current_player] = 5

        self.assertTrue(game._did_player_win())

    # Verify that a wrong answer will send a player to the penalty box.
    def test_wrong_answer_penalty(self):
        game = Game()

        game.add('Chet')

        game.wrong_answer()

        self.assertTrue(game.in_penalty_box[game.current_player])

    # Verify that getting an answer wrong will move on to the next player.
    def test_wrong_answer_next_player(self):
        game = Game()

        game.add('Chet')
        game.add('Phil')
        game.add('Bob')

        game.wrong_answer()
        game.wrong_answer()

        self.assertEqual(game.current_player, 2)

# The main function that will run all of the tests.
if __name__ == '__main__':
    unittest.main()