import socket
import sqlite3
import threading
from _thread import *
import pickle
import datetime
from BusinessLayer.Object.Product import Product
from Service.Handler import Handler
from DB.Repository import repository
from BusinessLayer.Controllers import CategoryController
from BusinessLayer.Controllers import UserController
from BusinessLayer.Utils import OfferStatus

from BusinessLayer.Object.Offer import Offer
from BusinessLayer.Object.Product import Product
from BusinessLayer.Object.Step import Step

from Service.OurFactory import OurFactory
from twisted.internet import reactor


class Struct(object):

    def __init__(self, **entries):
        self.__dict__.update(entries)

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
p1 = point(1,2)

def network():
    ServerSocket = socket.socket()
    host = '127.0.0.1'
    port = 4000
    ThreadCount = 0
    try:
        ServerSocket.bind((host, port))
    except socket.error as e:
        print(str(e))

    print('Waitiing for a Connection..')
    ServerSocket.listen(5)


    def threaded_client(connection):
        pro = Handler(conn)
        opening = 'Welcome to the Server'
        step1 = pickle.dumps(opening)
        print(step1)
        connection.send(step1)
        while True:
            data = connection.recv(2048)
            data1 = pickle.loads(data)
            print(type(data1), data1)
            # reply = 'Server Says: ' + data1
            if not data:
                break
            res, out = pro.handling(data1)
            # a = vars(res)
            b = pickle.dumps(vars(res))
            connection.sendall(b)
            if out is not None:
                break
        connection.close()

    while True:
        Client, address = ServerSocket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        start_new_thread(threaded_client, (Client,))
        ThreadCount += 1
        print('Thread Number: ' + str(ThreadCount))
    ServerSocket.close()


if __name__ == '__main__':

    conn = sqlite3.connect('database.db', check_same_thread=False)
    repository = repository(conn)
    repository.create_tables()
    u = UserController.UserController(conn)
    c = CategoryController.CategoryController(conn)
    reactor.listenTCP(4000, OurFactory(conn))
    reactor.run()
    # t1 = threading.Thread(target=network)
    # t1.start()