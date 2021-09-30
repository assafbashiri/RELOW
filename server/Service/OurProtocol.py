import pickle
import sys

from twisted.internet.protocol import Protocol
from Service.Handler import Handler
from twisted.python.failure import Failure

import io
from kivy.uix.image import Image
from kivy.core.image import Image as CoreImage

class OurProtocol(Protocol):

    def _init_(self, conn, factory):
        self.handler = Handler(conn)
        self.factory = factory
        self.size = 65569
        self.data = b''
        self.counter = 1

    def connectionMade(self):
        #should send hot deals
        print("hey baby!!!")
        self.transport.write(pickle.dumps('hey client'))

    def connectionLost(self, res):
        print("connectionLost")
        print(res)
        a = 7
        self.handler.handling({'op':4})


    def dataReceived(self, data):
        print("[RECEIVE] "+"  number    "+ str(self.counter))
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
        # if self.size == 0:
        #     print('very big')
        #     self.counter+=1
        #     self.size = 65569
        #     return
        try:
            data = pickle.loads(self.data)
        except Exception as e:
            self.counter +=1
            return
        print('[RECEIVE] '+'got all')
        res = self.handler.handling(data)
        to_send = pickle.dumps(vars(res))
        print( '[SEND] ' + str(sys.getsizeof(to_send)))
        self.transport.write(to_send)
        self.counter = 1
        self.data = b''

    # if runner * 4000 > full_size:
    #     break
    # if runner * 4000 + 4000 > full_size:
    #     to_send = res1[runner * 4000:]
    # else:
    #     to_send = res1[runner * 4000:runner * 4000 + 4000]
    # self.transport.write(res1)
    # runner += 1

    def get_kivy_image_from_bytes(image_bytes, file_extension):
        # Return a Kivy image set from a bytes variable
        buf = io.BytesIO(image_bytes)
        cim = CoreImage(buf, ext=file_extension)
        return Image(texture=cim.texture)