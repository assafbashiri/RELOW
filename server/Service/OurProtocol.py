import pickle
import sys

from twisted.internet.protocol import Protocol
from Service.Handler import Handler
from twisted.python.failure import Failure

import io
from kivy.uix.image import Image
from kivy.core.image import Image as CoreImage

class OurProtocol(Protocol):

    def __init__(self, conn, factory):
        self.handler = Handler(conn)
        self.factory = factory
        self.size = 65569
        self.data = b''
        self.counter = 0

    def connectionMade(self):
        #should send hot deals
        print("hey baby!!!")

    def connectionLost(self, res):
        print("connectionLost")
        print(res)
        a = 7
        self.handler.handling({'op':4})


    def dataReceived(self, data):
        print("dataReceived"+"  number    "+ str(self.counter))
        # buf = io.BytesIO(data)
        # cim = CoreImage(buf, ext='png')
        # return Image(texture=cim.texture)

        a = 9
        # f  = input()
        # if  f == 'True':
        #     f = True
        # else:
        #     f = False
        self.data += data
        self.size = self.size - sys.getsizeof(data)
        if self.size == 0:
            print('very big')
            self.counter+=1
            self.size = 65569
            return
        else:
            print('got all')
            data1 = pickle.loads(self.data)
            self.data = b''
            self.size = 65569
            self.counter = 0
            res = self.handler.handling(data1)
            self.transport.write(pickle.dumps(vars(res)))


    def get_kivy_image_from_bytes(image_bytes, file_extension):
        # Return a Kivy image set from a bytes variable
        buf = io.BytesIO(image_bytes)
        cim = CoreImage(buf, ext=file_extension)
        return Image(texture=cim.texture)
