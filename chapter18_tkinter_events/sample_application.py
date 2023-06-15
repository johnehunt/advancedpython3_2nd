import tkinter as tk

def button_click(event):
    print(f'Button clicked: {event}')

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
window.title('Sample Application')

button = tk.Button(window, text='Click Me!')
button.pack()
button.bind('<Button-1>', button_click)

label = tk.Label(window, text='User Name')
label.pack( side = tk.LEFT)

entry = tk.Entry(window, bd =5)
entry.pack(side = tk.RIGHT)
entry.bind('<FocusIn>', focus_gained)
entry.bind('<FocusOut>', focus_lost)
entry.bind('<Key>', key_press)


window.mainloop()
