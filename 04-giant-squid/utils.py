#!/usr/bin/env python3.8

if __name__ == "__main__":
    print("This is a utility file. Do not run.")
    exit(0)

# This will read a txt file as follows:

# The first line is comma separated list of numbers to draw for bingo game
# The rest of the file contains multiple 5 x 5 grids of numbers for the bingo boards in the bingo game

# This is going to return a list of numbers to draw and a list of boards to play against the drawn numbers.
def parse_data(in_file):
    drawings = []
    boards = []

    with open(in_file) as data_file:
        tmp_data = data_file.readline()
        drawings = [int(x) for x in tmp_data.rstrip().split(',')]

        tmp_data = data_file.readline()

        row_num = 0
        new_row = []

        while tmp_data != '':
            if tmp_data != '\n':

                # Data is messy, cleaning it up now
                new_row = tmp_data.rstrip().split(' ')
                if '' in new_row:
                    new_row_tmp = [n for n in new_row if n != '']
                    new_row = new_row_tmp

                new_row_tmp = [int(x) for x in new_row]
                new_row = new_row_tmp

                if row_num % 5 == 0:
                    # Somethings wrong with this part... the boards are only 4x5
                    # New board to make
                    new_board = BingoBoard(new_row)
                    boards.append(new_board)

                else:
                    # Add onto existing board
                    new_board.__add_row__(new_row)
                row_num += 1

            tmp_data = data_file.readline()

    return drawings, boards


class BingoBoard:
    def __init__(self, row):
        self.board = [[r for r in row]]
        self.marker_nums = []

    def __str__(self):
        return str(self.board)

    def __add_row__(self, new_row):
        curr_rows = len(self.board)

        if 5 > curr_rows > 0:
            if len(new_row) == len(self.board[0]):
                self.board.append(new_row)
        elif curr_rows == 0:
            self.board.append(new_row)

    def __check_win__(self):
        # Check rows
        check = False
        for row in self.board:
            check = True # Assume row might win
            for r in row:
                if r not in self.marker_nums:
                    check = False # A row must have all of the marker numbers to win, 

            if check:
                return True

        # Check cols
        for col_i in range(5):
            check = True
            for c in self.board:
                if c[col_i] not in self.marker_nums:
                    check = False

            if check:
                return True

        return False

    def calculate_score(self):
        if not self.__check_win__():
            return 0

        score = 0

        for row in self.board:
            for r in row:
                if r not in self.marker_nums:
                    score += r

        return score * self.marker_nums[-1]

    # Returns whether the boards wins upon marking
    def mark_board(self, mark_num):
        for row_list in self.board:
            if mark_num in row_list:
                self.marker_nums.append(mark_num)
                if self.__check_win__():
                    return True

        return False

    