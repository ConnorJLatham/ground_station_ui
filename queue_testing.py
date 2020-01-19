# from here: https://stackoverflow.com/questions/16938647/python-code-for-serial-data-to-print-on-window

import serial
import threading
import queue
import tkinter as tk



class SerialThread(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
    def run(self):
        s = serial.Serial('COM1',9600)
        while True:
            if s.inWaiting():
                text = s.readline(s.inWaiting())
                self.queue.put('yes')

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("1360x750")
        frameLabel = tk.Frame(self, padx=40, pady =40)
        self.text = tk.Text(frameLabel, wrap='word', font='TimesNewRoman 37',
                            bg=self.cget('bg'), relief='flat')
        frameLabel.pack()
        self.text.pack()
        self.queue = queue.Queue()
        thread = SerialThread(self.queue)
        thread.start()
        self.process_serial()

    def process_serial(self):
        while self.queue.qsize():
            try:
                self.text.delete(1.0, 'end')
                self.text.insert('end', self.queue.get())
            except queue.Empty:
                pass
        self.after(100, self.process_serial)

app = App()
app.mainloop()