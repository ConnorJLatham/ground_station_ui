import serial
import serial.tools.list_ports as l_p
import time

ports = list(l_p.comports())

baud_rate = 115200
timeout = 3

for p in ports:
    if 'Arduino' in p.description:
        name = p.description.split(' ')
        port = name[2]
        ard_com = port.strip('()')
        
ser = serial.Serial(
                    ard_com, \
                    baud_rate, \
                    timeout = .1, \
                    writeTimeout = 0)
time.sleep(1)

while True:
    if (ser.inWaiting() > 20):
        try:
            x = ser.readline().decode()
            print(x)
            print(ser.inWaiting())
        except:
            print('didnt get it')