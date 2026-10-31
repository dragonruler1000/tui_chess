def is_empty(piece):
    return piece == "."

def piece_side(piece):
    return "upper" if piece.isupper() else "lower"

# Copied the two above functions so i could avoid circuler imports by asking needing to import them from main while main imports rules.py

def on_board(row, col): # This function checks to make sure that a move will end with the piece on the board still
    return 0 <= row < 8 and 0 <= col < 8

def pawn_moves(board, row, col): # This is the movement rules for the pawn. it includes the direction the pawn moves depending on what side it is,
    piece = board[row][col]      #  the ability to move 2 squares forward on its first move, and the diaginal attacks. Right now i dont have En Passant working.
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

def knight_moves(board, row, col):  # The movement for the night is pretty simple becasue it moves and attacks in a 'L' pattern so the only check that is needed is
    me = piece_side(board[row][col])# if it will end one the board and if the location it is moving to doesnt have a piece of its own side on it.
    moves = []
    for dr, dc in [(-2,-1),(-2,1),(-1,-2),(-1,2,),(1,-2),(1,2),(2,-1),(2,1)]:
        r, c = row + dr, col + dc
        if not on_board(r,c):
            continue
        target = board[r][c]
        if is_empty(target) or piece_side(target) != me:
            moves.append((r, c))
    return moves

def slide(board, row, col, directions): # This is used for the bishop, rook, and queen sense the all basicly move the same just in diffrent directions.
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

ROOK_DIRS = [(-1,0),(1,0),(0,-1),(0,1)] # These tables show the directions that the rook, and bishop can move and the queen just uses both of them.
BISHOP_DIRS = [(-1,-1),(-1,1),(1,-1),(1,1)]

def bishop_moves(board, row, col): return slide(board, row, col, BISHOP_DIRS)

def rook_moves(board, row, col): return slide(board, row, col, ROOK_DIRS)

def queen_moves(board, row, col): return slide(board, row, col, BISHOP_DIRS + ROOK_DIRS)

def king_moves(board, row, col): # The king has the same movement as the queen just it can only move 1 space at a time so this is basicly the slide function but without the loop
    me = piece_side(board[row][col])
    moves = []
    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]: # Can't just use the Rook and bishop dirs tables withoug refactoring the code.
        r, c = row + dr, col + dc
        if not on_board(r, c):
            continue
        target = board[r][c]
        if is_empty(target) or piece_side(target) != me:
            moves.append((r, c))
    return moves