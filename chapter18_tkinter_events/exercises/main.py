import tkinter as tk
from tkinter import messagebox

def enter_button_click(event):
    print(f'Enter Button Click {event}')
    age = age_entry_text.get()
    if not age.isnumeric():
        messagebox.showerror('Error', f"Age is not a number: '{age}'")
    else:
        welcome_label.config(text=f'Welcome {name_entry.get()}')


def birthday_button_click(event):
    print(f'Birthday Button Click {event}')
    old_age = age_entry_text.get()
    new_age = int(old_age) + 1
    age_entry_text.set(str(new_age))
    msg = f'Happy birthday {name_entry.get()} you are now {new_age}'
    messagebox.showinfo("Birthday", msg)


# Create main window
window = tk.Tk()
# Set the size of the window
window.geometry('260x160')
# Set the title of the window
window.title('Happy Birthday App')

# Create a frame
frame = tk.Frame(window)
frame.pack()

name_label = tk.Label(frame, text='Name: ')
name_label.pack(side=tk.LEFT)

name_entry = tk.Entry(frame, bd=5)
name_entry.pack(side=tk.RIGHT)

frame2 = tk.Frame(window)
frame2.pack()

age_label = tk.Label(frame2, text='Age: ')
age_label.pack(side=tk.LEFT)

age_entry_text = tk.StringVar()
age_entry = tk.Entry(frame2, textvariable=age_entry_text, bd=5)
age_entry.pack(side=tk.RIGHT)

frame3 = tk.Frame(window)
frame3.pack()

button = tk.Button(window, text='Enter')
button.pack()
button.bind('<Button-1>', enter_button_click)

welcome_label = tk.Label(window, text='Welcome')
welcome_label.pack()

button = tk.Button(window, text='Birthday')
button.pack()
button.bind('<Button-1>', birthday_button_click)

window.mainloop()