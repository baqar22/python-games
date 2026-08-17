import tkinter as tk
from tkinter import messagebox
import random

HUMAN = "X"
AI = "O"
EMPTY = ""

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
    (0, 4, 8), (2, 4, 6)              # diags
]

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe (GUI) + Minimax")

        self.board = [EMPTY] * 9
        self.buttons = []
        self.game_over = False

        # Settings
        self.ai_starts_var = tk.BooleanVar(value=False)
        self.difficulty_var = tk.StringVar(value="Unbeatable (Minimax)")
        self.status_var = tk.StringVar(value="You are X. Your turn.")

        # ---------- Top UI ----------
        top = tk.Frame(root)
        top.pack(padx=12, pady=(10, 6), fill="x")

        tk.Label(top, textvariable=self.status_var, font=("Arial", 12)).pack(anchor="w")

        # Controls row
        controls = tk.Frame(root)
        controls.pack(padx=12, pady=6, fill="x")

        tk.Label(controls, text="Difficulty:", font=("Arial", 10)).grid(row=0, column=0, sticky="w")
        diff_menu = tk.OptionMenu(
            controls,
            self.difficulty_var,
            "Easy (Random)",
            "Medium (Mix)",
            "Hard (Minimax depth-limited)",
            "Unbeatable (Minimax)"
        )
        diff_menu.config(width=24)
        diff_menu.grid(row=0, column=1, sticky="w", padx=(6, 18))

        ai_start_cb = tk.Checkbutton(
            controls, text="AI starts first",
            variable=self.ai_starts_var,
            command=self.on_ai_start_toggle
        )
        ai_start_cb.grid(row=0, column=2, sticky="w")

        # ---------- Board ----------
        grid = tk.Frame(root)
        grid.pack(padx=12, pady=12)

        for i in range(9):
            btn = tk.Button(
                grid,
                text=" ",
                font=("Arial", 28, "bold"),
                width=3,
                height=1,
                command=lambda idx=i: self.on_click(idx),
            )
            btn.grid(row=i // 3, column=i % 3, padx=4, pady=4)
            self.buttons.append(btn)

        # ---------- Bottom UI ----------
        bottom = tk.Frame(root)
        bottom.pack(padx=12, pady=(0, 12), fill="x")

        tk.Button(bottom, text="New Game", command=self.reset).pack(side=tk.LEFT, padx=5)
        tk.Button(bottom, text="Quit", command=root.quit).pack(side=tk.LEFT, padx=5)

        # Start initial game
        self.reset()

    # -------------------- Helpers --------------------
    def set_status(self, text):
        self.status_var.set(text)

    def available_moves(self, b):
        return [i for i, cell in enumerate(b) if cell == EMPTY]

    def winner_and_line(self, b):
        for a, c, d in WIN_LINES:
            if b[a] != EMPTY and b[a] == b[c] == b[d]:
                return b[a], (a, c, d)
        return None, None

    def is_draw(self, b):
        w, _ = self.winner_and_line(b)
        return w is None and all(cell != EMPTY for cell in b)

    def next_player(self):
        x_count = sum(1 for c in self.board if c == HUMAN)
        o_count = sum(1 for c in self.board if c == AI)
        return HUMAN if x_count == o_count else AI  # X starts

    def disable_all(self):
        for btn in self.buttons:
            btn.config(state="disabled")

    def enable_empty(self):
        for i, btn in enumerate(self.buttons):
            btn.config(state=("normal" if self.board[i] == EMPTY else "disabled"))

    def clear_highlight(self):
        for btn in self.buttons:
            btn.config(relief="raised", bd=2)

    def highlight_line(self, line):
        # Highlight by making buttons look "sunken" with thicker border (no color needed)
        for idx in line:
            self.buttons[idx].config(relief="sunken", bd=5)

    # -------------------- Minimax --------------------
    def minimax(self, b, is_maximizing):
        w, _ = self.winner_and_line(b)
        if w == AI:
            return 1
        if w == HUMAN:
            return -1
        if self.is_draw(b):
            return 0

        if is_maximizing:
            best = -10
            for move in self.available_moves(b):
                b[move] = AI
                score = self.minimax(b, False)
                b[move] = EMPTY
                best = max(best, score)
            return best
        else:
            best = 10
            for move in self.available_moves(b):
                b[move] = HUMAN
                score = self.minimax(b, True)
                b[move] = EMPTY
                best = min(best, score)
            return best

    def minimax_depth_limited(self, b, depth, is_maximizing):
        w, _ = self.winner_and_line(b)
        if w == AI:
            return 10 - depth
        if w == HUMAN:
            return depth - 10
        if self.is_draw(b):
            return 0
        if depth <= 0:
            return 0  # neutral evaluation at cutoff (simple & fast)

        if is_maximizing:
            best = -999
            for move in self.available_moves(b):
                b[move] = AI
                score = self.minimax_depth_limited(b, depth - 1, False)
                b[move] = EMPTY
                best = max(best, score)
            return best
        else:
            best = 999
            for move in self.available_moves(b):
                b[move] = HUMAN
                score = self.minimax_depth_limited(b, depth - 1, True)
                b[move] = EMPTY
                best = min(best, score)
            return best

    def best_ai_move_unbeatable(self):
        best_score = -10
        best_move = None
        for move in self.available_moves(self.board):
            self.board[move] = AI
            score = self.minimax(self.board, False)
            self.board[move] = EMPTY
            if score > best_score:
                best_score = score
                best_move = move
        return best_move

    def best_ai_move_depth_limited(self, depth=3):
        best_score = -999
        best_move = None
        for move in self.available_moves(self.board):
            self.board[move] = AI
            score = self.minimax_depth_limited(self.board, depth - 1, False)
            self.board[move] = EMPTY
            if score > best_score:
                best_score = score
                best_move = move
        return best_move

    def ai_move_easy(self):
        moves = self.available_moves(self.board)
        return random.choice(moves) if moves else None

    def ai_move_medium(self):
        # Mix random + smart: sometimes random, sometimes depth-limited minimax
        if random.random() < 0.45:
            return self.ai_move_easy()
        return self.best_ai_move_depth_limited(depth=3)

    def ai_move_hard(self):
        return self.best_ai_move_depth_limited(depth=5)

    def choose_ai_move(self):
        mode = self.difficulty_var.get()
        if mode == "Easy (Random)":
            return self.ai_move_easy()
        if mode == "Medium (Mix)":
            return self.ai_move_medium()
        if mode == "Hard (Minimax depth-limited)":
            return self.ai_move_hard()
        return self.best_ai_move_unbeatable()

    # -------------------- Game Flow --------------------
    def on_click(self, idx):
        if self.game_over or self.board[idx] != EMPTY:
            return

        # Human plays
        self.make_move(idx, HUMAN)
        if self.check_end():
            return

        # AI plays
        self.set_status("AI thinking...")
        self.disable_all()
        self.root.after(120, self.ai_turn)

    def ai_turn(self):
        if self.game_over:
            return
        move = self.choose_ai_move()
        if move is not None:
            self.make_move(move, AI)
        ended = self.check_end()
        if not ended:
            self.set_status("Your turn.")
            self.enable_empty()

    def make_move(self, idx, player):
        self.board[idx] = player
        self.buttons[idx].config(text=player, state="disabled")

    def check_end(self):
        w, line = self.winner_and_line(self.board)
        if w is not None:
            self.game_over = True
            self.disable_all()
            self.highlight_line(line)
            self.set_status(f"{w} wins!")
            messagebox.showinfo("Game Over", f"{w} wins!")
            return True

        if self.is_draw(self.board):
            self.game_over = True
            self.disable_all()
            self.set_status("Draw!")
            messagebox.showinfo("Game Over", "It's a draw!")
            return True

        return False

    def on_ai_start_toggle(self):
        # Start a new game when toggled to avoid confusing mid-game changes
        self.reset()

    def reset(self):
        self.board = [EMPTY] * 9
        self.game_over = False
        self.clear_highlight()

        for btn in self.buttons:
            btn.config(text=" ", state="normal")

        # Decide who starts
        if self.ai_starts_var.get():
            self.set_status("AI starts. AI thinking...")
            self.disable_all()
            self.root.after(200, self.ai_first_move)
        else:
            self.set_status("You are X. Your turn.")
            self.enable_empty()

    def ai_first_move(self):
        if self.game_over:
            return
        move = self.choose_ai_move()
        if move is not None:
            self.make_move(move, AI)
        if not self.check_end():
            self.set_status("Your turn.")
            self.enable_empty()


if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()