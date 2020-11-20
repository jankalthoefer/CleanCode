# !/usr/bin/python
# coding=utf-8

class UI:
    def __init__(self):
        self.draw_opener()


    def draw_opener(self):
        print("Welcome to TikTakToe \n")

    # user input
    def get_input_column(self):
        return input("Column>  ")

    def get_input_row(self):
        return input("Row>  ")

    # game field output
    def draw_field(self, field):
        rowcount = 1
        print("     1       2     3")
        print("   ⎡-----⏉ -----⏉ ----⎤")
        for row in field:
            print " " + str(rowcount) + " │",
            print " " + row[0] + "      " + row[1] + "     " + row[2],
            print(" ⎟")
            rowcount += 1
            if rowcount < 4:
                print("   ├⎯⎯⎯⎯⎯┼⎯⎯⎯⎯⎯⎯┼⎯⎯⎯⎯⎯┤")
            else:
                print("   ⎣-----⏊ -----⏊ ----⎦")

    pass

    # player related outputs
    def draw_players_turn(self, player_number):
        if player_number == 1:
            print("Player One Input")
        elif player_number == 2:
            print("Player Two Input")   

    def draw_players_win(self, player_number):
        if player_number == 1:
            print("!!! Player One Wins !!!")
        elif player_number == 2:
            print("!!! Player Two Wins !!!")
    

    # will be used in a later commit
    # def __draw_player_text(self, text, player_number):


    # Static messages   
    def draw_line(self):
        print("\n\n⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")

    def draw_tie(self):
        print("Its a tie")

    def draw_invalid_input(self):
        print("Invalid Input, Input should be numbers only")

    def draw_invalid_number(self):
        print("Invalid Numbers")

    def draw_field_occupied(self):
        print("Field already occupied ")
