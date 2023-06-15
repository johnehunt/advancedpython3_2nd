import tkinter as tk

WIDTH = 600
HEIGHT = 400

BACKGROUND_COLOUR = 'white'

CIRCLE = 'Circle'
SQUARE = 'Square'
LINE = 'Line'

SIZE = 20


class PyDraw:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=WIDTH, height=HEIGHT, bg=BACKGROUND_COLOUR)
        self.canvas.pack()
        self.canvas.bind('<Button-1>', self.draw)
        self.mode = SQUARE
        # Set up menus
        self.menubar = tk.Menu(self.root)
        self.root.config(menu=self.menubar)
        self.create_file_menu()
        self.create_mode_menu()

    def create_mode_menu(self):
        mode_menu = tk.Menu(self.menubar, tearoff=0)
        mode_menu.add_command(label=CIRCLE, command=self.set_circle_mode)
        mode_menu.add_command(label=SQUARE, command=self.set_square_mode)
        mode_menu.add_command(label=LINE, command=self.set_line_mode)
        self.menubar.add_cascade(label='Mode', menu=mode_menu)

    def create_file_menu(self):
        file_menu = tk.Menu(self.menubar, tearoff=0)
        file_menu.add_command(label='New', command=self.new_canvas)
        file_menu.add_command(label='Exit', command=self.exit_app)
        self.menubar.add_cascade(label='File', menu=file_menu)

    def set_circle_mode(self):
        print(f'Set circle mode')
        self.mode = CIRCLE

    def set_square_mode(self):
        print(f'Set square mode')
        self.mode = SQUARE

    def set_line_mode(self):
        print(f'Draw line mode')
        self.mode = LINE

    def draw(self, event):
        x, y = event.x, event.y
        if self.mode == CIRCLE:
            self.canvas.create_oval(x, y, x + SIZE, y + SIZE, fill='red')
        elif self.mode == SQUARE:
            self.canvas.create_rectangle(x, y, x + SIZE, y + SIZE, fill= 'blue')
        elif self.mode == LINE:
            self.canvas.create_line(x, y, x + SIZE, y + SIZE)

    def new_canvas(self):
        self.canvas.delete('all')

    def exit_app(self):
        self.root.quit()


def main():
    app = PyDraw()
    app.root.mainloop()


if __name__ == '__main__':
    main()
