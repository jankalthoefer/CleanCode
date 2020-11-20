# !/usr/bin/python
# coding=utf-8

import UI

# extracted from printlines to have it interchangable
CROSS = "X"
DOT = "O"


class Game:
    ui = None
    field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    current_player = 1

    win = False
    tie = False
    
    moves = 0
    def __init__(self):
        self.ui = UI.UI()
        

        self.ui.draw_field(self.field)

        while not self.win and not self.tie:
            self.ui.draw_line()
            if self.current_player == 1:
                self.ui.draw_players_turn(1)
                self.take_turn(CROSS)
            else:
                self.ui.draw_players_turn(2)
                self.take_turn(DOT)
            if self.moves >= 8:
                self.tie = True
            self.moves += 1
            self.check_win()

        # handle game finish in seperate function
        if not self.tie:
            # when its player 1 turn, player 2 just won the game
            if self.current_player != 1:
                self.ui.draw_players_win(1)
            else:
                self.ui.draw_players_win(2)
        else: 
            self.ui.draw_tie()      
    pass
  

    def set_Field(self, columnNumber, rowNumber, newChar):
        # should be handled by ui
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
                self.field[rowNumber - 1][columnNumber - 1] = newChar
                self.ui.draw_field(self.field)
                
                
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

    def take_turn(self, playersChar):
        columnInput = self.ui.get_input_column()
        rowInput = self.ui.get_input_row()

        self.ui.draw_line
        self.set_Field(columnInput, rowInput, playersChar)


    def check_win(self):
        for i in range(0, 3, 1):
            self.check_columns(i)
            self.check_rows(i)
        self.check_diagonalOne()
        self.check_diagonalTwo()

    def check_columns(self, column):
        for i in range(0, 3, 1):
            if self.field[i][column] is " ":
                return

        if self.field[0][column] is self.field[1][column] is self.field[2][column]:
            #print("| Win")
            self.win = True
            return

    def check_rows(self, row):
        for i in range(0, 3, 1):
            if self.field[row][i] is " ":
                return

        if self.field[row][0] is self.field[row][1] is self.field[row][2]:
            #print("- Win")
            self.win = True
            return

    def check_diagonalOne(self):
        # \ Diagonal
        for i in range(0, 3, 1):
            if self.field[i][i] is " ":
                return

        if self.field[0][0] is self.field[1][1] is self.field[2][2]:
            #print("\ Win")
            self.win = True
            return

    def check_diagonalTwo(self):
        # / Diagonal
        if self.field[0][2] is " " or self.field[1][1] is " " or self.field[2][0] is " ":
            return
        if self.field[0][2] is self.field[1][1] is self.field[2][0]:
            #print("/ Win")
            self.win = True
            return
#end Class