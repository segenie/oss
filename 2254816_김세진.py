import tkinter as tk

BOARD_SIZE = 15
CELL_SIZE = 40
STONE_SIZE = 16

class OmokGame:
    def __init__(self, root):
        self.root = root
        self.root.title("오목 게임")
        self.canvas = tk.Canvas(root, width=BOARD_SIZE * CELL_SIZE, height=BOARD_SIZE * CELL_SIZE, bg='burlywood')
        self.canvas.pack()

        self.board = [['.' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.turn = 0  # 0: 흑, 1: 백

        self.draw_board()
        self.canvas.bind("<Button-1>", self.handle_click)

    def draw_board(self):
        for i in range(BOARD_SIZE):
            self.canvas.create_line(CELL_SIZE//2, CELL_SIZE//2 + i*CELL_SIZE, CELL_SIZE//2 + (BOARD_SIZE-1)*CELL_SIZE, CELL_SIZE//2 + i*CELL_SIZE)
            self.canvas.create_line(CELL_SIZE//2 + i*CELL_SIZE, CELL_SIZE//2, CELL_SIZE//2 + i*CELL_SIZE, CELL_SIZE//2 + (BOARD_SIZE-1)*CELL_SIZE)

    def handle_click(self, event):
        x = round((event.x - CELL_SIZE//2) / CELL_SIZE)
        y = round((event.y - CELL_SIZE//2) / CELL_SIZE)

        if not (0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE):
            return
        if self.board[y][x] != '.':
            return

        stone = '●' if self.turn % 2 == 0 else '○'
        self.board[y][x] = stone
        self.draw_stone(x, y, stone)

        if self.check_win(x, y, stone):
            winner = "흑" if self.turn % 2 == 0 else "백"
            self.canvas.unbind("<Button-1>")
            self.canvas.create_text(BOARD_SIZE*CELL_SIZE//2, BOARD_SIZE*CELL_SIZE//2, text=f"{winner} 승리!", font=("Arial", 30), fill="red")
        else:
            self.turn += 1

    def draw_stone(self, x, y, stone):
        cx = CELL_SIZE//2 + x * CELL_SIZE
        cy = CELL_SIZE//2 + y * CELL_SIZE
        color = "black" if stone == '●' else "white"
        self.canvas.create_oval(cx - STONE_SIZE, cy - STONE_SIZE, cx + STONE_SIZE, cy + STONE_SIZE, fill=color, outline="black")

    def check_win(self, x, y, stone):
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dx, dy in directions:
            count = 1
            for dir in [1, -1]:
                nx, ny = x, y
                while True:
                    nx += dx * dir
                    ny += dy * dir
                    if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE and self.board[ny][nx] == stone:
                        count += 1
                    else:
                        break
            if count >= 5:
                return True
        return False

if __name__ == "__main__":
    root = tk.Tk()
    game = OmokGame(root)
    root.mainloop()
