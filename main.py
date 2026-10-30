from colorist import Color
from rules import pawn_moves, king_moves, bishop_moves, rook_moves, queen_moves, knight_moves # The module used to store the movement rules for the diffrent pieces

def starting_board(): # This is the starting layout of the board so if you want to make a custom setup edit this
    back_rank = ["r", "n", "b", "q", "k", "b", "n", "r"]
    return [
        back_rank[:], # Rank 8
        ["p"] * 8, # Rank 7
        *[["."] * 8 for _ in range(4)], # Ranks 6-3
        ["P"] * 8, # Rank 2
        [piece.upper() for piece in back_rank],
    ]
# This how the colors for the peices are set. RGB colors can be used if the terminal supports advanced ANSI color codes
WHITE = Color.YELLOW
BLACK = Color.BLUE
RESET = Color.DEFAULT

def fmt(piece): # This function sets all the peices to be upercase and sets the color for the pices
    if piece == ".":
        return piece
    color = WHITE if piece.isupper() else BLACK
    return f"{color}{piece.upper()}{RESET}"

def render_board(board, highlights=()): # This is where the board gets rendered. 
    files = "  " + "  ".join("abcdefgh")
    print(files)
    for r, row in enumerate(board):
        rank = 8 - r
        cells = []
        for c, p in enumerate(row):
            if (r, c) in highlights: # This part should make it so valid moves are highlighted but its not working right now :(
                # Capture squared get one marker, empty squares another
                cells.append("{Color.GREEN} x {Color.OFF}" if not is_empty(p) else "{Color.Cyan}*{Color.OFF}")
            else:
                cells.append(fmt(p))
        print(f"{rank} " + "  ".join(fmt(p) for p in row) + f" {rank}")
    print(files)

board = starting_board() # This grabs the table made by starting board and sets it to be the board



def get_piece(board, row, col): # this returns the charactor that is at the row and coloum given. Though i seem to not use it much because i just queury the table directly.
    return board[row][col]

def is_empty(piece): # I'm not entirly sure why this exsists as of right now
    return piece == "."

def piece_type(piece): # This returns the letter for the piece in upercase so the MOVE_RULES table only needs to have the upercase letters
    return piece.upper()

def piece_side(piece): # This returns what side the piece is on because the case of the letter encodes what color the piece belongs to
    return "upper" if piece.isupper() else "lower"

MOVE_RULES = { # This is used to make function calls easier so i didn't have to use a bunch of if/elif to call the move rules for each piece
    "P": pawn_moves,
    "N": knight_moves,
    "B": bishop_moves,
    "R": rook_moves,
    "Q": queen_moves,
    "K": king_moves
}

def square_to_index(square): # This is used to convert between standard notation (for example d4) used for user input and the location in the table (for example row 4, coloum 4)
    col = "abcdefgh".index(square[0])
    row = 8 - int(square[1])
    return row, col

def get_moves(board, row, col): # This function is used to find the type of piece at a location then call the movement rules for the piece using the MOVE_RULES table to use the right function
    piece = board[row][col]
    if is_empty(piece):
        return[]
    return MOVE_RULES[piece_type(piece)](board, row, col)

def is_valid_move(board, src, dst): # This function checks if a given move is a valid move or not.
    r1, c1 = square_to_index(src)
    r2, c2 = square_to_index(dst)
    return (r2, c2) in get_moves(board, r1, c1)

def parse_square(text): # This checks to see if a given location exists on the chess board or not
    text = text.strip().lower()
    if len(text) !=2 or text[0] not in "abcdefgh" or text[1] not in "12345678":
        return None
    return square_to_index(text)


def move(board, src, dst): # This function is what moves the pices on the board by setting the destination square to what the origin square was then sets the origin square to be empty
    r1, c1 = square_to_index(src)
    moves = get_moves(board, r1, c1)
    print(moves)
    r2, c2 = square_to_index(dst)
    board[r2][c2] = board[r1][c1]
    board[r1][c1] = "."

def index_to_square(row, col): # This converts from row and colum to standard notation. this is used to tell the player what the valid moves are in a human readable format.
    return "abcdefgh"[col] + str(8 - row)

def ask_move(board, current_side, turn): # This function asks for the players starting square checks to see if there is a piece there, if there is it checks to see if
    while True:                          # the piece has any valid moves. asks for your second move checks to see if it is in the list of valid moves then moves the piece if it is valid.
        text = input(f"\n{turn} to move. Pick a piece (e.g. e2): ")
        src = parse_square(text)

        if src is None:
            print("Thats not a square. Use a letter a-h and a number 1-8.")
            continue

        row, col = src
        piece = board[row][col]
        print(piece)

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
        render_board(board, highlights=set(moves)) # This should render the board with the valid moves highlighted.

        while True:
            text = input("Move to (or 'back' to pick another piece): ")
            if text.strip().lower() == "back":
                break
            dst = parse_square(text)
            if dst is None:
                print("That's not a square.")
            elif dst not in moves:
                print("That piece can't move there.")
            else:
                return src, dst

def apply_move(board, src, dst): # This is another function to move a peice. this is the one that is used sense this along with ask move do the same functions and more that move does
    (r1, c1), (r2,c2) = src, dst
    board[r2][c2] = board[r1][c1]
    board[r1][c1] = "."

side = "upper" # Side that moves first
turn = "Yellow" # This is the player that moves first

while True: # This is the main loop that renders the board asks for your moves applys them the changes whose turn it is and what side they are.
    render_board(board)
    src, dst = ask_move(board, side, turn)
    apply_move(board, src, dst)
    side = "upper" if side == "lower" else "lower"
    turn = "Yellow" if side == "upper" else "Blue"