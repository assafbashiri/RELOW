import pickle

from kivy.app import App
from kivy.storage.jsonstore import JsonStore

from twisted.internet import reactor


from kivymd.toast import toast

from Service.Object.OfferService import OfferService
from Service.Object.UserService import UserService
from Service.Object.CategoryService import CategoryService
from windows.mainWindow import Main_page_box
from windows.offers_list import Offers_Screen

from Response import Response


class Backend_controller:
    def __init__(self, req_answers, store):
        self.req_answers = req_answers
        # user / categories DATA
        self.user_service = None
        # self.client = client
        self.hot_deals = self.get_hot_deals()
        self.categories = None
        self.guest = False
        self.seller = None
        self.insert_offers()
        self.store = store
        self.init_categories()

    def insert_offers(self):
        pass
        # Offers_Screen_search.insert_offers(self=Offers_Screen_search)
        # Main_page_box.insert_offers(self= Main_page_box)
    def get_categories(self):
        return self.categories

    def init_categories(self):
        self.categories = []

        categories_req = {"op":56}
        self.req_answers.add_request(categories_req)
        ans = self.req_answers.get_answer()
        if ans.res is True:
            for cat in ans.data:
                y = CategoryService(cat)
                self.categories.append(y)

    def update_password(self, old_password, new_password):
        update_password_req = {'op': 6, 'old_password': old_password, 'new_password': new_password}
        self.req_answers.add_request(update_password_req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        return ans

    def guest_register(self):
        req = {'op': 78}
        self.req_answers.add_request(req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        if ans.res is True:
            self.store.put("user_guest", user_id = ans.data['user_id'])
            self.user_service = UserService(ans.data['user_id'], None, None,None,None,None,None,None,None,False,None,None,None,None,None,None,None,None,None,[],[],[],[],[])
            self.guest = True
            self.seller = False


            # we removed the user_info dict, and we add element to user_guest insted- coplete tommorow

    def guest_login(self, guest_id):
        req = {'op': 79, 'guest_id': guest_id}
        self.req_answers.add_request(req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        if ans.res is True:
            user = self.store.get('user_guest')
            self.user_service = UserService(guest_id, None, None,None,None,None,None,None,False,None,None,None,None,None,None,None,None,None,None,[],[],[],[],[])
            self.guest = True
            self.seller = False
            self.store.put('user_guest', user_id= guest_id)

    def register(self, first_name, last_name, phone, email, password, birth_date, gender):
        store = JsonStore('hello.json')
        if store.exists('user_guest'):
            user = store.get('user_guest')
            register_req = {
                'op': 80, 'user_id': user['user_id'], 'first_name': first_name, 'last_name': last_name, 'phone': phone,
                'email': email, 'password': password, 'birth_date': birth_date, 'gender': gender, 'seller':False
            }
        #     active = self.store['user']['user_info']['active']
        #     if active is True:
        #         toast("already register")
        #         return Response(None, None, False)

        # encode the request for Server-Language
        else:
            register_req = {
                'op': 1, 'first_name': first_name, 'last_name': last_name, 'phone': phone,
                'email': email, 'password': password, 'birth_date': birth_date, 'gender': gender, 'seller':False
        }
        # adding to the req_answers, and the Main-Thread should send them to the server
        self.req_answers.add_request(register_req)
        # waiting for an answer from the server to the Main-Thread, and for the Main_thread adding the answer to the
        # req_answers
        ans = self.req_answers.get_answer()
        print(ans.message)
        if ans.res is True:
            self.guest = False
            self.seller = False
            if self.seller == 0:
                App.get_running_app().root.screens[0].ids.down_menu.ids.add_offer.text = 'BECOME A SELLER'
            else:
                App.get_running_app().root.screens[0].ids.down_menu.ids.add_offer.text = 'ADD OFFER'
            if store.exists('user_guest'):
                self.store.delete('user_guest')
            self.store.put("user", user_id= ans.data['user_id'],
                           password = ans.data['password'],
                           email = ans.data['email'])
            # have to delete guest from store
            self.register_unregister_json(True)
            self.user_service = self.build_user(ans.data)
        return ans

    def unregister(self):
        # active = self.store['user']['user_info']['active']
        # if active is True:
        #     toast("already unregister")
        #     return Response(None, None, False)
        unregister_req = {'op': 2}
        self.req_answers.add_request(unregister_req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        if ans.res is True:
            self.register_unregister_json(False)
            self.user_service = None
            self.guest = True
        return ans

    def register_unregister_json(self, flag):
        pass

    def login_from_exist_user(self, email, password):
        store = JsonStore('hello.json')
        login_req = {'op': 3, 'email': email, 'password': password}
        self.req_answers.add_request(login_req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        if ans.res is True:
            # JSON
            if store.exists('user_guest'):
                self.store.delete('user_guest')
            self.store.put("user", user_id=ans.data['user_id'],
                           email=ans.data['email'],
                           password=ans.data['password'])
            self.user_service = self.build_user(ans.data)
            self.guest = False
            self.seller = self.user_service.seller
            if App.get_running_app().root is not None:
                if self.seller == 0:
                    App.get_running_app().root.screens[0].ids.down_menu.ids.add_offer.text = 'BECOME A SELLER'
                else:
                    App.get_running_app().root.screens[0].ids.down_menu.ids.add_offer.text = 'ADD OFFER'
        return ans

    def login(self, email, password):
        store = JsonStore('hello.json')
        login_req = {'op': 82, 'email': email, 'password': password, 'guest_id': self.user_service.user_id}
        self.req_answers.add_request(login_req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        if ans.res is True:
            # JSON
            if store.exists('user_guest'):
                self.store.delete('user_guest')
            self.store.put("user", user_id=ans.data['user_id'],
                           email=ans.data['email'],
                           password=ans.data['password'])
            self.user_service = self.build_user(ans.data)
            self.guest = False
            self.seller = self.user_service.seller
            if self.seller == 0:
                App.get_running_app().root.screens[0].ids.down_menu.ids.add_offer.text = 'BECOME A SELLER'
            else:
                App.get_running_app().root.screens[0].ids.down_menu.ids.add_offer.text = 'ADD OFFER'
        return ans

    def logout(self):
        store = JsonStore('hello.json')
        logout_req = {'op': 4}
        self.req_answers.add_request(logout_req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        if ans.res is True:
            self.user_service = None
            self.guest = True
            if store.exists('user'):
                self.store.delete('user')
        return ans

    # ------------------- Account Window ---------------------------------------------------------------------
    def update_offer(self, offer_id, category_name, sub_category_name, user_id, name, company, colors, sizes,
                     description, steps, end_date):
        update_req = {'op': 15, 'offer_id': offer_id, 'category_name': category_name,
                      'sub_category_name': sub_category_name, 'user_id': user_id, 'name': name,
                      'company': company, 'colors': colors, 'sizes': sizes, 'description': description,
                      'steps': steps, 'end_date': end_date}
        self.req_answers.add_request(update_req)
        ans = self.req_answers.get_answer()

        for ex in ans.message:
            toast(ex)
        if len(ans.message) == 0:
            toast('offer updated successfully')
            print('offer updated successfully')
        if ans.res is False:
            print("Bad Offer Update")
        return ans


    def update(self, first_name, last_name, email, phone_number, birth_date, gender):
        update_req = {'op': 5, 'first_name': first_name, 'last_name': last_name, 'email': email, 'phone_number':phone_number,
                      'birth_date':birth_date, 'gender':gender}
        self.req_answers.add_request(update_req)
        ans = self.req_answers.get_answer()
        if len(ans.message) == 0:
            print("User Details Updated Succesfully")
        else:
            print(ans.message)
        for ex in ans.message:
            toast(ex)
        changed_user = ans.data
        if ans.res is True:
            self.user_service = self.build_user(ans.data)

        return ans

    # def update_first_name(self, first_name):
    #     update_first_name_req = {'op': 5, 'first_name': first_name}
    #     self.req_answers.add_request(update_first_name_req)
    #     ans = self.req_answers.get_answer()
    #     return ans
    #
    # def update_last_name(self, last_name):
    #     update_last_name_req = {'op': 6, 'last_name': last_name}
    #     self.req_answers.add_request(update_last_name_req)
    #     ans = self.req_answers.get_answer()
    #     return ans
    #
    # def update_user_name(self, user_name):
    #     update_user_name_req = {'op': 7, 'user_name': user_name}
    #     self.req_answers.add_request(update_user_name_req)
    #     ans = self.req_answers.get_answer()
    #     return ans
    #
    # def update_email(self, email):
    #     update_email_req = {'op': 8, 'email': email}
    #     self.req_answers.add_request(update_email_req)
    #     ans = self.req_answers.get_answer()
    #     return ans
    #
    # def update_password(self, old_password, new_password):
    #     update_password_req = {'op': 37, 'old_password': old_password, 'new_password': new_password}
    #     self.req_answers.add_request(update_password_req)
    #     ans = self.req_answers.get_answer()
    #     return ans
    #
    # def update_birth_date(self, birth_date):
    #     update_birth_req = {'op': 9, 'birth_date': birth_date}
    #     self.req_answers.add_request(update_birth_req)
    #     ans = self.req_answers.get_answer()
    #     return ans
    #
    # def update_gender(self, gender):
    #     update_birth_req = {'op': 10, 'gender': gender}
    #     self.req_answers.add_request(update_birth_req)
    #     ans = self.req_answers.get_answer()
    #     return ans

    def add_address_details(self, city, street, zip_code, floor, apt):
        add_address_req = {'op': 11, 'city': city, 'street': street, 'zip_code': zip_code,
                           'floor': floor, 'apt': apt}
        self.req_answers.add_request(add_address_req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        if ans.res is True:
            self.user_service = self.build_user(ans.data)

        return ans
    def add_payment_method(self, credit_card_number, credit_card_exp_date, cvv, card_type, id):
        add_pay_req = {'op': 12, 'credit_card_number': credit_card_number,
                       'expire_date': credit_card_exp_date,
                       'cvv': cvv, 'card_type': card_type, 'id_number': id}
        self.req_answers.add_request(add_pay_req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        if ans.res is True:
            self.user_service = self.build_user(ans.data)

        return ans

    # ----------------- offer Window ----------------------------------------
    # ----- buyer methods ----------------------------------
    def add_liked_offer(self, offer_id):
        add_liked_offer_req = {'op': 25, 'offer_id': offer_id}
        self.req_answers.add_request(add_liked_offer_req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        if ans.res is True:
            self.user_service.liked_offers.append(offer_id)
        return ans

    def remove_liked_offer(self, offer_id):
        remove_liked_offer_req = {'op': 26, 'offer_id': offer_id}
        self.req_answers.add_request(remove_liked_offer_req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        if ans.res is True:
            self.user_service.liked_offers.remove(offer_id)
        return ans

    def add_active_buy_offer(self, offer_id, quantity, step, color, size, address):
        if address is None:
            address = self.user_service.get_address()
            if address.res is False:
                toast(address.message)
                return address
        add_active_buy_offer_req = {'op': 23,
                                    'offer_id': offer_id,
                                    'quantity': quantity,
                                    'step': step,
                                    'color': color,
                                    'size': size,
                                    'address':address}
        self.req_answers.add_request(add_active_buy_offer_req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        return ans

    def update_active_buy_offer(self, offer_id, quantity, step, color, size, address):
        add_active_buy_offer_req = {'op': 101,
                                    'offer_id': offer_id,
                                    'quantity': quantity,
                                    'step': step,
                                    'color': color,
                                    'size': size,
                                    'address':address}
        self.req_answers.add_request(add_active_buy_offer_req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        return ans

    def remove_active_buy_offer(self, offer_id):
        remove_act_buy_offer_req = {'op': 28, 'offer_id': offer_id}
        self.req_answers.add_request(remove_act_buy_offer_req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        return ans

    def add_active_sell_offer(self, name, company, colors, sizes, description, photos, category_name,
                              sub_category_name, steps, end_date):
        add_active_sell_offer_req = {'op': 24, 'name': name, 'company': company, 'colors': colors,
                                     'sizes': sizes, 'description': description, 'photos': photos,
                                     'category_name': category_name, 'sub_category_name': sub_category_name,
                                     'steps': steps, 'end_date': end_date}
        self.req_answers.add_request(add_active_sell_offer_req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        return ans

    def update_purchase(self, offer_id, quantity, step, color, size):
        req = {'op': 37, 'offer_id': offer_id, 'quantity': quantity, 'step': step, 'color': color, 'size': size}
        self.req_answers.add_request(req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        return ans

    # ----- seller methods ---------------------------------

    def remove_active_sell_offer(self, offer_id):
        remove_act_sell_offer_req = {'op': 27, 'offer_id': offer_id}
        self.req_answers.add_request(remove_act_sell_offer_req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        return ans

    def add_photo(self, offer_id, photo):
        add_photo_req = {'op': 31}
        self.req_answers.add_request(add_photo_req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        return ans

    def remove_photo(self, offer_id, photo):
        remove_photo_req = {'op': 34}
        self.req_answers.add_request(remove_photo_req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        return ans

    def update_end_date(self, offer_id, end_date):
        up_end_date_req = {'op': 39, 'offer_id': offer_id, 'end_date': end_date}
        self.req_answers.add_request(up_end_date_req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        return ans

    def update_step(self, offer_id, step):
        req = {'op': 41, 'offer_id': offer_id, 'step': step}
        self.req_answers.add_request(req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        return ans

    def update_product_name(self, offer_id, name):
        req = {'op': 42, 'offer_id': offer_id, 'name': name}
        self.req_answers.add_request(req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        return ans

    def update_product_company(self, offer_id, company):
        req = {'op': 43, 'offer_id': offer_id, 'company': company}
        self.req_answers.add_request(req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        return ans

    def update_product_colors(self, offer_id, colors):
        req = {'op': 44, 'offer_id': offer_id, 'colors': colors}
        self.req_answers.add_request(req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        return ans

    def update_product_sizes(self, offer_id, sizes):
        req = {'op': 45, 'offer_id': offer_id, 'sizes': sizes}
        self.req_answers.add_request(req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        return ans

    def update_product_description(self, offer_id, description):
        req = {'op': 46, 'offer_id': offer_id, 'description': description}
        self.req_answers.add_request(req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        return ans

    def update_sub_category_for_offer(self, offer_id, sub_category_name):
        up_sub_cat_for_offer_req = {'op': 38, 'offer_id': offer_id, 'sub_category_name': sub_category_name}
        self.req_answers.add_request(up_sub_cat_for_offer_req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        return ans

    def update_step_for_offer(self, offer_id, step_number, quantity, price):
        req = {'op': 54, 'offer_id': offer_id, 'step_number': step_number, 'quantity': quantity, 'price': price}
        self.req_answers.add_request(req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        return ans

    # ------------------------ search & getters methods ----------------------------

    def get_offers_by_category(self, category_name):
        offers = []
        req = {'op': 47, 'category_name': category_name}
        self.req_answers.add_request(req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        if ans.res is True:
            offers = self.build_offers_list(ans.data)
        else:
            print("bad search - offers_by_category")
        return offers

    def get_offers_by_sub_category(self, category_name, sub_category_name):
        offers = []
        req = {'op': 48, 'category_name': category_name, 'sub_category_name': sub_category_name}
        self.req_answers.add_request(req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        if ans.res is True:
            offers = self.build_offers_list(ans.data)
        else:
            print("bad search - offers_by_sub_category")
        return offers

    def get_offers_by_product_name(self, name):
        offers = []
        req = {'op': 49, 'name': name}
        self.req_answers.add_request(req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        if ans.res is True:
            offers = self.build_offers_list(ans.data)
        else:
            print("bad search - offers_by_product_name")
        return offers

    # def get_offers_by_status(self, status):
    #     offers = []
    #     req = {'op': 50, 'status': status}
    #     self.req_answers.add_request(req)
    #     ans = self.req_answers.get_answer()
    #     if ans.res is True:
    #         offers = self.build_offers_list(ans.data)
    #     else:
    #         print("bad search")
    #     return offers

    def get_hot_deals(self):
        offers = []
        req = {'op': 51}
        self.req_answers.add_request(req)
        # self.client.transport.write('req'.encode('utf8'))
        ans = self.req_answers.get_answer()
        print(ans.message)
        if ans.res is True:
            offers = self.build_offers_list(ans.data)
        else:
            print("bad search - hot_deals")
        return offers

    def get_all_history_buy_offers(self):
        offers = []
        req = {'op': 13}
        self.req_answers.add_request(req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        if ans.res is True:
            offers = self.build_offers_list(ans.data)
        else:
            print("bad search - all_history_buy_offers")
        return offers

    def get_all_history_sell_offers(self):
        offers = []
        req = {'op': 14}
        self.req_answers.add_request(req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        if ans.res is True:
            offers = self.build_offers_list(ans.data)
        else:
            print("bad search - all_history_sell_offers")
        return offers

    # def get_history_buy_offer(self, offer_id):
    #     req = {'op': 15, 'offer_id': offer_id}
    #     self.req_answers.add_request(req)
    #     ans = self.req_answers.get_answer()
    #     if ans.res is True:
    #         offer = self.build_offer(ans.data)
    #     else:
    #         print("bad search")
    #     return offer
    #
    # def get_history_sell_offer(self, offer_id):
    #     req = {'op': 16, 'offer_id': offer_id}
    #     self.req_answers.add_request(req)
    #     ans = self.req_answers.get_answer()
    #     if ans.res is True:
    #         offer = self.build_offer(ans.data)
    #     else:
    #         print("bad search")
    #     return offer

    def get_all_active_buy_offers(self):
        offers = []
        req = {'op': 17}
        self.req_answers.add_request(req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        if ans.res is True:
            offers = self.build_offers_list(ans.data)
        else:
            print("bad search - all_active_buy_offers")
        return offers

    def get_all_active_sell_offers(self):
        offers = []
        req = {'op': 18}
        self.req_answers.add_request(req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        if ans.res is True:
            offers = self.build_offers_list(ans.data)
        else:
            print("bad search - all_active_sell_offers")
        return offers

    # def get_active_buy_offer(self, offer_id):
    #     req = {'op': 19, 'offer_id': offer_id}
    #     self.req_answers.add_request(req)
    #     ans = self.req_answers.get_answer()
    #     if ans.res is True:
    #         offer = self.build_offer(ans.data)
    #     else:
    #         print("bad search")
    #     return offer
    #
    # def get_active_sell_offer(self, offer_id):
    #     req = {'op': 20, 'offer_id': offer_id}
    #     self.req_answers.add_request(req)
    #     ans = self.req_answers.get_answer()
    #     if ans.res is True:
    #         offer = self.build_offer(ans.data)
    #     else:
    #         print("bad search")
    #     return offer
    #
    # def get_liked_offer(self, offer_id):
    #     req = {'op': 21, 'offer_id': offer_id}
    #     self.req_answers.add_request(req)
    #     ans = self.req_answers.get_answer()
    #     if ans.res is True:
    #         offer = self.build_offer(ans.data)
    #     else:
    #         print("bad search")
    #     return offer

    def get_all_liked_offers(self):
        offers = []
        req = {'op': 22}
        self.req_answers.add_request(req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        if ans.res is True:
            offers = self.build_offers_list(ans.data)
        else:
            print("bad search")
        return offers

    # ------------------- Admin Functions ---------------------------------------------------------------------

    def add_to_hot_deals(self, offer_id):
        req = {'op': 52, 'offer_id': offer_id}
        self.req_answers.add_request(req)
        ans = self.req_answers.get_answer()
        return ans

    def remove_from_hot_deals(self, offer_id):
        req = {'op': 53, 'offer_id': offer_id}
        self.req_answers.add_request(req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        return ans

    def update_start_date(self, offer_id, start_date):
        req = {'op': 40, 'offer_id': offer_id, 'start_date': start_date}
        self.req_answers.add_request(req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        return ans

    def update_category_name(self, category_name, name):
        up_cat_name_req = {'op': 35, 'category_name': category_name, 'name': name}
        self.req_answers.add_request(up_cat_name_req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        return ans

    def update_sub_category_name(self, category_name, sub_category_name, name):
        up_sub_cat_name_req = {'op': 36, 'category_name': category_name, 'sub_category_name': sub_category_name,
                               'name': name}
        self.req_answers.add_request(up_sub_cat_name_req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        return ans

    def remove_category(self, category_name):
        remove_cat_req = {'op': 32, 'category_name': category_name}
        self.req_answers.add_request(remove_cat_req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        return ans

    def remove_sub_category(self, category_name, sub_category_name):
        remove_sub_cat_req = {'op': 33, 'category_name': category_name, 'sub_category_name': sub_category_name}
        self.req_answers.add_request(remove_sub_cat_req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        return ans

    def add_category(self, name):
        add_cat_req = {'op': 29, 'name': name}
        self.req_answers.add_request(add_cat_req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        return ans

    def add_sub_category(self, name, category_name):
        add_sub_cat_req = {'op': 30, 'name': name, 'category_name': category_name}
        self.req_answers.add_request(add_sub_cat_req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        return ans

    def complete_register(self, code, email):
        complete_register_req = {'op': 81, 'code': int(code), 'email':email}
        self.req_answers.add_request(complete_register_req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        return ans

    def become_a_seller(self,email):
        complete_register_req = {'op': 100, 'email':email}
        self.req_answers.add_request(complete_register_req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        return ans

    def get_offers_by_product_company(self, company):
        offers = []
        req = {'op': 99, 'company': company}
        self.req_answers.add_request(req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        if ans.res is True:
            offers = self.build_offers_list(ans.data)
        else:
            print("bad search - offers_by_product_company")
        return offers

    def contact_us(self, subject, description):
        req = {'op': 94, 'subject': subject, 'description': description}
        self.req_answers.add_request(req)
        ans = self.req_answers.get_answer()
        return ans

    def exit(self):
        self.logout()
        exit_req = {'op': 55}
        self.req_answers.add_request(exit_req)
        ans = self.req_answers.get_answer()
        print(ans.message)
        return ans

    # ------------------------------- private methods

    def build_offers_list(self, data):
        offers = []
        for x in data:
            offer_temp = OfferService(x['offer_id'], x['user_id'], x['product'], x['category_id'], x['sub_category_id'],
                                      x['status'],
                                      x['steps'], x['start_date'], x['end_date'], x['current_step'],
                                      x['current_buyers'])

            offers.append(offer_temp)
        return offers

    def build_offer(self, x):
        offer_temp = OfferService(x['offer_id'], x['user_id'], x['product'], x['category_id'], x['sub_category_id'],
                                  x['status'],
                                  x['steps'], x['start_date'], x['end_date'], x['current_step'],
                                  x['current_buyers'], x['category_name'], x['sub_category_name'])
        return offer_temp

    def build_user(self, data):
        birth_date = data['birth_date']
        length= len(data['birth_date'])-1
        birth =  birth_date[1:length]
        user_temp = UserService(data['user_id'], data['first_name'], data['last_name'], data['phone'], data['email'],
                                data['password'], birth, data['gender'], data['seller'], data['city'],
                                data['street'], data['apartment_number'], data['zip_code'], data['floor'],
                                data['id_number'], data['credit_card_number'], data['credit_card_exp_date'], data['cvv'],
                                data['card_type'],
                                data['history_buy_offers'], data['history_sell_offers'], data['liked_offers'], data['active_sell_offers'],
                                data['active_buy_offers'],)
        return user_temp

    def get_user_service(self):
        return self.user_service


