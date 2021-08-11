import socket
import sqlite3
import threading
from _thread import *
import pickle
import datetime
from BusinessLayer.Object.Product import Product
from Service.protocol import Protocol
from DB.Repository import repository
from BusinessLayer.Controllers import CategoryController
from BusinessLayer.Controllers import UserController
from BusinessLayer.Utils import OfferStatus

from BusinessLayer.Object.Offer import Offer
from BusinessLayer.Object.Product import Product


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
    repository.create_tables()
    u = UserController.UserController(conn)
    c = CategoryController.CategoryController(conn)
    # ------- check -------------------------------------------------
    repository.delete_all_db()

    bdate = datetime.datetime(1996, 12, 15)
    c.add_category("sport")#0
    c.add_category("cars")#1
    c.add_sub_category_by_name("soccer", "sport")
    c.add_sub_category_by_name("bmw", "cars")
    u.register("t1","n1","tn1","tomnisim1@gmail.com", 123, bdate, "male")
    u.register("t2","n2","tn2","tomnisim2@gmail.com", 123, bdate, "male")
    u.register("t3","n3","tn3","tomnisim3@gmail.com", 123, bdate, "male")

    #product1 = Product("shorts1", "fila", "blue", "5/6", "nice shorts", "nophoto")
    #product2 = Product("shorts2", "fila", "blue", "5/6", "nice shorts", "nophoto")
    #product3 = Product("shorts3", "fila", "blue", "5/6", "nice shorts", "nophoto")

    date = datetime.datetime(2022, 5, 17)
    c.add_offer(1, "shorts1", "fila", "blue", "5/6", "nice shorts", "nophoto", 0, 0,  {}, date)
    c.add_offer(2, "shorts2", "fila", "blue", "5/6", "nice shorts", "nophoto", 0, 0,  {}, date)
    c.add_offer(2, "shorts3", "fila", "blue", "5/6", "nice shorts", "nophoto", 1, 1,  {}, date)
    res_to_check = c.get_offers_by_category(0)



    c.remove_sub_category(0, 0)
    c.remove_category(0)
    # ------- check -------------------------------------------------
    print("tom")
    t1 = threading.Thread(target=network)
    t1.start()


    
    #us.add_payment_method( 1, "1234", "19/04/2022", "048", "master", "31354888")

    #t1 = threading.Thread(target=network)
    #t1.start()

