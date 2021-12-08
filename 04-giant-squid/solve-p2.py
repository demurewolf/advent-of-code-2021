#!/usr/bin/env python3.8

from utils import parse_data

#filename="test-input.txt"
filename="puzzle-input.txt"

drawings, boards = parse_data(filename)
winning_boards = []
stop = False
for d in drawings:
    print(f"Drawing #{d}")
    for i, b in enumerate(boards, start=1):
        if b not in winning_boards and b.mark_board(d):
            winning_boards.append(b)

            if len(winning_boards) == len(boards):
                stop = True

    if stop:
        break

print(f"Last winning board (LWB): {winning_boards[-1]}")
print(f"Score of LWB: {winning_boards[-1].calculate_score()}")
