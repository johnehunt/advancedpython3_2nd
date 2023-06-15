import tkinter as tk


def button_click():
    """ function to be run when button is clicked"""
    print("Button clicked!")


# Set up the window and the button within the window
window = tk.Tk()

# Set the size of the window
window.geometry("200x80")

# Set the title of the tkinter window
window.title('Simple Window')

# Add a button to the window
button = tk.Button(window,
                   text="Click Me",
                   command=button_click)
button.pack()

# Start the main GUI processing loop
window.mainloop()
