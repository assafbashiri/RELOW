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
        print("fuck you ba baby")

    def dataReceived(self, data):
        print("hello")
        data1 = pickle.loads(data)
        print(type(data1))
        res = self.handler.handling(data1)
        print(type(res))
        print(res)
        res1 = res[0]
        print(type(res1))
        print(res1)
        a = vars(res1)
        self.transport.write(pickle.dumps(a))
