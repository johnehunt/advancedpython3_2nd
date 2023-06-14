import tkinter as tk

root = tk.Tk()

# Create a top-level window
top_level = tk.Toplevel(root)
top_level.title("My TopLevel")

# Add widgets to the top-level window
label = tk.Label(top_level, text="This is a top level window.")
label.pack()

root.mainloop()

