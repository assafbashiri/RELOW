

class response:
    def __init__(self):
        self.data = None
        self.res = None

    def get_data(self):
        return self.data

    def get_response(self):
        return self.res

    def set_data(self, data):
        self.data = data

    def set_response(self,res):
        self.res = res