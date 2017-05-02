from copy import deepcopy
from itertools import combinations

from CheckersFunctions import *



# [row[::-1] for row in board[::-1]]




class Ai:
    def __init__(self, name, func):
        self.name = name
        self.func = func
    def get_move(self, board):
        return self.func(board)



def flipped_board(board):
    # Rotate board
    new_board = [row[::-1] for row in board[::-1]]
    # switch 1's and 2's
    for y in range(len(new_board)):
        for x in range(len(new_board[y])):
            if new_board[y][x] == 1:
                new_board[y][x] = 2
            elif new_board[y][x] == 10:
                new_board[y][x] = 20
            elif new_board[y][x] == 2:
                new_board[y][x] = 1
            elif new_board[y][x] == 20:
                new_board[y][x] = 10
    return new_board


def display_board(board):
    legend = {0: ".", 1: "x", 10: "X", 2: "o", 20: "O"}
    print "\n".join([" ".join([legend[cell] for cell in row]) for row in board])



def run_game(ai_a, ai_b):
    board = [
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 2, 0, 2, 0, 2, 0],
        [0, 2, 0, 2, 0, 2, 0, 2],
        [2, 0, 2, 0, 2, 0, 2, 0]
    ]

    display_board(board)
    for i in range(100):
        for ai in (ai_a, ai_b):
            print "\n\n"

            if not has_moves(board):
                print "Stalemate!"
                return None
            
            move = ai.get_move(board)
            # print "\n\nmove: " + str(move)
            if is_legal_move(board, move):
                apply_move(board, move)
            else:
                print "Illegal move made by " + ai.name

            if is_game_won(board):
                return ai
                
            if ai is ai_a:
                display_board(board)
            else:
                display_board(flipped_board(board))
            board = flipped_board(board)









if __name__ == "__main__":


    from LiamCheckers import makeMove
    from TestAIs import *
    
    ais = [
        Ai("Russell 1", random_ai),
        Ai("Russell 2", random_ai)
    ]

    combs = combinations(ais, 2)

    for pair in combs:
        victor = run_game(pair[0], pair[1])
        if victor is not None:
            print victor.name + " wins!"
        else:
            print "Tie!"

