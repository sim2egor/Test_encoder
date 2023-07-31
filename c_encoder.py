from queue import Queue
import threading
from interface import Interface



class Encoder():
    name = "encoder"
    path = "/dev/ttyUSB0"
    baudrate = 115200
    thread_read =None
    q1 =Queue()
    iface =None
    

    def __init__(self) -> None:
        self.__data:int =0
        


    def connect(self, path=None, baudrate=115200):
        self.path = path
        self.baudrate = baudrate
        self.iface =Interface("encoder_"+self.name,self.path,self.baudrate)
        self.iface.start(self.q1)
        self.thread_read =threading.Thread(target=self.onread)
        self.thread_read.start()

    def disconnect(self):
        self.iface.stop()
        self.iface= None

    def onread(self):

        while True:
            line =str(self.q1.get())
            arr=line.split()
            try :
                self.__data =int(arr[1])
                print(self.__data)
            except:
                ''' что то пошло не так, бывает'''
                pass

    def get_data(self):
        return self.__data


if __name__ == '__main__':
    conn= Encoder()
    conn.connect("/dev/ttyUSB0")
    
