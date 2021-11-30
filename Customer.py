# File for the Customer class, "from Customer import Customer" in Main.py

# Work in progress, not sure on a lot of things
# Customer class

# Import the ShoppingCart class to give user's their shopping cart
from ShoppingCart import ShoppingCart

Class Customer:
# new instance of Customer with empty variables and shopping cart import
def __init___(self, username=None, password=None, billing_info=None, shipping_address=None, order_history=None, current_shopping_cart=ShoppingCart):
    
    # create a new Customer
    self.username = username
    self.password = password
    self.billing_info = billing_info
    self.shipping_address = shipping_address

    # order history and current shopping cart
    self.order_history = []    # creates a new empty list for customer order history, not sure if this correct
    self.current_shopping_cart = ShoppingCart

    # return an error if the Customer's username already exists 
    # python.org - not sure about this
    if self.username in Customer.username:
        raise NameError('Username already exists.')

# change the user's username
def setUsername(self, new_username):
    new_username = self.username

# change the user's password
def setPassword(self, new_password):
    new_password = self.password

# change the user's billing info
def updateBillingInfo(self, new_billing_info):
    new_billing_info = self.billing_info

# change the user's shipping address
def updateShippingAddress(self, new_shipping_address):
    new_shipping_address = self.shipping_address

# return Customer's username
def getUsername(self):
    return self.username

# return Customer's password
def getPassword(self):
    return self.password

# return Customer's billing
def getBillingInfo(self):
    return self.billing_info

# return Customer's shipping
def getShippingAddress(self):
    return self.shipping_address

# display order history for the customer
# from GeeksforGeeks
def viewOrderHistory(self):
    print(*self.order_history, sep = "\n")

# add a new order to the end of the Customer's purchase history
def addOrderToHistory(self, new_order):
    self.order_history.append(new_order)

# delete the account if the user enters the correct password, after asking the user if they are sure
def deleteAccount(password):
