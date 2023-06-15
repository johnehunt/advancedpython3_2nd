import tkinter as tk
import tkinter.simpledialog as simpledialog

def key_press(event):
    print("Key pressed:", event.char)

def focus_lost(event):
    print(f'Widget {event.widget} lost focus')

def focus_gained(event):
    print(f'Widget {event.widget} gained focus')

# Create main window
window = tk.Tk()
# Set the size of the window
window.geometry('300x120')
# Set the title of the window
window.title('Sample App')

# Create a frame
frame = tk.Frame(window)
frame.pack()

label = tk.Label(frame, text='User Name')
label.pack( side = tk.LEFT)

# Set up a 'ext variable' to use with the entry field
# Makes setting it programmatically easier (don't need to delete and insert)
entry_text = tk.StringVar()
entry = tk.Entry(frame, textvariable=entry_text, bd =5)
entry.pack(side = tk.RIGHT)
entry.bind('<FocusIn>', focus_gained)
entry.bind('<FocusOut>', focus_lost)
entry.bind('<Key>', key_press)

def button_click(event):
    answer = simpledialog.askstring("Name Entry", "Please enter your name:")
    if answer:
        print("Your name is:", answer)
        entry_text.set(answer)
    else:
        print("No input provided.")

button = tk.Button(window, text='Show Message')
button.pack()
button.bind('<Button-1>', button_click)

window.mainloop()
