
class Response:
    def __init__(self, data, message, res):
        self.data = data
        self.message = message
        self.res = res

    def get_data(self):
        return self.data

    def get_response(self):
        return self.res

    def get_message(self):
        return self.message

    def set_data(self, data):
        self.data = data

    def set_response(self, res):
        self.res = res

    def set_message(self, message):
        self.message = message
