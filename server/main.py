import socket
import sqlite3
import threading
from _thread import *
import pickle
from Service import protocol
from DB.Repository import repository
class Struct(object):
    def __init__(self, **entries):
        self.__dict__.update(entries)

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
p1 = point(1,2)

def network():
    ServerSocket = socket.socket()
    host = '127.0.0.1'
    port = 1233
    ThreadCount = 0
    try:
        ServerSocket.bind((host, port))
    except socket.error as e:
        print(str(e))

    print('Waitiing for a Connection..')
    ServerSocket.listen(5)

    def threaded_client(connection):
        opening = 'Welcome to the Servern'
        step1 = pickle.dumps(opening)
        print(step1)
        connection.send(step1)
        while True:
            data = connection.recv(2048)
            data1 = pickle.loads(data)
            print(type(data1), data1)
            # reply = 'Server Says: ' + data1
            if not data:
                break
            res = protocol.hendeling(data1)
            a = vars(res)
            b = pickle.dumps(a)
            connection.sendall(b)
        connection.close()

    while True:
        Client, address = ServerSocket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        start_new_thread(threaded_client, (Client,))
        ThreadCount += 1
        print('Thread Number: ' + str(ThreadCount))
    ServerSocket.close()


if __name__ == '__main__':
    conn = sqlite3.connect('database.db')
    repository = repository(conn)
    repository.create_tables()
    print('boo')
    t1 = threading.Thread(target=network)
    t1.start()