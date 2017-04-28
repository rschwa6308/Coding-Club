from random import choice
from copy import deepcopy


def random_ai(board):
    return choice(get_moves(board))


def get_jumps(board, open_, closed):
    new_open_ = deepcopy(open_)
    for move in open_:
        print move
        current_move_changed = False
        last = move[-1]
        for shift_y in (-2, 2):
            for shift_x in (-2, 2):
                new = deepcopy(move)
                new.append((last[0] + shift_x, last[1] + shift_y))
                if is_legal_move(board, new):
                    current_move_changed = True
                    new_open_.append(new)
        if not current_move_changed:
            new_open_.remove(move)
            closed.append(move)

    if len(new_open_) == 0:
        return closed
    else:
        return get_jumps(board, new_open_, closed)



def get_moves(board):
    moves = []
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] in (1, 10):
                # print x, y
                if is_legal_move(board, [(x, y), (x - 1, y + 1)]):
                    moves.append([(x, y), (x - 1, y + 1)])
                if is_legal_move(board, [(x, y), (x + 1, y + 1)]):
                    moves.append([(x, y), (x + 1, y + 1)])
    return moves


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




if __name__ == "__main__":
    board = [
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 2, 0, 2, 0, 2, 0],
        [0, 2, 0, 2, 0, 2, 0, 2],
        [2, 0, 2, 0, 2, 0, 2, 0]
    ]

    # print get_moves(board)

    print get_jumps(board, [[(1, 2)]], [])

    
