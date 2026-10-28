def starting_board():
    back_rank = ["r", "n", "b", "q", "k", "b", "n", "r"]
    return [
        back_rank[:], # Rank 8
        ["p"] * 8, # Rank 7
        *[["."] * 8 for _ in range(4)], # Ranks 6-3
        ["P"] * 8, # Rank 2
        [piece.upper() for piece in back_rank],
    ]

def render_board(board):
    files = "  " + "  ".join("abcdefgh")
    print(files)
    for i, row in enumerate(board):
        rank = 8 - i
        print(f"{rank} " + "  ".join(row) + f" {rank}")
    print(files)

board = starting_board()
render_board(board)

def square_to_index(square):
    col = "abcdefgh".index(square[0])
    row = 8 - int(square[1])
    return row, col

def move(board, src, dst):
    r1, c1 = square_to_index(src)
    r2, c2 = square_to_index(dst)
    board[r2][c2] = board[r1][c1]
    board[r1][c1] = "."

while True:
    src = input("What piece are you moving: ")
    dst = input("where are you moving it: ")
    move(board, src, dst)
    render_board(board)