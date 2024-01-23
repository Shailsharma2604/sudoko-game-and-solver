import tkinter as tk
from PIL import Image, ImageTk  # used for the image print to first page


class Window:

    def __init__(self, master):
        self.img = Image.open("main page.jpeg")  # image calling by the code
        self.img = self.img.resize((700, 700))

        self.img = ImageTk.PhotoImage(self.img)

        label = tk.Label(master, image=self.img)
        label.pack(expand=True, fill=tk.BOTH)

        # button code is down here in
        Button1 = tk.Button(root, text="Play Game", bg='yellow', font="bold",command=lambda: [root.destroy(), sudoku3x3()])
        Button1.pack(fill="x")
        Button2 = tk.Button(root, text="Solve Sudoku", font="bold", bg='yellow',command=lambda: [root.destroy(), solver()])
        Button2.pack(fill="x")

        # functions are called by this
        from solver import solver
        from sudoku3x3 import sudoku3x3


# window is created by this code
root = tk.Tk()
window = Window(root)
root.mainloop()

