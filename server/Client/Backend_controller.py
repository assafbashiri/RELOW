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
        # adding to the queue, and the Main-Thread should send them to the server
        self.req_answers.add_request(register_req)
        # waiting for an answer from the server to the Main-Thread, and for the Main_thread adding the answer to the queue
        ans = self.req_answers.get_answer()
        return ans
"""
    def unregister(self, user_id):
        unregister_req = {'op': 2, 'user_id': user_id}
        self.queue.add(unregister_req)
        ans = self.queue.get()
        return ans

    def login(self, user_name, password):
        login_req = {'op': 3, 'user_name': user_name, 'password': password}
        self.queue.add(login_req)
        ans = self.queue.get()
        return ans

    def logout(self, user_id):
        logout_req = {'op': 4, 'user_id': user_id}
        self.queue.add(logout_req)
        ans = self.queue.get()
        return ans

    def update_first_name(self, user_id, first_name):
        update_first_name_req = {'op': 5, 'user_id': user_id, 'first_name': first_name}
        self.queue.add(update_first_name_req)
        ans = self.queue.get()
        return ans

    def update_last_name(self, user_id, last_name):
        update_last_name_req = {'op': 6, 'user_id': user_id, 'last_name': last_name}
        self.queue.add(update_last_name_req)
        ans = self.queue.get()
        return ans

    def update_user_name(self, user_id, user_name):
        update_user_name_req = {'op': 7, 'user_id': user_id, 'user_name': user_name}
        self.queue.add(update_user_name_req)
        ans = self.queue.get()
        return ans

    def update_email(self, user_id, email):
        update_email_req = {'op': 8, 'user_id': user_id, 'email': email}
        self.queue.add(update_email_req)
        ans = self.queue.get()
        return ans

    # not in the handler - have to add there
    def update_password(self, user_id, old_password, new_password):
        update_password_req = {'op': 195, 'user_id': user_id, 'old_password': old_password, 'new_password': new_password}
        self.queue.add(update_password_req)
        ans = self.queue.get()
        return ans

    def update_birth_date(self, user_id, birth_date):
        update_birth_req = {'op': 9, 'user_id': user_id, 'birth_date': birth_date}
        self.queue.add(update_birth_req)
        ans = self.queue.get()
        return ans

    def update_gender(self, user_id, gender):
        update_birth_req = {'op': 10, 'user_id': user_id, 'gender': gender}
        self.queue.add(update_birth_req)
        ans = self.queue.get()
        return ans

    def add_address_details(self, user_id, city, street, zip_code, floor, apt):
        add_address_req = {'op': 11, 'user_id': user_id, 'city': city, 'street': street, 'zip_code': zip_code, 'floor': floor, 'apt': apt}
        self.queue.add(add_address_req)
        ans = self.queue.get()
        return ans

    def add_payment_method(self, user_id, credit_card_number, credit_card_exp_date, cvv, card_type, id):
        add_pay_req = {'op': 12,'user_id': user_id,  'credit_card_number': credit_card_number, 'expire_date': credit_card_exp_date,
                       'cvv': cvv, 'card_type': card_type, 'id_number': id}
        self.queue.add(add_pay_req)
        ans = self.queue.get()
        return ans"""