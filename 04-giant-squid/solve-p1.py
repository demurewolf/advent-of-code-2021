#!/usr/bin/env python3.8

from utils import parse_data

#filename="test-input.txt"
filename="puzzle-input.txt"

drawings, boards = parse_data(filename)

print(f"Numbers to draw: {drawings}")

already_won = False
for d in drawings:
    print(f"Drawing #{d}")
    for i, b in enumerate(boards, start=1):
        if b.mark_board(d) and not already_won:
            score = b.calculate_score()
            print(f"Winning board found: {i}")
            print(f"Score of winning board: {score}")
            already_won = True

    if already_won:
        exit(0)