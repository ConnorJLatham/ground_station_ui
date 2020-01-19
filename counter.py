# from: https://www.python-course.eu/tkinter_buttons.php
# also check: https://www.daniweb.com/programming/software-development/threads/505937/python-tkinter-delay-hangs-using-after-method
# and: https://docs.python.org/3/library/asyncio-task.html

import tkinter as tk
import random as r 

def abort_switch():
    abort_status = True
    abort_button.config(bg = 'red')

def get_data():
    data = r.randint(0, 2)
    return data

def get_labels():
    labels = [label, label_2]
    return labels

def update_display():
    data = get_data()
    labels = get_labels()
    for label in labels:
        label.config(text = str(data))
        if data>1:
            label.config(bg = 'red')
        else:
            label.config(bg = 'green')
    label.after(100, update_display)

root = tk.Tk()
root.title("Counting Seconds")

label_2 = tk.Label(root, bg = 'red')
label_2.pack()
label = tk.Label(root, fg="dark green")
label.pack()

abort_button = tk.Button(root, command = abort_switch)
abort_button.config(text = 'ABORT')
abort_button.config(bg = 'green')
abort_button.config( height = '5', width = '20')
abort_button.pack()

update_display()

button = tk.Button(root, text='Stop', width=25, command=root.destroy)
button.pack()
root.mainloop()