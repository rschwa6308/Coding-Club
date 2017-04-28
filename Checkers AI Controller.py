from itertools import combinations


board = [
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 1],
    [0, 0, 2, 0, 2, 0, 0, 0],
    [0, 10, 0, 0, 0, 0, 0, 0],
    [2, 0, 2, 0, 2, 0, 2, 0],
    [0, 2, 0, 2, 0, 0, 0, 2],
    [2, 0, 2, 0, 2, 0, 2, 0]
]



def is_legal_advance(board, (start, end)):
    if board[start[1]][start[0]] == 1:
        return abs(end[0] - start[0]) == 1 and end[1] - start[1] == 1
    else:
        return abs(end[0] - start[0]) == 1 and abs(end[1] - start[1]) == 1


def is_legal_jump(board, (start, end)):
    if board[(start[1] + end[1])/2][(start[0] + end[0])/2] in (2, 20):
        if board[start[1]][start[0]] == 1:
            return abs(end[0] - start[0]) == 2 and end[1] - start[1] == 2
        else:
            return abs(end[0] - start[0]) == 2 and abs(end[1] - start[1]) == 2
    else:
        return False



def is_legal_move(board, move):
    # If any square is off the board, return false
    if any(min(x, y) < 0 or max(x, y) > 7 for (x, y) in move):
        return False
    
    # If starting square is not an owned piece, return false
    if board[move[0][1]][move[0][0]] not in (1, 10):
        return False
    
    # If any intermediate square is occupied, return false
    if any(board[y][x] != 0 for (x, y) in move[1:]):
        return False

    # If move is a basic advance, check it
    if len(move) == 2 and abs(move[0][0] - move[1][0]) == 1:
        return is_legal_advance(board, move)

    # Check jump legality
    for start, end in [(move[i], move[i+1]) for i in range(len(move) - 1)]:
        if not is_legal_jump(board, [start, end]):
            return False

    return True



# [row[::-1] for row in board[::-1]]




class Ai:
    def __init__(self, name, func):
        self.name = name
        self.func = func
    def get_move(self, board):
        return self.func(board)




def apply_move(board, move):
    start_value = board[move[0][1]][move[0][0]]
    board[move[0][1]][move[0][0]] = 0
    if len(move) == 2 and abs(move[0][0] - move[1][0]) == 1:
        board[move[1][1]][move[1][0]] = start_value
    else:
        for i in range(len(move) - 1):
            start = move[i]
            end = move[i + 1]
            board[(start[1] + end[1]) / 2][(start[0] + end[0]) / 2] = 0
        board[move[-1][1]][move[-1][0]] = start_value



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
    print "\n".join([" ".join([(str(cell), ".")[cell == 0] for cell in row]) for row in board])



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
            move = ai.get_move(board)
            print "\n\nmove: " + str(move)
            if is_legal_move(board, move):
                apply_move(board, move)
            else:
                print "Illegal move made by " + ai.name
            display_board(board)
            board = flipped_board(board)












if __name__ == "__main__":

##    unit_tests = [
##        ([(1, 2), (3, 4), (5, 6)], True),
##        ([(1, 12), (2, 3)], False),
##        ([(1, 2), (2, -3)], False),
##        ([(1, 2), (2, 3), (3, 4)], False),
##        ([(1, 4), (3, 2)], True),
##        ([(1, 4), (3, 2), (5, 4)], True),
##    ]
##
##    for test in unit_tests:
##        result = is_legal_move(board, test[0])
##        print str(test[0]) + " --> " + str(result) + "\t" + ("PASS" if result == test[1] else "FAIL")

    from LiamCheckers import makeMove
    from TestAIs import *
    
    ais = [
        Ai("Liam 1", makeMove),
        Ai("Liam 2", makeMove)
    ]

    combs = combinations(ais, 2)

    for pair in combs:
        victor = run_game(pair[0], pair[1])
        print victor.name + " wins"
