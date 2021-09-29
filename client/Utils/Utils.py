from datetime import datetime
from fpdf import FPDF
import time
import requests
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.button import Button

class Utils:


    def string_to_datetime_with_hour(self, str_date):
        return datetime.strptime(str_date, '%d/%m/%y %H:%M:%S')
    def string_to_datetime_without_hour(self, str_date):
        return datetime.strptime(str_date, "%Y-%m-%d")
    def compare_dates(self, end_date1, end_date2):
        a=0

        # year1 = end_date1.year
        # month1 = end_date1.month
        # day1 = end_date1.day
        #
        # year2 = end_date2.year
        # month2 = end_date2.month
        # day2 = end_date2.day
        #
        #



        formatted_date1 = time.strptime(end_date1, '%y-%m-%d %H:%M:%S')
        formatted_date2 = time.strptime(end_date2, '%y-%m-%d %H:%M:%S')
        print(formatted_date1 > formatted_date2)

        # if date1 < date2:
        #     return -1
        # elif date1==date2:
        #     return 0
        # else:
        #     return 1

    def datetime_to_string(self, date):
        now = datetime.now()  # current date and time
        year = now.strftime("%Y")
        month = now.strftime("%m")
        day = now.strftime("%d")
        time = now.strftime("%H:%M:%S")
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        return date_time
    def create_summery_end_offer(self, offer):
        # save FPDF() class into a variable pdf
        pdf = FPDF()

        # Add a page
        pdf.add_page()

        # set style and size of font that you want in the pdf
        pdf.set_font("Arial", size=15)

        # create a cell
        pdf.cell(200, 10, txt=f"product name: {offer.product['name']} ",ln=1, align='C')
        pdf.cell(200, 10, txt=f"product company: {offer.product['company']} ",ln=1, align='C')

        num_of_buyer=1
        for purchase in offer.current_buyers:
            buyer_name='nameeeeeeeee'
            pdf.cell(200, 10, txt=f"buyer : {num_of_buyer}) : {buyer_name}",ln=1, align='C')
            pdf.cell(200, 10, txt=f"    color : {purcahse.color}",ln=1, align='C')
            pdf.cell(200, 10, txt=f"    size : {purcahse.size}",ln=1, align='C')

            num_of_buyer+=1

        # add another cell
        pdf.cell(200, 10, txt="---------------------------------------",
                 ln=2, align='C')

        # save the pdf with name .pdf
        pdf.output(f"Offers_summary/offer {offer.offer_id} summery.pdf")

    #type = alert/succes
    def pop(self, text, type):
        if self.dialog is None:
            self.dialog=MDDialog(
                title=type,
                text=text,
                buttons = [
                    MDFlatButton(text='OK', on_release=lambda a=self.dialog:Utils.close_pop(self, a)),
                ],
            )
        self.dialog.open()

    def close_pop(self,d):
        self.dialog.dismiss()
