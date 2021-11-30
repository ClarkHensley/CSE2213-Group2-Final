# File for the ShoppingCart class.

# Import the Book class, as Books are passed in and out of the Shopping Cart
from Book import Book
from Customer import Customer

# ShoppingCart class
class ShoppingCart:
    """ ShoppingCart class is used to keep track of what the customer has in theier cart. 
    It will include the titles and quantities of each of the books in the cart, the ability to display the contents of the cart, 
    and the ability to add and remove books from the cart."""

    def __init__(self, owners_name:None, inventory:None):


        # Populate the dictionary elements of this class. 
        if owners_name is None:
            self.owners_name = {}
        else: 
            self.owners_name = owners_name

        if inventory is None:
            self.inventory = {}
        else: 
            self.inventory = inventory

        #TODO: Returns an error if the owners_name is not the name of a customer that exists
        temp1 = set([x for x in self.owners_name])
        temp2 = set([x for x in self.username])
        if not( temp1 == temp2):
            raise ValueError

    def addBook(self, new_book, quantity=1):
        """ This function adds new books to the Shopping Cart. It adds it by ISBN."""

    def removeBook(self, book, quantity=0):
        """ This function removes books from the Shopping Cart. By default the quantity parameter is set to 0"""

    def displayCart(self):

    def checkout(self):

