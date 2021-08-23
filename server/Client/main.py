import socket
import pickle
import kivy
from kivy.app import App
from kivy.storage.jsonstore import JsonStore
import threading

from TestUp import TestApp
from Req_Answers import Req_Answers

from Backend_controller import Backend_controller
from Decoder import Decoder


class Struct(object):
    def __init__(self, **entries):
        self.__dict__.update(entries)


store = JsonStore('hello.json')
req_answers = Req_Answers()
controller = Backend_controller(req_answers)


def start_gui():
    print("start thread work")



def network():
    # --------------- connect to Server ---------------------------------
    print("start thread work")
    ClientSocket = socket.socket()
    host = '127.0.0.1'
    port = 4000
    print('Waiting for connection')
    try:
        ClientSocket.connect((host, port))
    except socket.error as e:
        print(str(e))

    # response = ClientSocket.recv(1024)
    # response1 = pickle.loads(response)
    # print(response1)


    # --------------- init the fields ---------------------------------



    # main Window as a Thread
    # mainWindow = MainWindow()

    decoder = Decoder()
    print("amit")
    while True:
        to_send = req_answers.get_answer()
        print(to_send, 'step 11111\n')
        message = pickle.dumps(to_send)
        print(message, 'step 2\n')

        ClientSocket.send(message)
        if to_send['op'] == 2:
            print("bey bey")
            ClientSocket.close()
            App.get_running_app().stop()
            break
        elif to_send['op'] == 4:
            print("bey bey")
            ClientSocket.close()
            break
        # send to server - done
        ans = ClientSocket.recv(1024)
        print(ans, "step 3")
        # ans1 = pickle.loads(ans)
        # res = Response(ans1['data'], ans1['message'], ans1['res'])
        print(type(ans))
        # if ans1['res'] is True:
        #     store.put('user', us='david')
        #     print("yes baby")
        # App.get_running_app().stop()
        decoded_ans = pickle.loads(ans)

        req_answers.add_answer(decoded_ans)
        print("bolobolo")


def ex():
    App.get_running_app().stop()

if __name__ == '__main__':
    t1 = threading.Thread(target=network)
    t1.start()
    TestApp(req_answers, controller).run()



