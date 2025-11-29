import tkinter as tk
from tkinter import messagebox
from functools import partial

class TicTacToe:
    def __init__(self, root):
        self.root = root
        root.title("Tic Tac Toe")
        root.resizable(False, False)
        self.current = "X"
        self.board = [""] * 9
        self.buttons = []
        self.scores = {"X": 0, "O": 0}
        self.create_widgets()
        self.new_game()

    def create_widgets(self):
        header = tk.Frame(self.root, pady=8)
        header.pack()
        self.status = tk.Label(header, text="X's turn", font=("Helvetica", 14))
        self.status.pack()

        board_frame = tk.Frame(self.root, padx=10, pady=10, bg="#ececec")
        board_frame.pack()

        btn_config = {"width": 6, "height": 3, "font": ("Helvetica", 24, "bold"),
                      "bd": 2, "relief": "raised", "bg": "white", "activebackground": "#dfefff"}

        for i in range(9):
            b = tk.Button(board_frame, text="", command=partial(self.on_click, i), **btn_config)
            row = i // 3
            col = i % 3
            b.grid(row=row, column=col, padx=5, pady=5)
            self.buttons.append(b)

        control = tk.Frame(self.root, pady=8)
        control.pack(fill="x")
        score_frame = tk.Frame(control)
        score_frame.pack(side="left", padx=10)
        self.score_label = tk.Label(score_frame, text=self.score_text(), font=("Helvetica", 11))
        self.score_label.pack()

        actions = tk.Frame(control)
        actions.pack(side="right", padx=10)
        tk.Button(actions, text="New Round", command=self.new_round).pack(side="left", padx=5)
        tk.Button(actions, text="Reset Scores", command=self.reset_scores).pack(side="left", padx=5)
        tk.Button(actions, text="Quit", command=self.root.quit).pack(side="left", padx=5)

    def score_text(self):
        return f"Scores — X: {self.scores['X']}   O: {self.scores['O']}"

    def on_click(self, index):
        if self.board[index] or self.is_game_over():
            return
        self.board[index] = self.current
        self.buttons[index].config(text=self.current, disabledforeground="#000000")
        self.buttons[index].config(state="disabled", bg="#ffffff")
        winner, line = self.check_winner()
        if winner:
            self.end_round(winner, line)
            return
        if all(self.board):
            self.end_round(None, None)  # tie
            return
        self.current = "O" if self.current == "X" else "X"
        self.status.config(text=f"{self.current}'s turn")

    def check_winner(self):
        wins = [
            (0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)
        ]
        for a,b,c in wins:
            if self.board[a] and self.board[a] == self.board[b] == self.board[c]:
                return self.board[a], (a,b,c)
        return None, None

    def end_round(self, winner, line):
        if winner:
            for i in line:
                self.buttons[i].config(bg="#90ee90")  # highlight
            self.scores[winner] += 1
            self.status.config(text=f"{winner} wins!")
            messagebox.showinfo("Game Over", f"{winner} wins!")
        else:
            self.status.config(text="It's a tie!")
            messagebox.showinfo("Game Over", "It's a tie!")
        for b in self.buttons:
            b.config(state="disabled")
        self.score_label.config(text=self.score_text())

    def is_game_over(self):
        winner, _ = self.check_winner()
        return winner is not None or all(self.board)

    def new_round(self):
        self.board = [""] * 9
        for b in self.buttons:
            b.config(text="", state="normal", bg="white")
        # alternate starting player
        self.current = "O" if self.current == "X" else "X"
        self.status.config(text=f"{self.current}'s turn")

    def new_game(self):
        # start fresh with X
        self.current = "X"
        self.scores = {"X": 0, "O": 0}
        self.new_round()
        self.score_label.config(text=self.score_text())

    def reset_scores(self):
        self.scores = {"X": 0, "O": 0}
        self.score_label.config(text=self.score_text())

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    # make board colourful: set each button a distinct color and add hover effect
    palette = ["#ffadad", "#ffd6a5", "#fdffb6",
               "#caffbf", "#9bf6ff", "#a0c4ff",
               "#bdb2ff", "#ffc6ff", "#ffc9de"]
    hover_palette = ["#ff8b8b", "#ffc07a", "#e8f07a",
                     "#8ee79a", "#66e0ff", "#6f9cff",
                     "#9b8bff", "#ff9ddb", "#ffb3c4"]

    for i, btn in enumerate(app.buttons):
        btn.config(bg=palette[i], activebackground=hover_palette[i], bd=3)
        btn.bind("<Enter>", lambda e, i=i: app.buttons[i].config(bg=hover_palette[i]) if app.buttons[i]['state'] == 'normal' else None)
        btn.bind("<Leave>", lambda e, i=i: app.buttons[i].config(bg=palette[i]) if app.buttons[i]['state'] == 'normal' else None)

    # replace the placeholder with this: add simple flower designs and ensure they reappear each round
    original_new_round = app.new_round

    def new_round_with_flowers():
        # call original logic to reset the board/buttons and alternate starter
        original_new_round()
        # apply small flower glyphs to empty (normal) buttons
        for i, b in enumerate(app.buttons):
            if b['state'] == 'normal' and not app.board[i]:
                b.config(text='✿', font=("Helvetica", 20), fg="#444444")
            else:
                # keep current X/O or disabled appearance
                pass

    app.new_round = new_round_with_flowers

    # rebind the "New Round" button in the UI to the patched method (search the widget tree)
    def rebind_new_round_button(widget):
        for child in widget.winfo_children():
            try:
                if isinstance(child, tk.Button) and child.cget("text") == "New Round":
                    child.config(command=app.new_round)
            except tk.TclError:
                pass
            rebind_new_round_button(child)

    rebind_new_round_button(app.root)

    # apply flowers for the initial display
    for i, b in enumerate(app.buttons):
        if b['state'] == 'normal' and not app.board[i]:
            b.config(text='✿', font=("Helvetica", 20), fg="#444444")

    # make boxes smaller and unify colour, remove per-button hover handlers
    single_color = "#a0c4ff"
    for b in app.buttons:
        b.unbind("<Enter>")
        b.unbind("<Leave>")
        b.config(width=4, height=2, font=("Helvetica", 14, "bold"),
                 bg=single_color, activebackground=single_color, bd=2,
                 fg="#000000", disabledforeground="#000000")
        if b['text'] == '✿':
            b.config(font=("Helvetica", 12), fg="#444444")

    # wrap the current new_round (which already adds flowers) so it reapplies unified styling each round
    original_new_round = app.new_round
    def new_round_smaller():
        original_new_round()
        for b in app.buttons:
            b.unbind("<Enter>")
            b.unbind("<Leave>")
            b.config(width=4, height=2, font=("Helvetica", 14, "bold"),
                     bg=single_color, activebackground=single_color, bd=2,
                     fg="#000000", disabledforeground="#000000")
            if b['text'] == '✿':
                b.config(font=("Helvetica", 12), fg="#444444")
    app.new_round = new_round_smaller

    # rebind New Round button in UI to our wrapper
    def rebind_new_round_button(widget):
        for child in widget.winfo_children():
            try:
                if isinstance(child, tk.Button) and child.cget("text") == "New Round":
                    child.config(command=app.new_round)
            except tk.TclError:
                pass
            rebind_new_round_button(child)
    rebind_new_round_button(app.root)

    root.mainloop()