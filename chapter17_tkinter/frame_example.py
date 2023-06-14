import tkinter as tk

root = tk.Tk()

# Create a frame
frame = tk.Frame(root)
frame.pack()

# Add widgets to the frame
label = tk.Label(frame, text="Hello, World!")
label.pack()

root.mainloop()
