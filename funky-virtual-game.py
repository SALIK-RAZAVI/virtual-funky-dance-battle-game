import tkinter as tk
from PIL import Image, ImageTk
import time

class FunkyDanceBattle:
    def __init__(self, root):
        self.root = root
        self.root.title("Funky Dance Battle")
        self.root.geometry("800x600")

        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()

        self.create_dancers()
        self.start_dance()

    def create_dancers(self):
        self.dancer1 = self.canvas.create_rectangle(100, 300, 200, 400, fill="blue")
        self.dancer2 = self.canvas.create_rectangle(600, 300, 700, 400, fill="red")

    def start_dance(self):
        self.dance_moves = [(0, -10), (0, 10), (10, 0), (-10, 0)]
        self.animate_dancer(self.dancer1, 0)
        self.animate_dancer(self.dancer2, 1)

    def animate_dancer(self, dancer, index):
        move = self.dance_moves[index % len(self.dance_moves)]
        self.canvas.move(dancer, move[0], move[1])
        self.root.after(500, self.animate_dancer, dancer, index + 1)

if __name__ == "__main__":
    root = tk.Tk()
    app = FunkyDanceBattle(root)
    root.mainloop()
