# IMPORTS--------------------

import tkinter as tk 
import time
import serial
import serial.tools.list_ports as l_p

#----------------------------

# SET UP THE CLASS-----------

class ground_station:
# a wrapping class for the actual tkinter root
	
	def __init__(self, root):
		self.root = root
		self.setup_gui()
		self.setup_serial()
	
	# set up the main window of the gui
	def setup_main_win(self):
		self.root.title('AE442 GROUND STATION')
		self.root.config(bg = 'black')
		self.root.attributes('-alpha', 1)
	
	# set up the orientation monitor window
	def ori_widget(self):
		self.ori_frame = tk.LabelFrame(self.root, text = 'Rocket Orientation',\
								  padx = 200, pady = 200, bg = 'grey')
		self.ori_frame.grid(row = 0, column = 0)
		
		button_test = tk.Button(self.ori_frame, text = 'nice', command = None)
		button_test.pack()
	
	# set up the stage and abort buttons
	def button_widget(self):
		self.button_frame = tk.LabelFrame(self.root, text = 'Rocket Control',\
								  padx = 200, pady = 50)
		self.button_frame.grid(row = 1, column = 0)
		
		button_test = tk.Button(self.button_frame, text = 'nice', command = None)
		button_test.pack()
		
	# set up the serial output stream
	def serial_output_widget(self):
		serial_out_frame = tk.LabelFrame(self.root, text = 'Serial Out',\
								  padx = 5, pady = 5)
		serial_out_frame.grid(row = 1, column = 1)
		
		scrollbar = tk.Scrollbar(serial_out_frame, orient = 'vertical')
		scrollbar.pack(side = 'right', fill = 'y')
	
	# set up the serial input bar
	def serial_input_widget(self):
		pass
		
	
	def indicator_widget(self):
		self.indicator_frame = tk.LabelFrame(self.root, text = 'Indicators',\
								  padx = 5, pady = 5)
		self.indicator_frame.grid(row = 0, column = 1)
		
		button_test = tk.Button(self.indicator_frame, text = 'nice', command = None)
		button_test.pack()
		
	def state_widget(self):
		self.state_frame = tk.LabelFrame(self.root, text = 'Rocket State',\
								  padx = 5, pady = 5)
		self.state_frame.grid(row = 0, column = 2)
		
		button_test = tk.Button(self.state_frame, text = 'nice', command = None)
		button_test.pack()
		
	def setup_gui(self):
		self.setup_main_win()
		self.ori_widget()
		self.button_widget()
		self.serial_output_widget()
		self.serial_input_widget()
		self.indicator_widget()
		self.state_widget()
		
	def setup_serial(self):
		ports = list(l_p.comports())
		baud_rate = 115200
		ser_delay = 3
		
		for p in ports:
			if 'Arduino' in p.description:
				name = p.description.split(' ')
				port = name[2]
				ard_com = port.strip('()')
		
		try:
			self.ser = serial.Serial(ard_com, \
									 baud_rate, \
									 timeout = 0.1, )
			print('Established connection over com port: {}'.format(ard_com))
		except:
			print('Could not connect to the serial port')
			
   # get the message from the input widget
	def get_input_msg(self):
		pass
	
	# transmit a serial message
	def send_serial_msgs(self, message):
		message += '\n'
		
		self.ser.write(message.encode('utf-8'))
	
	def read_serial(self):
		
		if (self.ser.inWaiting() > 3):
			try:
				x = self.ser.readline().decode()
				print(x)
			except:
				print('Message Not Received at: {}'.format(time.time()))
	
	def update_gui(self):
		self.send_serial_msgs('nice')
		self.read_serial()
		self.root.after(10, self.update_gui)
#----------------------------

# RUN THE GUI----------------

grd_st_tk = tk.Tk()
grd_st = ground_station(grd_st_tk)
grd_st.update_gui()
grd_st_tk.mainloop()
