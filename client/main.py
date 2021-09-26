import socket
import pickle
import urllib
import urllib3
from Utils.CheckValidity import CheckValidity
from kivy.app import App
import threading
from kivymd.toast import toast
from kivy.lang import Builder
from twisted.internet import reactor, protocol
import googlemaps
import pprint
import time
import urllib
from geosky import geo_plug
import ast
import json
import requests
from Backend_controller import Backend_controller
from Req_Answers import Req_Answers
from kivy.storage.jsonstore import JsonStore
# from Backend_controller import Backend_controller
from windows.mainWindow import TestApp


class Struct(object):
    def __init__(self, **entries):
        self.__dict__.update(entries)

class OurClient(protocol.Protocol):
    """Once connected, send a message, then print the result."""

    def connectionMade(self):
        self.transport.write(b"hello, world!")

    def dataReceived(self, data):
        to_send = req_answers.get_request()
        message = pickle.dumps(to_send)
        print(message.message, 'step 2\n')

        self.transport.write.send(message)
        decoded_ans = Struct(**(pickle.loads("ans")))
        if decoded_ans.message == 'EXIT':
            ex()
            req_answers.add_answer(decoded_ans)
            return
        req_answers.add_answer(decoded_ans)

    def connectionLost(self, reason):
        print("connection lost")


class OurFactory(protocol.ClientFactory):
    protocol = OurClient

    def clientConnectionFailed(self, connector, reason):
        print("Connection failed - goodbye!")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("Connection lost - goodbye!")
        reactor.stop()



def net():
    f = OurFactory()
    reactor.connectTCP("129.168.1.19", 4000, f)
    reactor.run()


def network(**kwargs):
    # --------------- connect to Server ---------------------------------
    print(kwargs['arg1'])
    print("start thread work")
    ClientSocket = socket.socket()
    host =  '127.0.0.1' #'192.168.1.19'
    port = 4000
    print('Waiting for connection..')
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

    while True:
        to_send = req_answers.get_request()
        message = pickle.dumps(to_send)

        a = ClientSocket.send(message)
        b = 9
        # if to_send['op'] == 2:
        #     ClientSocket.close()2169-+





        #     App.get_running_app().stop()
        #     break
        BUFF_SIZE = 10000  # 4 KiB
        data = b''
        while True:
            part = ClientSocket.recv(BUFF_SIZE)
            data += part
            if len(part) < BUFF_SIZE:
                # either 0 or end of data
                break
        decoded_ans = Struct(**(pickle.loads(data)))
        print(decoded_ans.message)
        if decoded_ans.message == 'EXIT':

            ex()
            req_answers.add_answer(decoded_ans)
            return
        req_answers.add_answer(decoded_ans)


def ex():
    App.get_running_app().stop()

if __name__ == '__main__':

    # a = geo_plug.all_CountryNames()
    #
    # b = geo_plug.all_Country_StateNames()
    #
    # # json_acceptable_string = b.replace("'", "\"")
    # ddd = json.loads(b)
    # # eee = json.loads(a)
    # c = geo_plug.all_State_CityNames('United States')  # name == 'all' or state name
    # d = geo_plug.all_State_CityNames('Odisha')
    # #########################################################################################
    #
    # overpass_url = "http://overpass-api.de/api/interpreter"
    # overpass_query = """
    #        [out:json];
    #        area["ISO3166-1"="IN"];
    #        (rel(area)["admin_level"="4"];);
    #        out;
    #        """
    api_key = 'AIzaSyA1Hxe3DlRQ1eLilFyaPZib3NObI_6a8zo'
    gmaps = googlemaps.Client(key = api_key)
    #place_result = gmaps.places_nearby(location = '-33.8676522, 151.1957362', radius =40000, open_now=False,type='country')
    response = requests.get(
        'https://maps.googleapis.com/maps/api/place/autocomplete/json?input=Israel&key=AIzaSyA1Hxe3DlRQ1eLilFyaPZib3NObI_6a8zo')
    data = json.loads(response.text)



    url11 = 'https://data.gov.il/api/3/action/datastore_search?resource_id=1b14e41c-85b3-4c21-bdce-9fe48185ffca&limit=5'

    a=0
    # # # for elem in data['data']:
    # # #     if elem['country'] not in cities.keys():
    # # #         cities[elem['country']] = []
    # # #         cities[elem['country']].append(elem['city'])
    # # #     else:
    # # #         cities[elem['country']].append(elem['city'])
    # # api_key = 'AIzaSyCh7ZdQOIiQjCQyWyDMY9yudUj1WzOYZRg'
    # # url = "https://maps.googleapis.com/maps/api/place/details/json?place_id=ChIJN1t_tDeuEmsRUsoyG83frY4&fields=name%2Crating%2Cformatted_phone_number&key=YOUR_API_KEY"
    # #
    # # payload = {}
    # # headers = {}
    # #
    # # response = requests.request("GET", url, headers=headers, data=payload)
    # #print(response.text)
    # #--------------------------------------------------------------------------------------------------------------------------------
    #
    # print(data['error_message'])
    # url_countries = 'https://parseapi.back4app.com/classes/Country?limit=10000&order=name&keys=name'
    # headers = {
    #     'X-Parse-Application-Id': 'mxsebv4KoWIGkRntXwyzg6c6DhKWQuit8Ry9sHja',  # This is the fake app's application id
    #     'X-Parse-Master-Key': 'TpO0j3lG2PmEVMXlKYQACoOXKQrL3lwM0HwR9dbH'  # This is the fake app's readonly master key
    # }
    # data_countries = json.loads(
    #     requests.get(url_countries, headers=headers).content.decode('utf-8'))  # Here you have the data that you need
    #
    # url_cities = 'https://parseapi.back4app.com/classes/City?limit=10000&order=name&keys=name,country'
    # headers = {
    #     'X-Parse-Application-Id': 'mxsebv4KoWIGkRntXwyzg6c6DhKWQuit8Ry9sHja',  # This is the fake app's application id
    #     'X-Parse-Master-Key': 'TpO0j3lG2PmEVMXlKYQACoOXKQrL3lwM0HwR9dbH'  # This is the fake app's readonly master key
    # }
    # data_cities = json.loads(
    #     requests.get(url_cities, headers=headers).content.decode('utf-8'))  # Here you have the data that you need
    # print(json.dumps(data_countries, indent=2))
    # print(json.dumps(data_cities, indent=2))
    # #--------------------------------------------------------------------------------------------------------------------------------
    # #4IBFb6Wpq5
    # list = []
    # for a in data_cities['results']:
    #     if a['country']['objectId'] == 'BXkZTI2omc':
    #         list.append(a.name)
    #
    # where = urllib.parse.quote_plus("""
    # {
    #     "country": {
    #         "__type": "Pointer",
    #         "className": "Country",
    #         "objectId": "Israel"
    #     }
    # }
    # """)
    # url = 'https://parseapi.back4app.com/classes/City?limit=10&keys=name,country&where=%s' % where
    # headers = {
    #     'X-Parse-Application-Id': 'mxsebv4KoWIGkRntXwyzg6c6DhKWQuit8Ry9sHja',  # This is the fake app's application id
    #     'X-Parse-Master-Key': 'TpO0j3lG2PmEVMXlKYQACoOXKQrL3lwM0HwR9dbH'  # This is the fake app's readonly master key
    # }
    address_dict = {}
    data = json.loads(
    requests.get('https://data.gov.il/api/3/action/datastore_search?resource_id=1b14e41c-85b3-4c21-bdce-9fe48185ffca&limit=116621').text ) # Here you have the data that you need
    for d in data['result']['records']:
        region = d['region_name']
        city = d['city_name']
        street = d['street_name']
        if region not in address_dict.keys():
            address_dict[region] = {}
        if city not in address_dict[region].keys():
            address_dict[region][city]=[]
        address_dict[region][city].append(street)
    a=0

    #BXkZTI2omc\
    s ="kljlh"
    b=s[::-1]
    Builder.load_file('windows/mainWindow.kv')
    Builder.load_file('windows/managerWindow.kv')
    Builder.load_file('windows/connectWindow.kv')
    Builder.load_file('windows/accountWindow.kv')
    Builder.load_file('windows/searchWindow.kv')
    Builder.load_file('windows/addofferWindow.kv')
    Builder.load_file('windows/updateOfferWindow.kv')
    Builder.load_file('windows/registerWindow.kv')
    Builder.load_file('windows/loginWindow.kv')
    Builder.load_file('windows/offers_list.kv')
    Builder.load_file('windows/my_offersWindow.kv')
    Builder.load_file('windows/confirmationWindow.kv')
    Builder.load_file('windows/contactWindow.kv')
    store = JsonStore('hello.json')
    a = OurClient()
    req_answers = Req_Answers()
    t1 = threading.Thread(target=lambda:network(arg1=a))
    t1.start()
    controller = Backend_controller(req_answers, store, a)
    TestApp(controller).run()



