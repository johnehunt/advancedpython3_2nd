import tkinter as tk
from abc import abstractmethod


class PyDrawConstants:
    WIDTH = 600
    HEIGHT = 400

    BACKGROUND_COLOUR = 'white'

    CIRCLE_MODE = 'Circle'
    SQUARE_MODE = 'Square'
    LINE_MODE = 'Line'
    TEXT_MODE = 'Text'

    SIZE = 30

class Figure:
    def __init__(self, canvas, x=0, y=0, size=None, fill='blue'):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.size = size
        self.fill = fill

    @abstractmethod
    def draw(self):
        pass

class Square(Figure):
    def __init__(self, canvas, x, y, size):
        super().__init__(canvas=canvas, x=x, y=y, size=size)

    def draw(self):
        self.canvas.create_rectangle(self.x,
                                     self.y,
                                     self.x + self.size,
                                     self.y + self.size,
                                     fill=self.fill)

class Circle(Figure):
    def __init__(self, canvas, x, y, size):
        super().__init__(canvas=canvas, x=x, y=y, size=size, fill='red')

    def draw(self):
        self.canvas.create_oval(self.x,
                                     self.y,
                                     self.x + self.size,
                                     self.y + self.size,
                                     fill=self.fill)

class Line(Figure):
    def __init__(self, canvas, x, y, size):
        super().__init__(canvas=canvas, x=x, y=y, size=size)

    def draw(self):
        self.canvas.create_line(self.x,
                                self.y,
                                self.x + self.size,
                                self.y + self.size)

class Text(Figure):
    def __init__(self, canvas, x, y, text_string='Text', font='Helvetica 15 bold', fill='black'):
        super().__init__(canvas=canvas, x=x, y=y, fill=fill)
        self.text_string = text_string
        self.font = font

    def draw(self):
        text = self.text_string
        self.canvas.create_text(self.x,
                                self.y,
                                text=text,
                                fill=self.fill,
                                font=self.font)


class DrawingModel:

    def __init__(self):
        self.contents = []

    def clear_figures(self):
        self.contents = []

    def add_figure(self, figure):
        self.contents.append(figure)

class DrawingController:

    def __init__(self, view, model, get_mode):
        self.view = view
        self.model = model
        self.get_mode = get_mode

    def on_mouse_click(self, mouse_event):
        x = mouse_event.x
        y = mouse_event.y
        self.add(self.get_mode(), x, y)

    def add(self, mode, x, y, size=PyDrawConstants.SIZE):
        if mode == PyDrawConstants.SQUARE_MODE:
            fig = Square(self.view, x, y, size)
        elif mode == PyDrawConstants.CIRCLE_MODE:
            fig = Circle(self.view, x, y, size)
        elif mode == PyDrawConstants.TEXT_MODE:
            fig = Text(self.view, x, y)
        else:
            fig = Line(self.view, x, y, size)
        self.model.add_figure(fig)
        self.view.draw_contents()

    def clear(self):
        self.model.clear_figures()
        self.view.delete('all')

class DrawingView(tk.Canvas):
    def __init__(self, parent, get_mode,
                 width=PyDrawConstants.WIDTH,
                 height=PyDrawConstants.HEIGHT,
                 bg=PyDrawConstants.BACKGROUND_COLOUR):
        super().__init__(parent, width=width, height=height, bg=bg)
        self.model = DrawingModel()
        self.controller = DrawingController(self, self.model, get_mode)
        self.pack()
        self.bind('<Button-1>', self.controller.on_mouse_click)

    def draw_contents(self):
        for figure in self.model.contents:
            figure.draw()

class PyDrawController:

    def __init__(self, root):
        self.root = root
        self.view = None
        # Set the initial mode
        self.mode = PyDrawConstants.SQUARE_MODE

    def set_circle_mode(self):
        self.mode = PyDrawConstants.CIRCLE_MODE

    def set_line_mode(self):
        self.mode = PyDrawConstants.LINE_MODE

    def set_square_mode(self):
        self.mode = PyDrawConstants.SQUARE_MODE

    def set_text_mode(self):
        self.mode = PyDrawConstants.TEXT_MODE

    def clear_drawing(self):
        self.view.drawing_controller.clear()

    def get_mode(self):
        return self.mode

    def new_canvas(self):
        self.view.delete('all')

    def exit_app(self):
        self.root.quit()

class PyDrawMenuBar(tk.Menu):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller=controller
        self.create_file_menu()
        self.create_mode_menu()

    def create_mode_menu(self):
        mode_menu = tk.Menu(self, tearoff=0)
        mode_menu.add_command(label=PyDrawConstants.CIRCLE_MODE, command=self.controller.set_circle_mode)
        mode_menu.add_command(label=PyDrawConstants.SQUARE_MODE, command=self.controller.set_square_mode)
        mode_menu.add_command(label=PyDrawConstants.LINE_MODE, command=self.controller.set_line_mode)
        mode_menu.add_command(label=PyDrawConstants.TEXT_MODE, command=self.controller.set_text_mode)
        self.add_cascade(label='Mode', menu=mode_menu)


    def create_file_menu(self):
        file_menu = tk.Menu(self, tearoff=0)
        file_menu.add_command(label='New', command=self.controller.new_canvas)
        file_menu.add_command(label='Exit', command=self.controller.exit_app)
        self.add_cascade(label='File', menu=file_menu)



class PyDraw:
    def __init__(self):
        self.root = tk.Tk()

        # Set the title of the window
        self.root.title('PyDraw')

        # Set up the controller
        self.controller = PyDrawController(self.root)

        # Set up menus
        self.menubar = PyDrawMenuBar(self.root, self.controller)
        self.root.config(menu=self.menubar)

        # Setup drawing panel
        self.drawing_panel = DrawingView(self.root, self.controller.get_mode)
        self.controller.view = self.drawing_panel

        self.root.eval('tk::PlaceWindow . center')


def main():
    app = PyDraw()
    app.root.mainloop()


if __name__ == '__main__':
    main()
