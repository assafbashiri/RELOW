import pickle
import sys
import io

from twisted.internet.protocol import Protocol
from Service.Handler import Handler

from kivy.uix.image import Image
from kivy.core.image import Image as CoreImage


class OurProtocol(Protocol):
    def __init__(self, conn, factory):
        self.handler = Handler(conn)
        self.factory = factory
        self.data = b''
        self.counter = 1

    def connectionMade(self):
        print("connected")
        self.transport.write(pickle.dumps('hey client'))

    def connectionLost(self, res):
        print("connectionLost")
        print(res)
        self.handler.handling({'op':4})


    def dataReceived(self, data):
        print("[RECEIVE] "+"  number    " + str(self.counter))
        self.data += data
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

    def get_kivy_image_from_bytes(image_bytes, file_extension):
        # Return a Kivy image set from a bytes variable
        buf = io.BytesIO(image_bytes)
        cim = CoreImage(buf, ext=file_extension)
        return Image(texture=cim.texture)