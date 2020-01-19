import tkinter as tk 
from tkinter.ttk import Button
import time

class main_window:
    
    def __init__(self):
        self.tk = tk.Tk()
        self.frame = tk.Frame(self.tk)
        self.tk.attributes('-alpha', 1)
        self.tk.geometry('1920x1080')
        self.tk.config(bg = 'black')
        self.tk.title('Ground Control Station for AE442')
        
        
def abort_switch():
    abort_status = True
    abort_button.config(bg = 'red')
    
def ang_refresh(ang):
    color = 'red'

ang_status = True
abort_status = False
        
grd_con = tk.Tk()
grd_con.attributes('-alpha', 1)
grd_con.geometry('1920x1080')
grd_con.config(bg = 'black')
grd_con.title('Ground Station Control Menu for AE442')

color = 'green'

ang_monitor = tk.Label(grd_con)
ang_monitor.config(text = 'ANG STATUS')
ang_monitor.config(bg = color)
ang_monitor.grid(row = 1, column = 2)

abort_button = tk.Button(grd_con, command = abort_switch)
abort_button.config(text = 'ABORT')
abort_button.config(bg = 'green')
abort_button.config( height = '5', width = '20')
abort_button.grid(row = 1, column = 1)

# ang_monitor.after(1, ang_refresh)
# grd_con.mainloop()

win_main = tk.Tk()
win_main.geometry('1920x1080')
win_main.configure(bg='black')
status = tk.Label(win_main, text = "status norminal")
abort_button = Button(win_main, text = 'Abort')
abort_button.pack(side = tk.TOP, pady = 5)
status.pack()
win_main.mainloop()