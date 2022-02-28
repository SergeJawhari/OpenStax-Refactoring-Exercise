
class Game:
    def __init__(self):
        # organized initializations to fit on one line based on their values.
        self.players, self.pop_questions, self.science_questions, self.sports_questions, self.rock_questions = ([] for i in range(5))
        self.places, self.purses, self.in_penalty_box = ([0] * 6 for i in range(3))
        self.current_player, self.is_getting_out_of_penalty_box = 0, False

        for i in range(50):
            self.pop_questions.append("Pop Question %s" % i)
            self.science_questions.append("Science Question %s" % i)
            self.sports_questions.append("Sports Question %s" % i)
            self.rock_questions.append("Rock Question %s" % i)

    def is_playable(self):
        return self.how_many_players >= 2

    def add(self, player_name):
        self.players.append(player_name)
        # organized initializations to fit on one line based on their values.
        self.places[self.how_many_players], self.purses[self.how_many_players], self.in_penalty_box[self.how_many_players] = 0, 0, False

        print(player_name + " was added")
        print("They are player number %s" % self.how_many_players)

        return True

    @property
    def how_many_players(self):
        return len(self.players)

    # This property will get the name of the current player so that the self.players[self.current_player] doesn't have to
    # get called every time.
    @property
    def player_name(self):
        return self.players[self.current_player]

    # This function will handle moving spaces to cover for the three lines. and displaying the text.
    def move_places(self, roll):
        self.places[self.current_player] += roll
        if self.places[self.current_player] > 11:
            self.places[self.current_player] -= 12
            print(self.player_name + \
                '\'s new location is ' + \
                str(self.places[self.current_player]))
            print("The category is %s" % self._current_category)
            
    def roll(self, roll):
        print("%s is the current player" % self.player_name)
        print("They have rolled a %s" % roll)

        if self.in_penalty_box[self.current_player] and roll % 2 != 0:
            self.is_getting_out_of_penalty_box = True

            print("%s is getting out of the penalty box" % self.player_name)
            self.move_places(roll) # Composed multiple lines of code into a function, it is cleaner and removes redundancy.
            self._ask_question()

        if self.in_penalty_box[self.current_player] and roll % 2 == 0:
            print("%s is not getting out of the penalty box" % self.player_name)
            self.is_getting_out_of_penalty_box = False

        else:
            self.move_places(roll)
            self._ask_question()

    def _ask_question(self):
        if self._current_category == 'Pop': print(self.pop_questions.pop(0))
        if self._current_category == 'Science': print(self.science_questions.pop(0))
        if self._current_category == 'Sports': print(self.sports_questions.pop(0))
        if self._current_category == 'Rock': print(self.rock_questions.pop(0))

    # Placed all categories into 3 if statements instead of 9.
    @property
    def _current_category(self):
        if self.places[self.current_player] == 0 or self.places[self.current_player] == 4 or self.places[self.current_player] == 8:
            return 'Pop'
        if self.places[self.current_player] == 1 or self.places[self.current_player] == 5 or self.places[self.current_player] == 9:
            return 'Science'
        if self.places[self.current_player] == 2 or self.places[self.current_player] == 6 or self.places[self.current_player] == 10:
            return 'Sports'
        else:
            return 'Rock'

    # Removed redundant code and put it into a function.
    def was_correctly_answered(self):
        if self.in_penalty_box[self.current_player] and self.is_getting_out_of_penalty_box:
            self.winner_text()
            winner = self._did_player_win()
            self.next_player()
            return winner

        if self.in_penalty_box[self.current_player] and not self.is_getting_out_of_penalty_box:
            self.next_player()
            return True

        else:
            self.winner_text()
            winner = self._did_player_win()
            self.next_player()
            return winner

    # Removed string texts and put it inside of a defined print function.
    def wrong_answer(self):
        self.loser_text()
        self.in_penalty_box[self.current_player] = True
        self.next_player()
        return True

    def _did_player_win(self):
        return not (self.purses[self.current_player] == 6)

    # This function will move on to the next player.
    def next_player(self):
        self.current_player += 1
        if self.current_player == self.how_many_players: self.current_player = 0

    # This function defines the loser text and displays it.
    def loser_text(self):
        print('Question was incorrectly answered')
        print(self.player_name + " was sent to the penalty box")

    # This function defines the loser text and displays it.
    def winner_text(self):
        print("Answer was correct!!!!")
        self.purses[self.current_player] += 1
        print(self.player_name + \
            ' now has ' + \
            str(self.purses[self.current_player]) + \
            ' Gold Coins.')

from random import randrange

if __name__ == '__main__':
    not_a_winner = False

    game = Game()

    game.add('Chet')
    game.add('Pat')
    game.add('Sue')

    while True:
        game.roll(randrange(5) + 1)

        if randrange(9) == 7:
            not_a_winner = game.wrong_answer()
        else:
            not_a_winner = game.was_correctly_answered()

        if not not_a_winner: break