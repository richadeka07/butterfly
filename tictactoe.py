import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic-Tac-Toe")
        master.resizable(False, False)

        self.current_player = "X"
        self.board = [[None]*3 for _ in range(3)]
        self.buttons = [[None]*3 for _ in range(3)]

        self.status_label = tk.Label(master, text=f"Player {self.current_player}'s turn", font=("Arial", 14))
        self.status_label.grid(row=0, column=0, columnspan=3, pady=(10, 0))

        for r in range(3):
            for c in range(3):
                btn = tk.Button(master, text="", width=8, height=4, font=("Arial", 24),
                                command=lambda rr=r, cc=c: self.on_click(rr, cc))
                btn.grid(row=r+1, column=c, padx=5, pady=5)
                self.buttons[r][c] = btn

        self.reset_button = tk.Button(master, text="Reset", command=self.reset, font=("Arial", 12))
        self.reset_button.grid(row=4, column=0, columnspan=3, pady=(5, 10))

    def on_click(self, row, col):
        if self.board[row][col] is not None:
            return
        self.board[row][col] = self.current_player
        self.buttons[row][col].configure(text=self.current_player, state="disabled")

        winner = self.check_winner()
        if winner:
            self.status_label.configure(text=f"Player {winner} wins!")
            self.end_game(f"Player {winner} wins!")
            return

        if self.is_draw():
            self.status_label.configure(text="Draw!")
            self.end_game("It's a draw!")
            return

        self.current_player = "O" if self.current_player == "X" else "X"
        self.status_label.configure(text=f"Player {self.current_player}'s turn")

    def check_winner(self):
        b = self.board
        # Rows and columns
        for i in range(3):
            if b[i][0] and b[i][0] == b[i][1] == b[i][2]:
                return b[i][0]
            if b[0][i] and b[0][i] == b[1][i] == b[2][i]:
                return b[0][i]
        # Diagonals
        if b[0][0] and b[0][0] == b[1][1] == b[2][2]:
            return b[0][0]
        if b[0][2] and b[0][2] == b[1][1] == b[2][0]:
            return b[0][2]
        return None

    def is_draw(self):
        return all(self.board[r][c] is not None for r in range(3) for c in range(3))

    def end_game(self, msg):
        # disable all buttons
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].configure(state="disabled")
        # optional popup
        messagebox.showinfo("Game Over", msg)

    def reset(self):
        self.current_player = "X"
        self.board = [[None]*3 for _ in range(3)]
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].configure(text="", state="normal")
        self.status_label.configure(text=f"Player {self.current_player}'s turn")


if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()
