import socket
import sqlite3
import threading
from _thread import *
import pickle
import datetime
from BussinessLayer.Object.Product import Product
from Service.protocol import Protocol
from DB.Repository import repository
from BussinessLayer.Controllers import CategoryController
from BussinessLayer.Controllers import UserController
from BussinessLayer.Utils import OfferStatus

from server.BussinessLayer.Object.Offer import Offer
from server.BussinessLayer.Object.Product import Product


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
    port = 1233
    ThreadCount = 0
    try:
        ServerSocket.bind((host, port))
    except socket.error as e:
        print(str(e))

    print('Waitiing for a Connection..')
    ServerSocket.listen(5)

    def threaded_client(connection):
        pro = Protocol(conn)
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
            res = pro.handling(data1)
            # a = vars(res)
            b = pickle.dumps(res)
            connection.sendall(b)
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
    #repository.create_tables()
    u = UserController.UserController(conn)
    c = CategoryController.CategoryController(conn)
    # ------- check -------------------------------------------------
    c.add_category("sport")
    c.add_sub_category("soccer", 0)

    product = Product("shorts", "fila", "blue", "5/6", "nice shorts", "nophoto")
    date = datetime.datetime(2020, 5, 17)
    c.add_offer(1, product, 0, 0, OfferStatus.OfferStatus.NOT_EXPIRED_UNCOMPLETED, {}, date, {})
    c.remove_sub_category(0, 0)
    c.remove_category(0)
    # ------- check -------------------------------------------------
    print("tom")
    repository.delete_all_db()
    t1 = threading.Thread(target=network)
    t1.start()

    repository.create_tables()
    
    #us.add_payment_method( 1, "1234", "19/04/2022", "048", "master", "31354888")

    #t1 = threading.Thread(target=network)
    #t1.start()

