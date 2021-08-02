from BussinesLayer import Controllers
from BussinesLayer.Controllers import UserController, CategoryController


def one(argument): #sign in
    response = UserController.addUser(argument['first_name'], argument['last_name'], argument['email'], argument['password'])
    return response

def two(argument): #log in
    response = UserController.getUser(argument['email'], argument['password'])
    return response

def three(argument): #log out
    print("3")

def four(argument): #search for offer by name-buyer
    response = CategoryController.getOfferByNamw(argument['name'])
    return response


def five(argument): #search for offer by category-buyer
    response = CategoryController.getOfferByCategory(argument['category'])
    return response


def six(argument):  #buy - join offer- buyer
    response = CategoryController.joinOffer(argument['offer_id'])
    return response


def seven(argument): #sell- add offer-seller
    response = CategoryController.addOffer(argument['ofer_id'], argument['user_id'], argument['category_id'], argument['subCategory_id'], argument['start_date'], argument['end_date'], argument['details'], argument['steps'])
    return response


def eleven(argument): #update offer-seller
    response = CategoryController.updateOffer(argument['ofer_id'], argument['user_id'], argument['category_id'], argument['subCategory_id'], argument['start_date'], argument['end_date'], argument['details'], argument['steps'])
    return response
def eight(argument): #get buyer history-buyer
    response = UserController.getBuyerHistory(argument['user_id'])
    return response

def nine(argument): #get seller history-seller
    response = UserController.getSellerHistory(argument['user_id'])
    return response

def ten(argument): #get active offers -buyer
    response = UserController.getActiveOffers_buyer()
    return response

def eleven(argument): #get active offers -seller
    response = UserController.getActiveOffers_seller()
    return response

def eleven(argument): #get offer -buyer
    print("11")

def eleven(argument): #get hot deals-buyer
    print("11")

def eleven(argument): #set hot offers-ADMIN
    print("11")

def eleven(argument): #confirm offer-ADMIN
    print("11")

def eleven(argument): #set hot deals-ADMIN
    print("11")

def eleven(argument): #some statistics
    print("11")


switcher= {1:one,
           2:two,
           3:three,
           4:four,
           5:five,
           6:six,
           7:seven,
           8:eight,
           9:nine,
           10:ten
                    }

def hendeling(argument):
    req = argument['op']
    func = switcher.get(req,"nothing")
    return func(argument)