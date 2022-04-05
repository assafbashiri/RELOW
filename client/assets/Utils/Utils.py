from datetime import datetime
import time
import requests
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.button import Button
# from fpdf import FPDF
class Utils:


    def string_to_datetime_with_hour(self, str_date):
        return datetime.strptime(str_date, '%d/%m/%y %H:%M:%S')
    def string_to_datetime_without_hour(self, str_date):
        date_to_return=None
        try:
            date_to_return =  datetime.strptime(str_date, "%Y-%m-%d")
        except Exception as e:
            print("bad date - Utils 'string_to_datetime_without_hour'")
        return date_to_return

    #return true if the end_date is not passed, false elsewhere
    def check_end_date(self, end_date):
        formatted_date_now = datetime.now()
        formatted_date_offer = datetime.strptime(end_date, '%Y-%m-%d')
        if (formatted_date_now < formatted_date_offer):
            return True
        return False

    def datetime_to_string(self, date):
        now = datetime.now()  # current date and time
        year = now.strftime("%Y")
        month = now.strftime("%m")
        day = now.strftime("%d")
        time = now.strftime("%H:%M:%S")
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        return date_time

    def pop(self, text, type):
        self.dialog = MDDialog(
            title=type,
            text=text,
            buttons = [
                MDFlatButton(text='OK', on_release=lambda a:Utils.close_pop(self)),
            ],
        )
        self.dialog.open()

    def close_pop(self):
        self.dialog.dismiss()
