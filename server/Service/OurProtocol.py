import pickle

from twisted.internet.protocol import Protocol
from Service.Handler import Handler
from twisted.python.failure import Failure


class OurProtocol(Protocol):

    def __init__(self, conn, factory):
        self.handler = Handler(conn)
        self.factory = factory

    def connectionMade(self):
        print("hey baby!!!")

    def connectionLost(self, res):
        print("fuck you ba baby")

    def dataReceived(self, data):
        data1 = pickle.loads(data)
        print(type(data1))
        res = self.handler.handling(data1)
        self.transport.write(pickle.dumps(res))
        if data1['op'] == '2':
            self.transport.connectionLost(Failure(BaseException(None)))
