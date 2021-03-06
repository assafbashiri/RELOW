import socket
import sqlite3
import threading
from _thread import *
import pickle
import datetime

from kivy.uix.image import AsyncImage
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

if __name__ == '__main__':
    conn = sqlite3.connect('database.db', check_same_thread=False)
    # conn.text_factory = bytes
    repository = repository(conn)
    repository.create_tables()
    # repository.delete_all_db()
    u = UserController(conn)
    c = CategoryController(conn)
    offers, history_offers = c.load()
    u.load_users(offers, history_offers)
    print("server loaded users and categories")

    # first method removes the exp offers from categories
    # ter = c.get_all_expired_offers()
    # u.move_all_expired_to_history(ter)







    # # ------- check --------------
    # step1 = Step(50, 20)
    # step2 = Step(100, 15)
    # step3 = Step(150, 10)
    # steps = {1: step1, 2: step2, 3: step3}
    #
    # date = datetime.datetime(1996, 12, 15)
    #
    #
    # c.add_category("sport")
    # c.add_category("electronic")
    # c.add_category("sea")
    # c.add_sub_category("swim2", "sport")
    # c.add_sub_category("swim3", "sport")
    # c.add_sub_category("swim4", "sport")
    # c.add_sub_category("surf", "sea")
    # c.add_sub_category("computers", "electronic")
    # c.add_sub_category("swim", "sport")
    # u.register("amit","moskovitz", "amitmosk","amit@gmail.com","123",date, 1)
    # u.register("tom","nisim", "tomnis","tom@gmail.com","123",date, 1)
    #
    #
    #
    # of3 = c.add_offer(1, "shoko", "tnova", "green", "5/6", "nice prod", "AsyncImage(source ='images/a.png')", "sport", "swim", {1: step1, 2: step2, 3: step3}, date, False)
    # u.add_active_sale_offer(of3)
    # u.add_active_buy_offer(2, of3, 20, 1,"green","55")
    #
    #
    #
    # date = datetime.datetime(2022, 5, 17)
    # date1 = datetime.datetime(2018, 5, 17)
    #
    #
    # with open('ab.jpg', 'rb') as f:
    #     data = f.read()
    # of1 = c.add_offer(1, "shorts1", "fila", "blue", "5/6", "nice shorts", "data", "sport", "swim",{1: step1, 2: step2, 3: step3}, date, False)
    # # of2 = c.add_offer(1, "shorts1", "fila", "blue", "5/6", "nice shorts", "nophoto", 0, 0,  {1: step1, 2: step2, 3: step3}, date1)
    # of2 = c.add_offer(2, "shorts2", "fila", "blue", "5/6", "nice shorts"," AsyncImage(source ='images/a.png')", "sport", "swim", {1: step1, 2: step2, 3: step3},date, False)
    # res_to_check1 = c.get_offers_by_category("sport")
    # u.add_like_offer(2, of3)
    # u.add_like_offer(2, of2)
    # u.add_active_sale_offer(of1)
    # u.add_active_sale_offer(of2)
    #
    # tt= u.get_user_by_id(1)
    # u.logout(1)
    # u.logout(2)
    # #



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