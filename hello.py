import math, random

# /c:/Users/Richa Deka/Coding/hello.py
# Simple Tic-Tac-Toe: 1-player (vs AI) or 2-player local

WIN_LINES = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

def show(board):
    def cell(i):
        return board[i] if board[i] else str(i+1)
    print()
    print(f" {cell(0)} | {cell(1)} | {cell(2)} ")
    print("---+---+---")
    print(f" {cell(3)} | {cell(4)} | {cell(5)} ")
    print("---+---+---")
    print(f" {cell(6)} | {cell(7)} | {cell(8)} ")
    print()

def winner(board):
    for a,b,c in WIN_LINES:
        if board[a] and board[a]==board[b]==board[c]:
            return board[a]
    if all(board): return 'Tie'
    return None

def valid_moves(board):
    return [i for i,v in enumerate(board) if not v]

def minimax(board, player, maximizing):
    w = winner(board)
    if w=='X': return (-1, None)
    if w=='O': return (1, None)
    if w=='Tie': return (0, None)
    best_score = -math.inf if maximizing else math.inf
    best_move = None
    for m in valid_moves(board):
        board[m] = player
        score, _ = minimax(board, 'O' if player=='X' else 'X', not maximizing)
        board[m] = None
        if maximizing:
            if score > best_score:
                best_score, best_move = score, m
        else:
            if score < best_score:
                best_score, best_move = score, m
    return best_score, best_move

def ai_move(board):
    # if first move, choose center or a corner
    if board.count(None) == 9:
        return random.choice([0,2,4,6,8])
    _, move = minimax(board, 'O', True)
    return move

def ask_move(board, player):
    while True:
        try:
            s = input(f"Player {player}, enter move (1-9): ").strip()
            i = int(s)-1
            if i in valid_moves(board):
                return i
            print("Invalid move, try again.")
        except Exception:
            print("Invalid input, enter number 1-9.")

def play():
    mode = ''
    while mode not in ('1','2'):
        mode = input("Choose mode: 1) vs AI  2) 2-player : ").strip()
    board = [None]*9
    current = 'X'
    show(board)
    while True:
        if mode=='1' and current=='O':
            m = ai_move(board)
            print(f"AI chooses {m+1}")
        else:
            m = ask_move(board, current)
        board[m] = current
        show(board)
        w = winner(board)
        if w:
            if w=='Tie':
                print("It's a tie.")
            else:
                print(f"{w} wins!")
            break
        current = 'O' if current=='X' else 'X'

if __name__ == "__main__":
    play()