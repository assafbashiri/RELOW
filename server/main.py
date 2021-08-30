import socket
import sqlite3
import threading
from _thread import *
import pickle
import datetime

from twisted.internet import reactor

from BusinessLayer.Object.Product import Product
from DB.Repository import repository
from BusinessLayer.Controllers.CategoryController import CategoryController
from BusinessLayer.Controllers.UserController import UserController
from BusinessLayer.Utils.OfferStatus import OfferStatus

from BusinessLayer.Object.Offer import Offer
from BusinessLayer.Object.Product import Product
from BusinessLayer.Object.Step import Step
from Service.OurFactory import OurFactory


class Struct(object):

    def __init__(self, **entries):
        self._dict_.update(entries)

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y



    

if __name__ == '__main__':
    conn = sqlite3.connect('database.db', check_same_thread=False)
    repository = repository(conn)
    repository.create_tables()
    repository.delete_all_db()
    u = UserController(conn)
    c = CategoryController(conn)
    print("%")

    #  #offers = c.load()
    # #u.load_users(offers)
    # # ------- check -------------------------------------------------
    step1 = Step(50, 20)
    step2 = Step(100, 15)
    step3 = Step(150, 10)
    steps = {1: step1, 2: step2, 3: step3}
    date = datetime.datetime(1996, 12, 15)


    c.add_category("sport")
    c.add_sub_category("swim", "sport")
    u.register("amit","moskovitz", "amitmosk","amit@gmail.com","123",date, 1)
    u.register("tom","nisim", "tomnis","tom@gmail.com","123",date, 1)



    of3 = c.add_offer(1, "shoko", "tnova", "green", "5/6", "nice prod", "nophoto", "sport", "swim", {1: step1, 2: step2, 3: step3}, date)
    u.add_active_sale_offer(of3)
    u.add_active_buy_offer(2, of3, 20, 1)



    date = datetime.datetime(2022, 5, 17)
    date1 = datetime.datetime(2018, 5, 17)

    of1 = c.add_offer(1, "shorts1", "fila", "blue", "5/6", "nice shorts", "nophoto", "sport", "swim",{1: step1, 2: step2, 3: step3}, date)
    # of2 = c.add_offer(1, "shorts1", "fila", "blue", "5/6", "nice shorts", "nophoto", 0, 0,  {1: step1, 2: step2, 3: step3}, date1)
    of2 = c.add_offer(2, "shorts2", "fila", "blue", "5/6", "nice shorts", "nophoto", "sport", "swim", {1: step1, 2: step2, 3: step3},date)
    res_to_check1 = c.get_offers_by_category("sport")

    u.add_active_sale_offer(of1)
    u.add_active_sale_offer(of2)

    tt= u.get_user_by_id(1)
    a=9

    reactor.listenTCP(4000, OurFactory(conn))
    reactor.run()


    #c.remove_sub_category(1, 1)
    #c.remove_category(1)
    # ------- check -------------------------------------------------
    #print("tom")
    # t1 = threading.Thread(target=network)
    # t1.start()

    # us.add_payment_method( 1, "1234", "19/04/2022", "048", "master", "31354888")

    # t1 = threading.Thread(target=network)
    # t1.start()