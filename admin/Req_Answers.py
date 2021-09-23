from queue import Queue



class Req_Answers:
    def __init__(self):
        # encoded queues !
        x = 5
        self.requests_queue = Queue()
        self.answers_queue = Queue()

    def add_request(self, req):
        self.requests_queue.put(req)
        x = 5

    def add_answer(self, answer):
        self.answers_queue.put(answer)
        a=9

    def get_answer(self):
        return self.answers_queue.get()

    def get_request(self):
        return self.requests_queue.get()
