# File for the Customer class, "from Customer import Customer" in Main.py

# Work in progress, not sure on a lot of things
# Customer class

# Import the ShoppingCart class to give user's their shopping cart
from ShoppingCart import ShoppingCart

class Customer:
    # new instance of Customer with empty variables and shopping cart import
    def __init__(self, username, password, billing_info, shipping_address, order_history, current_shopping_cart):
    
        # create a new Customer
        self.username = username
        self.password = password
        self.billing_info = billing_info
        self.shipping_address = shipping_address
        self.order_history = order_history
        self.current_shopping_cart = current_shopping_cart
    
    
    # change the user's username
    def setUsername(self, new_username):
        self.username = new_username
    
    # change the user's password
    def setPassword(self, new_password):
        self.password = new_password
    
    # change the user's billing info
    def updateBillingInfo(self, new_billing_info):
        self.billing_info = new_billing_info
    
    # change the user's shipping address
    def updateShippingAddress(self, new_shipping_address):
        self.shipping_address = new_shipping_address
    
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
        i = 1
        result = ""
        for order in self.order_history:
            result += "Order "
            result += str(i)
            result += "\n"
            result += order
            i += 1
        return result
    
    # add a new order to the end of the Customer's purchase history
    def addOrderToHistory(self, new_order):
        self.order_history.append(new_order)

    # Access the shopping cart member of this Customer object:
    def getShoppingCart(self):
        return self.current_shopping_cart
    
