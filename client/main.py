import socket
import pickle
import urllib
import urllib3
from kivy.clock import Clock

from Utils.CheckValidity import CheckValidity
from kivy.app import App
import threading
from kivymd.toast import toast
from kivy.lang import Builder
from twisted.internet import reactor
from twisted.internet.protocol import Factory, Protocol, ClientFactory
from twisted.internet import protocol
import googlemaps
import pprint
import time
import urllib
from geosky import geo_plug
import ast
import json
import requests
import math
from Backend_controller import Backend_controller
from Req_Answers import Req_Answers
from kivy.storage.jsonstore import JsonStore
# from Backend_controller import Backend_controller
from windows.mainWindow import TestApp
import sys

class Struct(object):
    def __init__(self, **entries):
        self.__dict__.update(entries)


def start_app(req):
    store = JsonStore('hello.json')
    controller = Backend_controller(req, store)
    TestApp(controller).run()
    # factory = EchoClientFactory()
    # a = reactor.connectTCP("127.0.0.1", 4000, factory)
    # reactor.run(a)
# class Echo(Protocol):
#     def __init__(self, **kwargs):
#         self.size = 65569
#         self.data = b''
#         self.counter = 0
#         self.bool = False
#
#     def startedConnecting(self, connector):
#         print('Started to connect.')
#         req_answers = Req_Answers()
#         # controller = Backend_controller(req_answers, store, self.a)
#         # TestApp(controller).run()
#
#     def dataReceived(self, data):
#         self.transport.write(pickle.dumps('hey server'))
#         if self.bool is False:
#             self.run_the_business()
#             self.bool = True
#         else:
#             print("dataReceived" + "  number    " + str(self.counter))
#             # buf = io.BytesIO(data)
#             # cim = CoreImage(buf, ext='png')
#             # return Image(texture=cim.texture)
#             self.data += data
#             self.size = self.size - sys.getsizeof(data)
#             if self.size == 0:
#                 print('very big')
#                 self.counter += 1
#                 self.size = 65569
#                 return
#             else:
#                 print('got all')
#                 data1 = pickle.loads(self.data)
#                 self.data = b''
#                 self.size = 65569
#                 self.counter = 0
#                 res = self.handler.handling(data1)
#                 to_send = pickle.dumps(vars(res))
#                 size = sys.getsizeof(to_send)
#                 print(size)
#                 print(to_send._sizeof_())
#                 # self.transport.write(pickle.dumps(size))
#                 self.transport.write(to_send)
#                 a = 8
#     def connectionMade(self):
#         #should send hot deals
#         print("hey baby!!!")
#
#     def connectionLost(self, res):
#         print("connectionLost")
#         print(res)
#
#     def run_the_business(self):
#         store = JsonStore('hello.json')
#         req_answers = Req_Answers()
#         controller = Backend_controller(req_answers, store, self)
#         t1 = threading.Thread(target=lambda x: TestApp(controller).run())
#         t1.start()
#         # TestApp(controller).run()
#
# class EchoClientFactory(Factory):
#     def __init__(self, **kwargs):
#         super(Factory, self).__init__(**kwargs)
#
#
#
#     def buildProtocol(self, addr):
#         print( 'Connected.')
#         self.a = Echo()
#         return self.a


class Echo(Protocol):
    def __init__(self,req):
        self.start = False
        self.data = b''
        self.counter = 1
        self.size_rec = False
        self.req_answers = req
    def dataReceived(self, data):
        if self.start == False:
            self.start = True
        else:
            print("[RECEIVE] " + "  number    " + str(self.counter)+"     size:   "+ str(sys.getsizeof(data)))
            self.data += data
            # if self.size <= 0:
            #     print('very big')
            #     self.counter += 1
            #     self.size = 20000
            #     return
            try:
                ans = pickle.loads(self.data)
            except Exception as e:
                self.counter += 1
                return
            print('[RECEIVE] '+'got all')
            ans1 = Struct(**ans)
            self.req_answers.add_answer(ans1)
        self.data = b''
        self.counter = 1
        req = self.req_answers.get_request()
        print('[SEND] '+ str(req))
        to_send = pickle.dumps(req)
        self.transport.write(to_send)

    def connectionMade(self):
        a = 9
        # self.transport.write(pickle.dumps('bolo'))
        # Clock.schedule_once(self.run_the_business())
        # self.run_the_business()
        # self.transport.write('to_send'.encode('utf8'))

    def run_the_business(self):
        self.req_answers = Req_Answers()
        t1 = threading.Thread(target=lambda: start_app(self.req_answers))
        t1.start()

    def send_data(self, data):
        to_send = pickle.dumps(data)
        self.transport.write(pickle.dumps('bolo'))

    def connectionLost(self, res):
        print("connectionLost")
        print(res)



class EchoClientFactory(ClientFactory):
    def __init__(self,req):
        self.req_answers = req

    def startedConnecting(self, connector):
        print('Started to connect.')



        # TestApp(controller).run()

    def buildProtocol(self, addr):
        print('Connected.')
        return Echo(self.req_answers)

    def clientConnectionLost(self, connector, reason):
        print('Lost connection.  Reason:', reason)

    def clientConnectionFailed(self, connector, reason):
        print('Connection failed. Reason:', reason)

    # def clientConnectionLost(self, connector, reason):
    #     print( 'Lost connection.  Reason:', reason)
    #
    # def clientConnectionFailed(self, connector, reason):
    #     print ('Connection failed. Reason:', reason)



def net(req):
    factory = EchoClientFactory(req)
    reactor.connectTCP("192.168.0.176", 80, factory)  # "129.168.1.19"
    reactor.run(installSignalHandlers=False)


def network(**kwargs):
    # --------------- connect to Server ---------------------------------
    print(kwargs['arg1'])
    print("start thread work")
    ClientSocket = socket.socket()
    host =  '127.0.0.1' #'192.168.1.19'
    port = 4000
    print('Waiting for connection..')
    try:
        ClientSocket.connect((host, port))
    except socket.error as e:
        print(str(e))

    # response = ClientSocket.recv(1024)
    # response1 = pickle.loads(response)
    # print(response1)


    # --------------- init the fields ---------------------------------



    # main Window as a Thread
    # mainWindow = MainWindow()

    while True:
        to_send = req_answers.get_request()
        message = pickle.dumps(to_send)

        a = ClientSocket.send(message)
        b = 9
        # if to_send['op'] == 2:
        #     ClientSocket.close()2169-+





        #     App.get_running_app().stop()
        #     break
        BUFF_SIZE = 4000  # 4 KiB
        data = b''
        part = ClientSocket.recv(BUFF_SIZE)
        chanks = pickle.loads(part)
        print(chanks)
        runner = int(math.ceil(chanks/4000))
        while part is not None:
            print(chanks)
            print('number!!!!!!!!!                                   '+str(runner))
            chanks -= 4000
            runner -= 1
            if chanks < 0:
                break
                # part = ClientSocket.recv(chanks-(4000*(runner-2)))
            # else:
            part = ClientSocket.recv(BUFF_SIZE)
            data += part


        decoded_ans = Struct(**(pickle.loads(data)))
        print(decoded_ans.message)
        if decoded_ans.message == 'EXIT':

            ex()
            req_answers.add_answer(decoded_ans)
            return
        req_answers.add_answer(decoded_ans)


def ex():
    App.get_running_app().stop()

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
    # echo = Echo()
    # factory = EchoClientFactory()
    # reactor.connectTCP("localhost", 4000, factory)  # "129.168.1.19"
    # reactor.run(installSignalHandlers=False)
    req_answers = Req_Answers()

    t1 = threading.Thread(target=lambda:net(req_answers))
    t1.start()
    time.sleep(2)
    store = JsonStore('hello.json')
    controller = Backend_controller(req_answers, store)
    TestApp(controller).run()