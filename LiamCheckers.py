start = [[0,1,0,1,0,1,0,1],
         [1,0,1,0,1,0,1,0],
         [0,1,0,0,0,1,0,1],
         [0,0,0,0,0,0,0,0],
         [0,1,0,2,0,0,0,0],
         [2,0,0,0,2,0,2,0],
         [0,2,0,2,0,2,0,2],
         [2,0,2,0,2,0,2,0]]

# 1 is white (always you)
# 2 is black (always enemy)
# Multiply by 10 to get king

# Always going downwards if not king

hopX = -1
hopY = -1

def uncompressGrid(grid):
    fullGrid = [[0 for _ in range(8)] for _ in range(8)]
    for y, row in enumerate(grid):
        for x, item in enumerate(row):
            fullGrid[y][x*2+1-y%2] = item
    return fullGrid

def compressGrid(grid):
    newGrid = [[0 for _ in range(4)] for _ in range(8)]
    for y, row in enumerate(grid):
        for x, item in enumerate(row):
            if (x + y) % 2:
                newGrid[y][x//2] = item
    return newGrid

def assessSpace(y,x,grid,king):
    res = [y,x,0] # Store the value it will jump to
    if grid[y][x] == 2 or grid[y][x] == 20: # If the spot is already occupied
        legalMoves = getLegalMoves(y,x,grid,king,True) # Check for jumps
        global hopX, hopY
        if legalMoves[1] != hopX and not (legalMoves[0]-hopY)%2: # Cannot make a zig-zag jump
            # print(y,legalMoves[1],x)
            legalMoves[2] += 1 # Add 1 for capture
            return legalMoves # Default to leftmost jump
        else:
            res[2] = -100 # If no jumps, don't move here
    elif grid[y][x] == 1 or grid[y][x] == 10:
        res[2] = -100 # If friendly, don't move here
    else:
        # TODO: Better enemy avoidance
        if grid[y-1][x] == 2: res[2] -= 1
        if grid[y-1][x] == 20: res[2] -= 2
    return res

def getLegalMoves(y,x,grid,king=False,hop=False):
    # GOALS
    # ==================================================
    # Returns the number of pieces that will be captured
    # and the coordinates of the corresponding move
    # Count kings as two pieces
    # Subtract one if enemy is adjacent
    # Subtract two if enemy king is adjacent
    # Add three if king is gained
    # Return best of [[y,x,score]] representing fitness values
    moves = []
    if not hop:
        global hopX, hopY
        hopX, hopY = x, y
    if y < 7:
        moves.append(assessSpace(y+1,x,grid,king))# DOWN
    if king and y:
        moves.append(assessSpace(y-1,x,grid,king)) # UP
        
    if y % 2: # If row number is odd 
        if x: # If not on the far left
            if y < 7:
                moves.append(assessSpace(y+1,x-1,grid,king)) # DOWN-LEFT
            if king and y:
                moves.append(assessSpace(y-1,x-1,grid,king)) # UP-LEFT
            
    elif x < 3: # If row number is even and not on the far right
        if y < 7:
            moves.append(assessSpace(y+1,x+1,grid,king)) # DOWN-RIGHT
        if king and y:
            moves.append(assessSpace(y-1,x+1,grid,king)) # UP-RIGHT

    # print("The moves available in space ({0},{1}) are ".format(y,x),moves)
    if not moves:
        return [0,0,-100]
    bestScore = max(move[2] for move in moves)
    bestMove = moves[[move[2] for move in moves].index(bestScore)]
    return bestMove

def findOptimalMove(grid): # Find and return the best move of an entire grid
    moves = []
    for y, row in enumerate(grid):
        for x, item in enumerate(row):
            if item == 1 or item == 10:
                moves.append([y,x,getLegalMoves(y,x,grid,item==10)])
    #print(moves)
    bestScore = max(move[2][2] for move in moves)
    bestMove = moves[[move[2][2] for move in moves].index(bestScore)]
    return bestMove # This will look like (y0, x0, [y, x, score])
    
def makeMove(board):
    grid = compressGrid(board)
    # print('\n'.join(' '.join(list(str(x))) for x in grid))
    b = findOptimalMove(grid)
    b2 = [[b[0],b[1]*2+1-b[0]%2],[b[2][0],b[2][1]*2+1-b[2][0]%2]]
    best = [b2[0][::-1], b2[1][::-1]]
    # Translate to globally-used coordinate system
    return best
    
            
