import tkinter as tk
import tkinter.simpledialog as simpledialog

root = tk.Tk()


# Function to display an input dialog
def display_dialog():
    answer = simpledialog.askstring("Name Entry", "Please enter your name:")
    if answer:
        print("Your name is:", answer)
    else:
        print("No input provided.")


# Create a button to show the dialog
button = tk.Button(root, text="Open Dialog", command=display_dialog)
button.pack()

root.mainloop()
