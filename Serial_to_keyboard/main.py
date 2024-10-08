import serial
import sys
from pynput.keyboard import Key, Controller
import serial.tools
import serial.tools.list_ports
keyboard = Controller()

serport = "COM0"
portlist = serial.tools.list_ports.comports()
print("Avaliable ports:")
for port in portlist:
    print(port)
    if (str(port)[7:45] == "Silicon Labs CP210x USB to UART Bridge"):
        serport = str(port)[0:4]

if serport == "COM0":
    print("no reader connected, press enter reconnect reader and restart program")
    input()
    sys.exit(0)


ser = serial.Serial(serport)


print("using \""+serport+"\" as reader port")

ser.write('bx\r\n'.encode())
message =ser.readline()
print("Set reader protocol...\r\n"+message.decode())
if message.decode() == "Set HEX Prot\r\n":
    print ("Ready for work, waiting for card input!!!")
    print ("="*40)

while 1:
    line = ser.read(12)
    str = bytearray(line[2:-2]).decode()+"00"
    buf = int(str,16)
    converted_num = "{}".format(buf)
    print ("0x"+str+">> hex to stopnet digits>> "+converted_num)
    keyboard.type(converted_num+"\r\n")
