import tkinter as tk


def button_click():
    """ function to be run when button is clicked"""
    print("Button clicked!")


# Set up the window and the button within the window
window = tk.Tk()
button = tk.Button(window, text="Click Me", command=button_click)
button.pack()

# STart the main GUI processing loop
window.mainloop()
