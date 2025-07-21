# gui.py
import tkinter as tk

def on_click(r, c):
    print(f"Clicked {r},{c}")

root = tk.Tk()
buttons = [[tk.Button(root, text=" ", width=5, height=2, command=lambda r=i,c=j: on_click(r,c))
            for j in range(3)] for i in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j].grid(row=i, column=j)
root.mainloop()
