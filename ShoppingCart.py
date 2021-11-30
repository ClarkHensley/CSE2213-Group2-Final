# File for the ShoppingCart class.

# Import the Book class, as Books are passed in and out of the Shopping Cart
from Book import Book

# ShoppingCart class
class ShoppingCart:
    """ ShoppingCart class is used to keep track of what the customer has in their cart. 
    It will include the titles and quantities of each of the books in the cart, the ability to display the contents of the cart, 
    and the ability to add and remove books from the cart."""

    def __init__(self, owners_name, inventory=None):
        self.owners_name = owners_name

        if inventory is None:
            self.inventory = {}
        else: 
            self.inventory = inventory


    def addBook(self, book, quantity=1):
        """ This function adds new books to the Shopping Cart. It adds it by ISBN."""
        
        # Raise an error if the given count is less than 0
        if quantity < 1:
            raise ValueError

        if book.ISBN in self.inventory:

            self.inventory[new_book.ISBN][amount] += quantity

        else:
            new_book = {"title": book.title, "author": book.author, "ISBN": book.ISBN, "amount": quantity, "price": book.price}


    def removeBook(self, book, quantity=0):
        """ This function removes books from the Shopping Cart. By default the quantity parameter is set to 0"""

        # Raise an error if the count is invalid
        if quantity < 0:
            raise ValueError

        # Determine if the book is in the inventory
        # If it is not, a keyError will be raised
        num_books = self.inventory[ISBN][amount]

        # Now, if the user has requested removing more books than there are in the inventory, raise another ValueError
        if quantity > num_books:
            raise ValueError

        # Finally, set the new number
        self.inventory[ISBN][amount] -= quantity

        # If the count is not at Zero (or if quantity was 0), remove the entry form the cart.
        if self.inventory[ISBN][amount] == 0 or quantity == 0:
            del self.inventory[ISBN]

    def displayCart(self):
        """ Format the contents of the shoppping cart for display """
        running_total = 0.0
        final_string = "|Title\t|Author\t|ISBN\t|Amount\t|Price\t|Total Price\t|\n"

        for ISBN in self.inventory:
            sub_total = float(self.inventory[ISBN]["price"]) * float(self.inventory[ISBN]["amount"])
            sub_total = float("{:.2f}".format(sub_total))
            running_total += sub_total

            final_string += "|" + self.inventory[ISBN]["title"] + "\t|" + self.inventory[ISBN]["author"] + "\t|" + self.inventory[ISBN]["ISBN"] + "\t|" + self.inventory[ISBN]["amount"] + "\t|" + self.inventory[ISBN]["price"] + "\t|" + sub_total + "\t|\n"

        # Final line
        final_string += "|\t\t|\t\t|\t\t|\t\t|\t\t|" + str(running_total) + "\t|"

        return final_string

    def getValues(self):
        return (self.owners_name, self.inventory)

    def checkout(self):
        pass

