import tkinter as tk
from datetime import datetime


def button_click(event):
    print('Button clicked!')
    print(event)
    print(f'Event type: {event.type}')
    print(f'Widget: {event.widget}')
    print(f'Time: {datetime.fromtimestamp(event.time / 1e3)}')


# Create main window
window = tk.Tk()
# Set the size of the window
window.geometry('200x80')
# Set the title of the window
window.title('Simple Window')

# Create button
button = tk.Button(window,
                   text="Click Me!",
                   name='my button')
button.pack()

# Bind the button_click function to the <Button-1> event
button.bind("<Button-1>", button_click)

window.mainloop()
