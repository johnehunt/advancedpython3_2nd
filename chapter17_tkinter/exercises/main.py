import tkinter as tk
import tkinter.simpledialog as simpledialog

# Set up the window and the button within the window
window = tk.Tk()
# Set teh size of the window
window.geometry("200x80")
# Set the title of the tkinter window
window.title('Simple Window')

label = tk.Label(window, text="<<...>>")
label.pack()

def display_dialog():
    answer = simpledialog.askstring("Name Entry", "Please enter your name:")
    if answer:
        print("Your name is:", answer)
        label.config(text=answer)
    else:
        print("No input provided.")

# Add a button to the window
button = tk.Button(window,
                   text="Click Me",
                   command=display_dialog)
button.pack()

# Start the main GUI processing loop
window.mainloop()
