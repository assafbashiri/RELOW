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
    u.register("t3","n3","tn3","tomnisim3@gmail.com", 123, bdate, "male")
    u.register("t3","n3","tn3","tomnisim3@gmail.com", 123, bdate, "male")
    u.register("t3","n3","tn3","tomnisim3@gmail.com", 123, bdate, "male")

    product1 = Product("shorts1", "fila", "blue", "5/6", "nice shorts", "nophoto")
    #product2 = Product("shorts2", "fila", "blue", "5/6", "nice shorts", "nophoto")
    #product3 = Product("shorts3", "fila", "blue", "5/6", "nice shorts", "nophoto")

    date = datetime.datetime(2022, 5, 17)
    date1 = datetime.datetime(2018, 5, 17)
    step1 = Step(50,20)
    step2 = Step(100,15)
    step3 = Step(150,10)
    of1 = c.add_offer(1, "shorts1", "fila", "blue", "5/6", "nice shorts", "nophoto", 0, 0,  {1: step1, 2: step2, 3: step3}, date)
    #of2 = c.add_offer(1, "shorts1", "fila", "blue", "5/6", "nice shorts", "nophoto", 0, 0,  {1: step1, 2: step2, 3: step3}, date1)
    c.add_offer(2, "shorts2", "fila", "blue", "5/6", "nice shorts", "nophoto", 0, 0,  {1: step1, 2: step2, 3: step3}, date)
    c.add_offer(2, "shorts3", "fila1", "blue", "5/6", "nice shorts", "nophoto", 1, 1,  {1: step1, 2: step2, 3: step3}, date)
    u.add_active_sale_offer(of1)
    #u.add_active_sale_offer(of2)

    st = OfferStatus.OfferStatus.EXPIRED_COMPLETED
    u.update_status(1, 0, st)
    u.add_active_buy_offer(3,of1,20,1)
    u.add_active_buy_offer(2,of1,30,2)
    u.add_active_buy_offer(4,of1,40,2)
    u.add_active_buy_offer(5,of1,5,2)
    u.add_active_buy_offer(6,of1,15,3)
    res_to_check1 = c.get_offers_by_category(0)
    res_to_check2 = c.get_offers_by_sub_category(1,1)
    res_to_check3 = c.get_offers_by_product_name("shorts2")
    res_to_check4 = c.get_offers_by_status("NOT_EXPIRED_UNCOMPLETED")
    res_to_check5 = c.get_offers_by_company_name("fila1")

    exp = c.get_all_expired_offers()
    u.move_all_expired_to_history(exp)

    c.remove_sub_category(0, 0)
    c.remove_category(0)
    # ------- check -------------------------------------------------
    print("tom")
    #t1 = threading.Thread(target=network)
    #t1.start()


    
    #us.add_payment_method( 1, "1234", "19/04/2022", "048", "master", "31354888")

    #t1 = threading.Thread(target=network)
    #t1.start()

