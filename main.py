from colorist import Color
from rules import pawn_moves, king_moves, bishop_moves, rook_moves, queen_moves, knight_moves

def starting_board():
    back_rank = ["r", "n", "b", "q", "k", "b", "n", "r"]
    return [
        back_rank[:], # Rank 8
        ["p"] * 8, # Rank 7
        *[["."] * 8 for _ in range(4)], # Ranks 6-3
        ["P"] * 8, # Rank 2
        [piece.upper() for piece in back_rank],
    ]

WHITE = Color.YELLOW
BLACK = Color.BLUE
RESET = Color.DEFAULT

def fmt(piece):
    if piece == ".":
        return piece
    color = WHITE if piece.isupper() else BLACK
    return f"{color}{piece.upper()}{RESET}"

def render_board(board, highlights=()):
    files = "  " + "  ".join("abcdefgh")
    print(files)
    for r, row in enumerate(board):
        rank = 8 - r
        cells = []
        for c, p in enumerate(row):
            if (r, c) in highlights:
                # Capture squared get one marker, empty squares another
                cells.append("{Color.GREEN} x {Color.OFF}" if not is_empty(p) else "{Color.Cyan}*{Color.OFF}")
            else:
                cells.append(fmt(p))
        print(f"{rank} " + "  ".join(fmt(p) for p in row) + f" {rank}")
    print(files)

board = starting_board()



def get_piece(board, row, col):
    return board[row][col]

def is_empty(piece):
    return piece == "."

def piece_type(piece):
    return piece.upper()

def piece_side(piece):
    return "upper" if piece.isupper() else "lower"

MOVE_RULES = {
    "P": pawn_moves,
    "N": knight_moves,
    "B": bishop_moves,
    "R": rook_moves,
    "Q": queen_moves,
    "K": king_moves
}

def square_to_index(square):
    col = "abcdefgh".index(square[0])
    row = 8 - int(square[1])
    return row, col

def get_moves(board, row, col):
    piece = board[row][col]
    if is_empty(piece):
        return[]
    return MOVE_RULES[piece_type(piece)](board, row, col)

def is_valid_move(board, src, dst):
    r1, c1 = square_to_index(src)
    r2, c2 = square_to_index(dst)
    return (r2, c2) in get_moves(board, r1, c1)

def parse_square(text):
    text = text.strip().lower()
    if len(text) !=2 or text[0] not in "abcdefgh" or text[1] not in "12345678":
        return None
    return square_to_index(text)


def move(board, src, dst):
    r1, c1 = square_to_index(src)
    moves = get_moves(board, r1, c1)
    print(moves)
    r2, c2 = square_to_index(dst)
    board[r2][c2] = board[r1][c1]
    board[r1][c1] = "."

def index_to_square(row, col):
    return "abcdefgh"[col] + str(8 - row)

def ask_move(board, current_side, turn):
    while True:
        text = input(f"\n{turn} to move. Pick a piece (e.g. e2): ")
        src = parse_square(text)

        if src is None:
            print("Thats not a square. Use a letter a-h and a number 1-8.")
            continue

        row, col = src
        piece = board[row][col]

        if is_empty(piece):
            print("That square is empty.")
            continue
        if piece_side(piece) != current_side:
            print("That's not your piece.")
            continue

        moves = get_moves(board, row, col)
        if not moves:
            print("That piece has no valid moves.")
            continue

        print("Valid moves: " + ", ".join(index_to_square(r, c) for r, c in moves))
        render_board(board)

        while True:
            text = input("Move to (or 'back' to pick another piece or 'quit' to quit): ")
            if text.strip().lower() == "back":
                break
            dst = parse_square(text)
            if dst is None:
                print("That's not a square.")
            elif dst not in moves:
                print("That piece can't move there.")
            else:
                return src, dst

def apply_move(board, src, dst):
    (r1, c1), (r2,c2) = src, dst
    board[r2][c2] = board[r1][c1]
    board[r1][c1] = "."

side = "upper" # Side that moves first
turn = "Yellow"
quit = False

while True:
    render_board(board)
    src, dst = ask_move(board, side, turn)
    if quit == True:
        break
    else:
        apply_move(board, src, dst)
        side = "upper" if side == "lower" else "lower"
        turn = "Yellow" if side == "upper" else "Blue"