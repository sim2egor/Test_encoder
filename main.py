from queue import Queue
import threading
from interface import Interface



class Encoder():
    name = "aaa"
    path = "/dev/ttyUSB0"
    baudrate = 115200
    thread_read =None
    q1 =Queue()
    iface =None


    def connect(self, path=None, baudrate=115200):
        self.path = path
        self.baudrate = baudrate
        self.iface =Interface("qqq_"+self.name,self.path,self.baudrate)
        self.iface.start(self.q1)
        self.thread_read =threading.Thread(target=self.onread)
        self.thread_read.start()

    def disconnect(self):
        self.iface.stop()
        self.iface= None

    def onread():
        while True:
            line =q1.get()
            print(line)
