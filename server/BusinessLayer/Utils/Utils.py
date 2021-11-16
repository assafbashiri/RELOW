from fpdf import FPDF

import sqlite3
from datetime import datetime
import secrets
import string


class Utils:

    def generate_password(self):
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(10))
        return password

    def check_end_date(self, end_date):
        formatted_date_now = datetime.now()
        formatted_date_offer = datetime.strptime(end_date, '%Y-%m-%d')
        if (formatted_date_now < formatted_date_offer):
            return True
        return False

    def create_summery_end_offers(self, expired_offers, u, c):
        # conn = sqlite3.connect('database.db', check_same_thread=False)
        # save FPDF() class into a variable pdf
        for offer in expired_offers:
            pdf = FPDF()

            # Add a page
            pdf.add_page()

            # set style and size of font that you want in the pdf
            pdf.set_font("Arial", size=11)

            # create a cell
            pdf.cell(200, 10, txt=f"product details: ", ln=1, align='C')
            pdf.cell(200, 10, txt=f"    product name: {offer.product.name} ", ln=1, align='L')
            pdf.cell(200, 10, txt=f"    product company: {offer.product.company} ", ln=1, align='L')
            pdf.cell(200, 10, txt=f"    product sizes: {offer.product.sizes} ", ln=1, align='L')
            pdf.cell(200, 10, txt=f"    product colors: {offer.product.colors} ", ln=1, align='L')
            pdf.cell(200, 10, txt=f"    product description: {offer.product.description} ", ln=5, align='L')
            pdf.cell(200, 10, txt=f"    product photos: {offer.product.photos} ", ln=1, align='L')

            category = c.get_category_by_id(offer.category_id)
            category_name = category.name
            sub_category_name = category.get_sub_category_name_by_id(offer.sub_category_id)
            # offer details
            pdf.cell(200, 10, txt=f"offer details: ", ln=1, align='C')
            # pdf.cell(200, 10, txt=f"    offer start date:{offer.start_date} ",ln=1, align='C')
            pdf.cell(200, 10, txt=f"    offer final step: {offer.current_step} ", ln=1, align='C')
            pdf.cell(200, 10, txt=f"    offer category: {category_name} ", ln=1, align='C')
            pdf.cell(200, 10, txt=f"    offer sub category: {sub_category_name} ", ln=1, align='C')

            # step details
            pdf.cell(200, 10, txt=f"step details: ", ln=1, align='C')
            final_step = offer.steps[offer.current_step]
            pdf.cell(200, 10, txt=f"step price: {final_step.price} ", ln=1, align='C')
            pdf.cell(200, 10, txt=f"step buyers amount: {final_step.buyers_amount} ", ln=1, align='C')
            pdf.cell(200, 10, txt=f"step limit: {final_step.limit} ", ln=1, align='C')

            num_of_buyer = 1
            for buyer in offer.current_buyers.keys():
                purchase = offer.current_buyers[buyer]
                buyer_obj = u.get_user_by_id(purchase.buyer_id)
                chosen_step = offer.steps[purchase.step_id]
                pdf.cell(200, 10, txt=f"buyer : {num_of_buyer}) : {buyer_obj.first_name} {buyer_obj.last_name}", ln=1,
                         align='C')
                pdf.cell(200, 10, txt=f"    color : {purchase.color}", ln=1, align='C')
                pdf.cell(200, 10, txt=f"    size : {purchase.size}", ln=1, align='C')
                pdf.cell(200, 10, txt=f"    quantity : {purchase.quantity}", ln=1, align='C')
                pdf.cell(200, 10, txt=f"    address : {purchase.address}", ln=1, align='C')
                pdf.cell(200, 10, txt=f"    step details : ", ln=1, align='C')
                pdf.cell(200, 10, txt=f"        step price : {chosen_step.price}", ln=1, align='C')
                pdf.cell(200, 10, txt=f"        step limit : {chosen_step.limit}", ln=1, align='C')
                pdf.cell(200, 10, txt=f"        step buyers amount : {chosen_step.buyers_amount}", ln=1, align='C')

                num_of_buyer += 1

            # add another cell
            pdf.cell(200, 10, txt="---------------------------------------",
                     ln=2, align='C')

            # save the pdf with name .pdf
            pdf.output(f"Offers_summary/offer_{offer.offer_id}_summery.pdf")
