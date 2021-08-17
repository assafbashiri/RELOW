import socket
import sqlite3
import threading
from _thread import *
import pickle
import datetime
from BusinessLayer.Object.Product import Product
from DB.Repository import repository
from BusinessLayer.Controllers.CategoryController import CategoryController
from BusinessLayer.Controllers.UserController import UserController
from BusinessLayer.Utils.OfferStatus import OfferStatus

from BusinessLayer.Object.Offer import Offer
from BusinessLayer.Object.Product import Product
from BusinessLayer.Object.Step import Step


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
    repository.delete_all_db()
    u = UserController(conn)
    c = CategoryController(conn)
    offers = c.load()
    u.load_users(offers)
    # ------- check -------------------------------------------------
    step1 = Step(50, 20)
    step2 = Step(100, 15)
    step3 = Step(150, 10)
    date = datetime.datetime(1996, 12, 15)


    c.add_category("sport")
    c.add_sub_category("swim", 1)
    u.register("amit","moskovitz", "amitmosk","amit@gmail.com","123",date, 1)
    u.register("tom","nisim", "tomnis","tom@gmail.com","123",date, 1)
    of1 = c.add_offer(1, "shoko", "tnova", "green", "5/6", "nice prod", "nophoto", 1, 1, {1: step1, 2: step2, 3: step3}, date)
    u.add_active_sale_offer(of1)
    u.add_active_buy_offer(2, of1, 20, 1)



    date = datetime.datetime(2022, 5, 17)
    date1 = datetime.datetime(2018, 5, 17)

    of1 = c.add_offer(1, "shorts1", "fila", "blue", "5/6", "nice shorts", "nophoto", 1, 1,{1: step1, 2: step2, 3: step3}, date)
    # of2 = c.add_offer(1, "shorts1", "fila", "blue", "5/6", "nice shorts", "nophoto", 0, 0,  {1: step1, 2: step2, 3: step3}, date1)
    of2 = c.add_offer(2, "shorts2", "fila", "blue", "5/6", "nice shorts", "nophoto", 1, 1, {1: step1, 2: step2, 3: step3},date)
    res_to_check1 = c.get_offers_by_category(1)

    u.add_active_sale_offer(of1)
    u.add_active_sale_offer(of2)
    #c.remove_sub_category(1, 1)
    #c.remove_category(1)
    # ------- check -------------------------------------------------
    #print("tom")
    # t1 = threading.Thread(target=network)
    # t1.start()

    # us.add_payment_method( 1, "1234", "19/04/2022", "048", "master", "31354888")

    # t1 = threading.Thread(target=network)
    # t1.start()

