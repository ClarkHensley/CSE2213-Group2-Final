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


    def addBook(self, book, quantity):
        """ This function adds new books to the Shopping Cart. It adds it by ISBN."""
        
        if book.ISBN in self.inventory:

            self.inventory[book.ISBN]["amount"] += quantity

        else:
            new_book = {"title": book.title, "author": book.author, "ISBN": book.ISBN, "amount": quantity, "price": book.price}
            self.inventory[book.ISBN] = new_book


    def removeBook(self, ISBN, quantity=0):
        """ This function removes books from the Shopping Cart. By default the quantity parameter is set to 0"""

        # Raise an error if the count is invalid
        if quantity < 0:
            raise ValueError

        # Determine if the book is in the inventory
        # If it is not, a keyError will be raised
        num_books = self.inventory[ISBN]["amount"]

        # Now, if the user has requested removing more books than there are in the inventory, raise another ValueError
        if quantity > num_books:
            raise ValueError

        # Finally, set the new number
        self.inventory[ISBN]["amount"] -= quantity

        # If the count is not at Zero (or if quantity was 0), remove the entry form the cart.
        if self.inventory[ISBN]["amount"] == 0 or quantity == 0:
            del self.inventory[ISBN]

    def getTotalCost(self):
        """Calculate total cost of the shopping cart"""
        running_total = 0.0

        for ISBN in self.inventory:
            sub_total = float(self.inventory[ISBN]["price"]) * float(self.inventory[ISBN]["amount"])
            sub_total = float("{:.2f}".format(sub_total))
            running_total += sub_total
        return running_total
    
    def displayCart(self):
        """ Format the contents of the shoppping cart for display """
        final_string = "" 
        running_total = self.getTotalCost()
        title_string = "\n|{0:^30}|{1:^20}|{2:^20}|{3:^10}|{4:^15}|{5:^15}|\n".format("Title", "Author", "ISBN", "Amount", "Price", "Total Price")
        final_string += title_string
        final_string += "\n"
        hr = "{0:-^117}".format("")
        final_string += hr
        final_string += "\n"
        
        for ISBN in self.inventory:
            book_string = "|{0:^30}|{1:^20}|{2:^20}|{3:^10}|{4:^15}|{5:^15}|\n".format(self.inventory[ISBN]["title"], self.inventory[ISBN]["author"], self.inventory[ISBN]["ISBN"], self.inventory[ISBN]["amount"], "$" + str(self.inventory[ISBN]["price"]), "$" + str(float(self.inventory[ISBN]["price"]) * int(self.inventory[ISBN]["amount"])))
            final_string += book_string
            final_string += "\n"

        # Final line
        total_string = "{0:^102}{1:^15}".format("", "$" + str(running_total))
        final_string += total_string
        final_string += "\n"
        
        return final_string

    def getValues(self):
        """ Return the owner's name and inventory of the cart, which makes this object easier to reference in main() """
        return (self.owners_name, self.inventory)


    def checkout(self):
        """ Stores the ISBNs and quantities to remove, clears the Cart's inventory, and returns those ISBNs and quantities. """
        
        removal_list = []
        for ISBN in self.inventory:
            removal_list.append((ISBN, self.inventory[ISBN]["amount"]))
            
        del self.inventory
        self.inventory = {}

        return removal_list

