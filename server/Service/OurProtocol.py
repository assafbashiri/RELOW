import pickle

from twisted.internet.protocol import Protocol
from Service.Handler import Handler
from twisted.python.failure import Failure


class OurProtocol(Protocol):

    def __init__(self, conn, factory):
        self.handler = Handler(conn)
        self.factory = factory

    def connectionMade(self):
        #should send hot deals
        print("hey baby!!!")

    def connectionLost(self, res):
        print("connectionLost")

    def dataReceived(self, data):
        print("dataReceived")
        data1 = pickle.loads(data)
        res = self.handler.handling(data1)

        print(type(res))
        print(res)
        self.transport.write(pickle.dumps(vars(res)))
