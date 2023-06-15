import tkinter as tk

WIDTH = 600
HEIGHT = 400

BACKGROUND_COLOUR = 'white'


class PyDraw:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(self.root, width=WIDTH, height=HEIGHT, bg=BACKGROUND_COLOUR)
        self.canvas.pack()
        self.canvas.bind('<B1-Motion>', self.draw)
        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label='New', command=self.new_canvas)
        file_menu.add_command(label='Exit', command=self.exit_app)
        menubar.add_cascade(label='File', menu=file_menu)

    def draw(self, event):
        x, y = event.x, event.y
        self.canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill='black')

    def new_canvas(self):
        self.canvas.delete('all')

    def exit_app(self):
        self.root.quit()


def main():
    root = tk.Tk()
    app = PyDraw(root)
    root.mainloop()


if __name__ == '__main__':
    main()
