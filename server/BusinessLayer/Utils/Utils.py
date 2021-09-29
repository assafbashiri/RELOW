from fpdf import FPDF
from BusinessLayer.Controllers.CategoryController import CategoryController
from BusinessLayer.Controllers.UserController import UserController
from BusinessLayer.Object.Category import Category
import sqlite3


class Utils:



    def create_summery_end_offer(self, offer, u, c):
        # conn = sqlite3.connect('database.db', check_same_thread=False)

        # save FPDF() class into a variable pdf
        pdf = FPDF()

        # Add a page
        pdf.add_page()

        # set style and size of font that you want in the pdf
        pdf.set_font("Arial", size=15)

        # create a cell
        pdf.cell(200, 10, txt=f"product details: ",ln=1, align='C')
        pdf.cell(200, 10, txt=f"    product name: {offer.product.name} ",ln=1, align='C')
        pdf.cell(200, 10, txt=f"    product company: {offer.product.company} ",ln=1, align='C')
        pdf.cell(200, 10, txt=f"    product sizes: {offer.product.sizes} ",ln=1, align='C')
        pdf.cell(200, 10, txt=f"    product colors: {offer.product.colors} ",ln=1, align='C')
        pdf.cell(200, 10, txt=f"    product description: {offer.product.description} ",ln=1, align='C')
        pdf.cell(200, 10, txt=f"    product photos: 'photosss' ",ln=1, align='C')

        category = c.get_category_by_id(offer.category_id)
        category_name =category.name
        sub_category_name = category.get_sub_category_name_by_id(offer.sub_category_id)
        #offer details
        pdf.cell(200, 10, txt=f"offer details: ", ln=1, align='C')
        #pdf.cell(200, 10, txt=f"    offer start date:{offer.start_date} ",ln=1, align='C')
        pdf.cell(200, 10, txt=f"    offer final step: {offer.current_step} ",ln=1, align='C')
        pdf.cell(200, 10, txt=f"    offer category: {category_name} ",ln=1, align='C')
        pdf.cell(200, 10, txt=f"    offer sub category: {sub_category_name} ",ln=1, align='C')

        #step details
        pdf.cell(200, 10, txt=f"step details: ", ln=1, align='C')
        final_step = offer.steps[offer.current_step]
        pdf.cell(200, 10, txt=f"step price: {final_step.price} ", ln=1, align='C')
        pdf.cell(200, 10, txt=f"step buyers amount: {final_step.buyers_amount} ", ln=1, align='C')
        pdf.cell(200, 10, txt=f"step limit: {final_step.limit} ", ln=1, align='C')

        num_of_buyer=1
        for buyer in offer.current_buyers.keys():
            purchase = offer.current_buyers[buyer]
            buyer_obj=u.get_user_by_id(purchase.buyer_id)
            chosen_step = offer.steps[purchase.step_id]
            pdf.cell(200, 10, txt=f"buyer : {num_of_buyer}) : {buyer_obj.first_name} {buyer_obj.last_name}",ln=1, align='C')
            pdf.cell(200, 10, txt=f"    color : {purcahse.color}",ln=1, align='C')
            pdf.cell(200, 10, txt=f"    size : {purcahse.size}",ln=1, align='C')
            pdf.cell(200, 10, txt=f"    quantity : {purcahse.quantity}",ln=1, align='C')
            pdf.cell(200, 10, txt=f"    address : {purcahse.address}",ln=1, align='C')
            pdf.cell(200, 10, txt=f"    step details : ",ln=1, align='C')
            pdf.cell(200, 10, txt=f"        step price : {chosen_step.price}",ln=1, align='C')
            pdf.cell(200, 10, txt=f"        step limit : {chosen_step.limit}",ln=1, align='C')
            pdf.cell(200, 10, txt=f"        step buyers amount : {chosen_step.buyers_amount}",ln=1, align='C')

            num_of_buyer+=1

        # add another cell
        pdf.cell(200, 10, txt="---------------------------------------",
                 ln=2, align='C')

        # save the pdf with name .pdf
        pdf.output(f"Offers_summary/offer {offer.offer_id} summery.pdf")