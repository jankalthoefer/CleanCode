# !/usr/bin/python
# coding=utf-8

import UI

# extracted from printlines to have it interchangable
class Game:
    ui = None
    field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    current_player = 1

    # game state variables
    game_over = False
    tie = False

    moves = 0

    def __init__(self):
        self.ui = UI.UI()
        self.start_game()
    pass
    
    def start_game(self):
        while not self.game_over:
            
            if self.current_player == 1:
                self.ui.draw_players_turn(1)
                self.take_turn(1)
            else:
                self.ui.draw_players_turn(2)
                self.take_turn(2)
            if self.moves >= 8:
                self.set_tie();

            self.moves += 1
            self.ui.draw_line()
            self.ui.draw_field(self.field)

            self.check_win()

        self.handle_game_over()

    def handle_game_over(self):
        # handle game finish in seperate function
        if not self.tie:
            # when its player 1 turn, player 2 just won the game
            if self.current_player != 1:
                self.ui.draw_players_win(1)
            else:
                self.ui.draw_players_win(2)
        else: 
            self.ui.draw_tie()    

    def take_turn(self, playersChar):
        columnInput = self.ui.get_input_column()
        rowInput = self.ui.get_input_row()

        self.ui.draw_line
        self.make_move(columnInput, rowInput, playersChar)

    # sets position and switches player if successful
    def make_move(self, columnNumber, rowNumber, player_number):
        try:
            columnNumber = int(columnNumber)
            rowNumber = int(rowNumber)
        except ValueError:
            # it was a string, not an int.
            self.ui.draw_invalid_input
            pass  

        if ((columnNumber <= 3) or (columnNumber <= 1)) and ((rowNumber <= 3) or (rowNumber <= 1)):
            if self.field[rowNumber - 1][columnNumber - 1] is " ":
                # Valid Input Set Field and draw again
                self.field[rowNumber - 1][columnNumber - 1] = player_number
                
                self.switch_players()
            else:
                self.ui.draw_field_occupied()
        else:
            self.ui.draw_invalid_number()

    pass

    # change current player
    def switch_players(self):
        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1

    # checks each in every direction if a player as three in a row
    def check_win(self):
        for i in range(0, 3, 1):
            self.check_columns(i)
            self.check_rows(i)
        self.check_diagonalOne()
        self.check_diagonalTwo()

    # set game states
    def set_tie(self):
        self.tie = True

    def set_game_over(self):
        self.game_over = True

    # check all directions 
    def check_columns(self, column):
        for i in range(0, 3, 1):
            if self.field[i][column] is " ":
                return
        if self.field[0][column] is self.field[1][column] is self.field[2][column]:
            self.set_game_over()
            return

    def check_rows(self, row):
        for i in range(0, 3, 1):
            if self.field[row][i] is " ":
                return

        if self.field[row][0] is self.field[row][1] is self.field[row][2]:
            self.set_game_over()
            return

    def check_diagonalOne(self):
        # \ Diagonal
        for i in range(0, 3, 1):
            if self.field[i][i] is " ":
                return

        if self.field[0][0] is self.field[1][1] is self.field[2][2]:
            self.set_game_over()
            return

    def check_diagonalTwo(self):
        # / Diagonal
        if self.field[0][2] is " " or self.field[1][1] is " " or self.field[2][0] is " ":
            return
        if self.field[0][2] is self.field[1][1] is self.field[2][0]:
            self.set_game_over()
            return
#end Class