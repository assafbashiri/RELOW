from datetime import datetime
import time
import requests
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.button import Button
from fpdf import FPDF
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
    # def create_summery_end_offer(self, offer):
    #     # save FPDF() class into a variable pdf
    #     pdf = FPDF()
    #
    #     # Add a page
    #     pdf.add_page()
    #
    #     # set style and size of font that you want in the pdf
    #     pdf.set_font("Arial", size=15)
    #
    #     # create a cell
    #     pdf.cell(200, 10, txt=f"product name: {offer.product['name']} ",ln=1, align='C')
    #     pdf.cell(200, 10, txt=f"product company: {offer.product['company']} ",ln=1, align='C')
    #
    #     num_of_buyer=1
    #     for purchase in offer.current_buyers:
    #         buyer_name='nameeeeeeeee'
    #         pdf.cell(200, 10, txt=f"buyer : {num_of_buyer}) : {buyer_name}",ln=1, align='C')
    #         pdf.cell(200, 10, txt=f"    color : {purcahse.color}",ln=1, align='C')
    #         pdf.cell(200, 10, txt=f"    size : {purcahse.size}",ln=1, align='C')
    #
    #         num_of_buyer+=1
    #
    #     # add another cell
    #     pdf.cell(200, 10, txt="---------------------------------------",
    #              ln=2, align='C')
    #
    #     # save the pdf with name .pdf
    #     pdf.output(f"Offers_summary/offer {offer.offer_id} summery.pdf")

    #type = alert/succes
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
