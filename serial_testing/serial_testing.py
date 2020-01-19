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
        # print(port)
        # print(port.strip('()'))
        ard_com = port.strip('()')
        
ser = serial.Serial(ard_com, baud_rate, timeout = 0, writeTimeout = 0)
time.sleep(1)
#print(ser.inWaiting())
while (ser.inWaiting() > 0):
    ser.read(1)
#print(ser.name)
delta = 0
start = time.time()
while (delta < .05):
    ser.write(b'1000')
    delta = time.time()-start
# time.sleep(1)
# ser.close()
if (ser.inWaiting() > 0):
    x = ser.readline().decode()
    print(x)
# print(ser.inWaiting())

