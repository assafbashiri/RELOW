import pickle
import time
import sys
import threading

from kivy.app import App
from kivy.lang import Builder
from kivy.storage.jsonstore import JsonStore

from twisted.internet import reactor
from twisted.internet.protocol import Factory, Protocol, ClientFactory

from Backend_controller import Backend_controller
from Req_Answers import Req_Answers
from kivy.storage.jsonstore import JsonStore
from windows.mainWindow import TestApp


class Struct(object):
    def __init__(self, **entries):
        self.__dict__.update(entries)


class Echo(Protocol):
    def __init__(self, req):
        self.start = False
        self.data = b''
        self.counter = 1
        self.req_answers = req

    def dataReceived(self, data):
        if self.start == False:
            self.start = True
        else:
            print("[RECEIVE] " + "  number    " + str(self.counter) + "     size:   " + str(sys.getsizeof(data)))
            self.data += data
            try:  # check if all the data arived
                ans = pickle.loads(self.data)
            except Exception as e:
                self.counter += 1
                return
            print('[RECEIVE] ' + 'got all')
            ans1 = Struct(**ans)
            self.req_answers.add_answer(ans1)
        self.data = b''
        self.counter = 1
        req = self.req_answers.get_request()
        print('[SEND] ' + str(req))
        to_send = pickle.dumps(req)
        self.transport.write(to_send)

    def connectionMade(self):
        print('ready to work')

    def connectionLost(self, res):
        print("connectionLost")
        print(res)


class EchoClientFactory(ClientFactory):
    def __init__(self, req):
        self.req_answers = req

    def startedConnecting(self, connector):
        print('Started to connect.')

    def buildProtocol(self, addr):
        print('Connected.')
        return Echo(self.req_answers)

    def clientConnectionLost(self, connector, reason):
        print('Lost connection.  Reason:', reason)

    def clientConnectionFailed(self, connector, reason):
        print('Connection failed. Reason:', reason)


def net(req):
    factory = EchoClientFactory(req)
    reactor.connectTCP("localhost", 4000, factory)  # "129.168.1.19"
    reactor.run(installSignalHandlers=False)


if __name__ == '__main__':
    Builder.load_file('windows/mainWindow.kv')
    Builder.load_file('windows/managerWindow.kv')
    Builder.load_file('windows/connectWindow.kv')
    Builder.load_file('windows/accountWindow.kv')
    Builder.load_file('windows/searchWindow.kv')
    Builder.load_file('windows/addofferWindow.kv')
    Builder.load_file('windows/updateOfferWindow.kv')
    Builder.load_file('windows/registerWindow.kv')
    Builder.load_file('windows/loginWindow.kv')
    Builder.load_file('windows/offers_list.kv')
    Builder.load_file('windows/my_offersWindow.kv')
    Builder.load_file('windows/confirmationWindow.kv')
    Builder.load_file('windows/contactWindow.kv')
    Builder.load_file('windows/sellerWindow.kv')
    Builder.load_file('windows/paymentWindow.kv')
    Builder.load_file('windows/termsWindow.kv')
    Builder.load_file('windows/offerWindow.kv')
    req_answers = Req_Answers()
    t1 = threading.Thread(target=lambda: net(req_answers))
    t1.start()
    time.sleep(2)
    store = JsonStore('hello.json')
    controller = Backend_controller(req_answers, store)
    TestApp(controller).run()
