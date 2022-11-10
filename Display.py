import tkinter as tk
import Sudoku as s
import time

def display():
    window = tk.Tk()
    window.title("Sudoku Solver")
    window.geometry("600x600")
    canvas = tk.Canvas(window, width = 600, height = 600)
    canvas.pack()
    active = True
    end = 10
    while active:      
        for k in range(len(s.answer)):
            window.update()
            canvas.delete("all")
            for i in range(75, 526, 50):
                if i == 75 or i == 225 or i == 375 or i == 525:
                    canvas.create_line(i, 525, i, 75, fill = "black", width = 4)
                    canvas.create_line(525, i, 75, i, fill = "black", width = 4)
                else:
                    canvas.create_line(i, 525, i, 75, fill = "black", width = 2)
                    canvas.create_line(525, i, 75, i, fill = "black", width = 2)
            for i in range(9):
                for j in range(9):
                    if s.answer[k][i][j] != 0:
                        canvas.create_text(100 + j * 50, 100 + i * 50, fill = "black", font = "Times 20", text = str(s.answer[k][i][j]))
            if k == len(s.answer) - 1:
                time.sleep(end)
            else:
                time.sleep(0.01)
        active = False

if __name__ == "__main__":
    grid = [[0, 9, 1, 2, 0, 0, 8, 3, 0],
            [0, 0, 0, 0, 0, 6, 0, 0, 0],
            [0, 2, 0, 0, 0, 9, 0, 4, 7],
            [0, 5, 0, 0, 0, 3, 0, 8, 0],
            [6, 0, 0, 4, 1, 0, 0, 0, 0],
            [1, 0, 0, 8, 0, 0, 0, 9, 5],
            [0, 6, 0, 9, 0, 0, 0, 2, 0],
            [0, 0, 2, 3, 0, 0, 0, 0, 4],
            [8, 3, 0, 0, 4, 0, 1, 6, 0]]
    s.solve(grid)
    display()