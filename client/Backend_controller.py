class Backend_controller:
    def __init__(self, req_answers):
        self.req_answers = req_answers
        # user / categories DATA
        self.user_service = None
        self.hot_deals = None
        self.categories = None

    def register(self, first_name, last_name, user_name, email, password, birth_date, gender):
        print("register")
        # encode the request for Server-Language
        register_req = {
            'op': 1, 'first_name': first_name, 'last_name': last_name, 'user_name': user_name,
            'email': email, 'password': password, 'birth_date': birth_date, 'gender': gender
        }
        # adding to the req_answers, and the Main-Thread should send them to the server
        self.req_answers.add_request(register_req)
        # waiting for an answer from the server to the Main-Thread, and for the Main_thread adding the answer to the
        # req_answers
        ans = self.req_answers.get_answer()
        return ans

    def unregister(self, user_id):
        unregister_req = {'op': 2, 'user_id': user_id}
        self.req_answers.add_request(unregister_req)
        ans = self.req_answers.get_answer()
        return ans

    def login(self, user_name, password):
        login_req = {'op': 3, 'user_name': user_name, 'password': password}
        self.req_answers.add_request(login_req)
        ans = self.req_answers.get_answer()
        return ans

    def logout(self, user_id):
        logout_req = {'op': 4, 'user_id': user_id}
        self.req_answers.add_request(logout_req)
        ans = self.req_answers.get_answer()
        return ans

    def update_first_name(self, user_id, first_name):
        update_first_name_req = {'op': 5, 'user_id': user_id, 'first_name': first_name}
        self.req_answers.add_request(update_first_name_req)
        ans = self.req_answers.get_answer()
        return ans

    def update_last_name(self, user_id, last_name):
        update_last_name_req = {'op': 6, 'user_id': user_id, 'last_name': last_name}
        self.req_answers.add_request(update_last_name_req)
        ans = self.req_answers.get_answer()
        return ans

    def update_user_name(self, user_id, user_name):
        update_user_name_req = {'op': 7, 'user_id': user_id, 'user_name': user_name}
        self.req_answers.add_request(update_user_name_req)
        ans = self.req_answers.get_answer()
        return ans

    def update_email(self, user_id, email):
        update_email_req = {'op': 8, 'user_id': user_id, 'email': email}
        self.req_answers.add_request(update_email_req)
        ans = self.req_answers.get_answer()
        return ans

    def update_password(self, user_id, old_password, new_password):
        update_password_req = {'op': 37, 'user_id': user_id, 'old_password': old_password, 'new_password': new_password}
        self.req_answers.add_request(update_password_req)
        ans = self.req_answers.get_answer()
        return ans

    def update_birth_date(self, user_id, birth_date):
        update_birth_req = {'op': 9, 'user_id': user_id, 'birth_date': birth_date}
        self.req_answers.add_request(update_birth_req)
        ans = self.req_answers.get_answer()
        return ans

    def update_gender(self, user_id, gender):
        update_birth_req = {'op': 10, 'user_id': user_id, 'gender': gender}
        self.req_answers.add_request(update_birth_req)
        ans = self.req_answers.get_answer()
        return ans

    def add_address_details(self, user_id, city, street, zip_code, floor, apt):
        add_address_req = {'op': 11, 'user_id': user_id, 'city': city, 'street': street, 'zip_code': zip_code,
                           'floor': floor, 'apt': apt}
        self.req_answers.add_request(add_address_req)
        ans = self.req_answers.get_answer()
        return ans

    def add_payment_method(self, user_id, credit_card_number, credit_card_exp_date, cvv, card_type, id):
        add_pay_req = {'op': 12, 'user_id': user_id, 'credit_card_number': credit_card_number,
                       'expire_date': credit_card_exp_date,
                       'cvv': cvv, 'card_type': card_type, 'id_number': id}
        self.req_answers.add_request(add_pay_req)
        ans = self.req_answers.get_answer()
        return ans

    def get_all_history_buy_offers(self):
        get_his_buy_offers_req = {'op': 13}
        self.req_answers.add_request(get_his_buy_offers_req)
        ans = self.req_answers.get_answer()
        return ans

    def get_all_history_sell_offers(self):
        get_his_sell_offers_req = {'op': 14}
        self.req_answers.add_request(get_his_sell_offers_req)
        ans = self.req_answers.get_answer()
        return ans

    def get_history_buy_offer(self, offer_id):
        get_his_buy_offer_req = {'op': 15, 'offer_id': offer_id}
        self.req_answers.add_request(get_his_buy_offer_req)
        ans = self.req_answers.get_answer()
        return ans

    def get_history_sell_offer(self, offer_id):
        get_his_sell_offer_req = {'op': 16, 'offer_id': offer_id}
        self.req_answers.add_request(get_his_sell_offer_req)
        ans = self.req_answers.get_answer()
        return ans

    def get_all_active_buy_offers(self):
        get_act_buy_offers_req = {'op': 17}
        self.req_answers.add_request(get_act_buy_offers_req)
        ans = self.req_answers.get_answer()
        return ans

    def get_all_active_sell_offers(self):
        get_act_sell_offers_req = {'op': 18}
        self.req_answers.add_request(get_act_sell_offers_req)
        ans = self.req_answers.get_answer()
        return ans

    def get_active_buy_offer(self, offer_id):
        get_act_buy_offer_req = {'op': 19, 'offer_id': offer_id}
        self.req_answers.add_request(get_act_buy_offer_req)
        ans = self.req_answers.get_answer()
        return ans

    def get_active_sell_offer(self, offer_id):
        get_act_sell_offer_req = {'op': 20, 'offer_id': offer_id}
        self.req_answers.add_request(get_act_sell_offer_req)
        ans = self.req_answers.get_answer()
        return ans

    def get_liked_offer(self, offer_id):
        get_liked_offer_req = {'op': 21, 'offer_id': offer_id}
        self.req_answers.add_request(get_liked_offer_req)
        ans = self.req_answers.get_answer()
        return ans

    def get_all_liked_offers(self):
        get_liked_offers_req = {'op': 22}
        self.req_answers.add_request(get_liked_offers_req)
        ans = self.req_answers.get_answer()
        return ans

    def add_active_buy_offer(self, offer_id, quantity, step):
        add_active_buy_offer_req = {'op': 23, 'offer_id': offer_id, 'quantity': quantity, 'step': step}
        self.req_answers.add_request(add_active_buy_offer_req)
        ans = self.req_answers.get_answer()
        return ans

    def add_active_sell_offer(self, user_id, name, company, color, size, description, photos, category_id,
                              sub_category_id, steps, end_date):
        add_active_sell_offer_req = {'op': 24, 'user_id': user_id, 'name': name, 'company': company, 'color': color,
                                     'size': size, 'description': description, 'photos': photos,
                                     'category_id': category_id, 'sub_category_id': sub_category_id,
                                     'steps': steps, 'end_date': end_date}
        self.req_answers.add_request(add_active_sell_offer_req)
        ans = self.req_answers.get_answer()
        return ans

    def add_liked_offer(self, offer_id):
        add_liked_offer_req = {'op': 25, 'offer_id': offer_id}
        self.req_answers.add_request(add_liked_offer_req)
        ans = self.req_answers.get_answer()
        return ans

    def remove_liked_offer(self, offer_id):
        remove_liked_offer_req = {'op': 26, 'offer_id': offer_id}
        self.req_answers.add_request(remove_liked_offer_req)
        ans = self.req_answers.get_answer()
        return ans

    def remove_active_sell_offer(self, offer_id):
        remove_act_sell_offer_req = {'op': 27, 'offer_id': offer_id}
        self.req_answers.add_request(remove_act_sell_offer_req)
        ans = self.req_answers.get_answer()
        return ans

    def remove_active_buy_offer(self, offer_id):
        remove_act_buy_offer_req = {'op': 28, 'offer_id': offer_id}
        self.req_answers.add_request(remove_act_buy_offer_req)
        ans = self.req_answers.get_answer()
        return ans

    def add_category(self, name):
        add_cat_req = {'op': 29, 'name': name}
        self.req_answers.add_request(add_cat_req)
        ans = self.req_answers.get_answer()
        return ans

    def add_sub_category(self, name, category_id):
        add_sub_cat_req = {'op': 30, 'name': name, 'category_id': category_id}
        self.req_answers.add_request(add_sub_cat_req)
        ans = self.req_answers.get_answer()
        return ans

    def add_photo(self, photo):
        add_photo_req = {'op': 31}
        self.req_answers.add_request(add_photo_req)
        ans = self.req_answers.get_answer()
        return ans

    def remove_category(self, category_id):
        remove_cat_req = {'op': 32, 'category_id': category_id}
        self.req_answers.add_request(remove_cat_req)
        ans = self.req_answers.get_answer()
        return ans

    def remove_sub_category(self, category_id, sub_category_id):
        remove_sub_cat_req = {'op': 33, 'category_id': category_id, 'sub_category_id': sub_category_id}
        self.req_answers.add_request(remove_sub_cat_req)
        ans = self.req_answers.get_answer()
        return ans

    def remove_photo(self, photo):
        remove_photo_req = {'op': 34}
        self.req_answers.add_request(remove_photo_req)
        ans = self.req_answers.get_answer()
        return ans

    def update_category_name(self, category_id, name):
        up_cat_name_req = {'op': 35, 'category_id': category_id, 'name': name}
        self.req_answers.add_request(up_cat_name_req)
        ans = self.req_answers.get_answer()
        return ans

    def update_sub_category_name(self, category_id, sub_category_id, name):
        up_sub_cat_name_req = {'op': 36, 'category_id': category_id, 'sub_category_id': sub_category_id, 'name': name}
        self.req_answers.add_request(up_sub_cat_name_req)
        ans = self.req_answers.get_answer()
        return ans



    def update_sub_category_for_offer(self, offer_id, sub_category_id):
        up_sub_cat_for_offer_req = {'op': 38, 'offer_id': offer_id, 'sub_category_id': sub_category_id}
        self.req_answers.add_request(up_sub_cat_for_offer_req)
        ans = self.req_answers.get_answer()
        return ans

    def update_end_date(self, offer_id, end_date):
        up_end_date_req = {'op': 39, 'offer_id': offer_id, 'end_date': end_date}
        self.req_answers.add_request(up_end_date_req)
        ans = self.req_answers.get_answer()
        return ans

    def update_start_date(self, offer_id, start_date):
        req = {'op': 40, 'offer_id': offer_id, 'start_date': start_date}
        self.req_answers.add_request(req)
        ans = self.req_answers.get_answer()
        return ans

    def update_step(self, offer_id, step):
        req = {'op': 41, 'offer_id': offer_id, 'step': step}
        self.req_answers.add_request(req)
        ans = self.req_answers.get_answer()
        return ans

    def update_product_name(self, offer_id, name):
        req = {'op': 42, 'offer_id': offer_id, 'name': name}
        self.req_answers.add_request(req)
        ans = self.req_answers.get_answer()
        return ans

    def update_product_company(self, offer_id, company):
        req = {'op': 43, 'offer_id': offer_id, 'company': company}
        self.req_answers.add_request(req)
        ans = self.req_answers.get_answer()
        return ans

    def update_product_color(self, offer_id, color):
        req = {'op': 44, 'offer_id': offer_id, 'color': color}
        self.req_answers.add_request(req)
        ans = self.req_answers.get_answer()
        return ans

    def update_product_size(self, offer_id, size):
        req = {'op': 45, 'offer_id': offer_id, 'size': size}
        self.req_answers.add_request(req)
        ans = self.req_answers.get_answer()
        return ans

    def update_product_description(self, offer_id, description):
        req = {'op': 46, 'offer_id': offer_id, 'description': description}
        self.req_answers.add_request(req)
        ans = self.req_answers.get_answer()
        return ans

    def get_offers_by_category(self, category_id):
        req = {'op': 47, 'category_id': category_id}
        self.req_answers.add_request(req)
        ans = self.req_answers.get_answer()
        return ans

    def get_offers_by_sub_category(self, category_id, sub_category_id):
        req = {'op': 48, 'category_id': category_id, 'sub_category_id': sub_category_id}
        self.req_answers.add_request(req)
        ans = self.req_answers.get_answer()
        return ans

    def get_offers_by_product_name(self, name):
        req = {'op': 49, 'name': name}
        self.req_answers.add_request(req)
        ans = self.req_answers.get_answer()
        return ans

    def get_offers_by_status(self, status):
        req = {'op': 50, 'status': status}
        self.req_answers.add_request(req)
        ans = self.req_answers.get_answer()
        return ans

    def get_hot_deals(self):
        req = {'op': 51}
        self.req_answers.add_request(req)
        ans = self.req_answers.get_answer()
        return ans

    def add_to_hot_deals(self, offer_id):
        req = {'op': 52, 'offer_id': offer_id}
        self.req_answers.add_request(req)
        ans = self.req_answers.get_answer()
        return ans

    def remove_from_hot_deals(self, offer_id):
        req = {'op': 53, 'offer_id': offer_id}
        self.req_answers.add_request(req)
        ans = self.req_answers.get_answer()
        return ans

    def update_step_for_offer(self, offer_id, step_number, quantity, price):
        req = {'op': 54, 'offer_id': offer_id, 'step_number': step_number, 'quantity': quantity, 'price': price}
        self.req_answers.add_request(req)
        ans = self.req_answers.get_answer()
        return ans