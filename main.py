from queue import Queue
import threading
import serial
from interface import Interface
name = "aaa"
path = "/dev/ttyUSB0"
baudrate = 115200
thread_read =None
q1 =Queue()

def onread():
    while True:
        line =q1.get()
        print(line)

iface =Interface("qqq_"+name,path,baudrate)
iface.start(q1)
thread_read =threading.Thread(target=onread)
thread_read.start()
