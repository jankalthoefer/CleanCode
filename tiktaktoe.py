# !/usr/bin/python
# coding=utf-8

# 
CROSS = "👩‍"
DOT = "😺"


class Game:
    field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    playerOne = True
    win = False
    tie = False
    moves = 0
    def __init__(self):
        print("Welcome to TikTakToe \n")

        self.draw_field()
        while not self.win and not self.tie:
            print("\n\n⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
            if self.playerOne == True:
                print("Player One Input")
                self.take_turn(CROSS)
            else:
                print("Player Two Input")
                self.take_turn(DOT)
            if self.moves >= 8:
                self.tie = True
            self.moves += 1
            self.check_win()

        if not self.tie:
            if not self.playerOne:
                print("!!! Player One Wins !!!")
            else:
                print("!!! Player Two Wins !!!")
        else:
            print("Its a tie")


    pass

    def draw_field(self):
        rowcount = 1
        print("     1       2     3")
        print("   ⎡-----⏉ -----⏉ ----⎤")
        for row in self.field:
            print " " + str(rowcount) + " │",
            print " " + row[0] + "      " + row[1] + "     " + row[2],
            print(" ⎟")
            rowcount += 1
            if rowcount < 4:
                print("   ├⎯⎯⎯⎯⎯┼⎯⎯⎯⎯⎯⎯┼⎯⎯⎯⎯⎯┤")
            else:
                print("   ⎣-----⏊ -----⏊ ----⎦")

    pass

    def set_Field(self, columnNumber, rowNumber, newChar):
        try:
            columnNumber = int(columnNumber)
            rowNumber = int(rowNumber)
        except ValueError:
            print("Invalid Input, Input should be numbers only")
            pass  # it was a string, not an int.

        if ((columnNumber <= 3) or (columnNumber <= 1)) and ((rowNumber <= 3) or (rowNumber <= 1)):
            if self.field[rowNumber - 1][columnNumber - 1] is " ":
                # Valid Input Set Field and draw again
                self.field[rowNumber - 1][columnNumber - 1] = newChar
                self.draw_field()
                # Change Players
                self.playerOne = not self.playerOne
            else:
                print("Field already occupied ")
        else:
            print("Invalid Numbers")

    pass

    def take_turn(self, playersChar):
        columnInput = input("Column>  ");
        rowInput = input("Row>  ");
        print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
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
            print("| Win")
            self.win = True
            return

    def check_rows(self, row):
        for i in range(0, 3, 1):
            if self.field[row][i] is " ":
                return

        if self.field[row][0] is self.field[row][1] is self.field[row][2]:
            print("- Win")
            self.win = True
            return

    def check_diagonalOne(self):
        # \ Diagonal
        for i in range(0, 3, 1):
            if self.field[i][i] is " ":
                return

        if self.field[0][0] is self.field[1][1] is self.field[2][2]:
            print("\ Win")
            self.win = True
            return

    def check_diagonalTwo(self):
        # / Diagonal
        if self.field[0][2] is " " or self.field[1][1] is " " or self.field[2][0] is " ":
            return
        if self.field[0][2] is self.field[1][1] is self.field[2][0]:
            print("/ Win")
            self.win = True
            return
#end Class

#main

game = Game()
