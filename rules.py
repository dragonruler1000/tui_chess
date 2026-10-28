def is_empty(piece):
    return piece == "."

def piece_side(piece):
    return "upper" if piece.isupper() else "lower"

def on_board(row, col):
    return 0 <= row < 8 and 0 <= col < 8

def pawn_moves(board, row, col):
    piece = board[row][col]
    me = piece_side(piece)
    # Lowercase starts at the top (row 1) and moves down
    direction = 1 if me == "lower" else -1
    start_row = 1 if me == "lower" else 6
    moves = []

    # Forward one, and two from the starting row
    if on_board(row + direction, col) and is_empty(board[row + direction][col]):
        moves.append((row+direction, col))
        if row == start_row and is_empty(board[row + 2*direction][col]):
            moves.append((row + 2*direction, col))

    # captures
    for dc in (-1, 1):
        r, c = row + direction, col +dc
        if on_board(r, c) and not is_empty(board[r][c]) and piece_side(board[r][c]) != me:
            moves.append((r,c))
    return moves

def knight_moves(board, row, col):
    me = piece_side(board[row][col])
    moves = []
    for dr, dc in [(-2,-1),(-2,1),(-1,-2),(-1,2,),(1,-2),(1,2),(2,-1),(2,1)]:
        r, c = row + dr, col + dc
        if not on_board(r,c):
            continue
        target = board[r][c]
        if is_empty(target) or piece_side(target) != me:
            moves.append((r, c))
    return moves

def slide(board, row, col, directions):
    me = piece_side(board[row][col])
    moves = []
    for dr, dc in directions:
        r, c = row + dr, col +dc
        while on_board(r, c):
            target = board[r][c]
            if is_empty(target):
                moves.append((r, c))
            else:
                if piece_side(target) != me:
                    moves.append((r, c)) # capture, then stop
                break                    # blocked either way
            r, c = r+dr, c + dc
    return moves

ROOK_DIRS = [(-1,0),(1,0),(0,-1),(0,1)]
BISHOP_DIRS = [(-1,-1),(-1,1),(1,-1),(1,1)]

def bishop_moves(board, row, col): return slide(board, row, col, BISHOP_DIRS)

def rook_moves(board, row, col): return slide(board, row, col, ROOK_DIRS)

def queen_moves(board, row, col): return slide(board, row, col, BISHOP_DIRS + ROOK_DIRS)

def king_moves(board, row, col):
    me = piece_side(board[row][col])
    moves = []
    for dr, dc in [(0,-1),(0,1),(-1,0),(-1,0),(1,0),(1,0),(0,-1),(0,1)]:
        r, c = row + dr, col + dc
        if not on_board(r, c):
            continue
        target = board[r][c]
        if is_empty(target) or piece_side(target) != me:
            moves.append((r, c))
    return moves