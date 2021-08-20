from twisted.internet.protocol import Factory

from Service.OurProtocol import OurProtocol


class OurFactory(Factory):

    def __init__(self, conn):
        self.conn = conn

    def buildProtocol(self, addr):
        print('Connected.')
        return OurProtocol(self.conn, self)
