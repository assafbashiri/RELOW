class UserPayment:
    def __init__(self):
        self.id_number = None
        self.credit_card_number = None
        self.credit_card_exp_date = None
        self.cvv = None
        self.card_type = None

    def add_card_details(self, id, credit_card_number, credit_card_exp_date, cvv, card_type):
        self.id_number = id
        self.credit_card_number = credit_card_number
        self.credit_card_exp_date = credit_card_exp_date
        self.cvv = cvv
        self.card_type = card_type

    def set_credit_card_number(self, credit_card_number):
        self.credit_card_number = credit_card_number

    def set_credit_card_exp_date(self, credit_card_exp_date):
        self.credit_card_exp_date = credit_card_exp_date

    def set_cvv(self, cvv):
        self.cvv = cvv

    def set_card_type(self, card_type):
        self.card_type = card_type

    def set_id_number(self, id_number):
        self.id_number = id_number

    def get_card_number(self):
        return self.credit_card_number

    def get_credit_card_exp_date(self):
        return self.credit_card_exp_date

    def get_cvv(self):
        return self.cvv

    def get_id_number(self):
        return self.id_number

    def get_card_type(self):
        return self.card_type