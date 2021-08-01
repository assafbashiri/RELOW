from main import repository

def one(argument): #sign in
    print("1")

def two(argument): #log in
    argument.re
    repository.addUser()

def three(argument): #log out
    print("3")

def four(argument): #search for offer by name-buyer
    print("4")

def five(argument): #search for offer by category-buyer
    print("5")

def six(argument):  #buy - join offer- buyer
    print("6")

def seven(argument): #sell- add offer-seller
    print("76")

def eleven(argument): #update offer-seller
    print("11")

def eight(argument): #get buyer history-buyer
    print("8")

def nine(argument): #get seller history-seller
    print("9")

def ten(argument): #get active offers -buyer
    print("10")

def eleven(argument): #get active offers -seller
    print("11")

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