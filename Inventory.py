
# File for the main Inventory class, "from Inventory import Inventory" in Main.py

# Import the Book class, as Books are passed in and out of the Inventory
from Book import Book

# Inventory class
class Inventory:
    """ Inventory class which is used to keep track of the amounts of books in the book store, and the names of those books by ISBN. Implements this with two Python dictionaries. \
        This class can add and remove arbitrary numbers of books in arbitrary quantities, search its list of books for results matching search queries, and display the whole \
        Inventory out. """

    def __init__(self, books):
        """ Create a new instance of the inventory class. If an old instance of the inventory exists saved in the program .json files, these will be interpreted as Python \
            dictionaries and passed as arguments to the new object, which will use them as parameters. If these do not exist, default None type arguments will be passed \
            in, and the Inventory will be initialized with empty dictionaries """
        
        # Populate the dictionary elements of this class.
        self.books = books


    def addBooks(self, book, count=1):
        """ This function adds new books to the Inventory. By default, adds 1 book to the Inventory, though that value can be overwritten. Raise a Value Error if that number \
            Is less than 1. This also write the updated count of books to the inventory json file, as well as adding new books created to the books json file, so that the \ 
            file is kept updated as the program runs. """

        # Raise an error if the given count is less than 0
        if count < 1:
            raise ValueError

        # Populate the dictionaries

        # If the book is already in the inventory
        if book.ISBN in self.books:

            # Simply add to the current count of the book in the inventory
            self.books[book.ISBN][amount] += count

        else:
            # Otherwise, we have to add the book to the list of books too.
            # Add the string of the book to the list, as that is overloaded to include all the relevant information about the book.
            new_book = {"title": book.title, "author": book.author, "ISBN": book.ISBN, "amount": count, "price": book.price}
            self.books[book.ISBN] = new_book

        # Each time a book is added, we'll just overwrite the whole inventory and inventory_count json files, so that it is always correct.
        with open("inventory.json", "w") as h:
            json.dump(self.books, h)


    def removeBooks(self, ISBN, count=0):
        """ This function removes books from the inventory. by default the count parameter is set to 0, which will be interpreted as removing all books from the inventory \
            This can be changed, though the function will raise a ValueError if the parameter is less than 0, or if it exceeds the current quantity of the books in the Inventory. \
            Also, this function can raise a key error when the desired ISBN is not in the Inventory, and will be handled by the main function as such. This also updates the \
            inventory json file as books are removed. """

        # Raise an error if the given count is invalid
        if count < 0:
            raise ValueError

        # Determine if the book is in the inventory
        # If it is not, a keyError will be raised
        num_books = self.books[ISBN][amount]

        # Now, if the user has requested removing more books than there are in the inventory, raise another ValueError
        if count > num_books:
            raise ValueError

        # Set the new number of books in the Inventory
        if count == 0:
            self.books[ISBN][amount] = 0
        else:
            self.books[ISBN][count] -= count

        # Each time the count of a book is augmented, we'll just overwrite the hwole inventory_count json file. removeBooks can't get rid of books in the inventory, just set their count to 0, so we don't need to possibly edit inventory.json
        with open("inventory.json", "w") as h:
            json.dump(self.books, h)


    def findBooks(self, queries):
        """ This function searches each entry in the inventory for the search terms in the queries list, print out each entry. """
        
        # List to store the results in, to be returned to the main function for printing
        results = []

        for query in queries:

            try:
                # See if the query in question can be interpreted as an integer
                query = int(query)

                # If the query is an integer, search for the integer in the list of ISBNs
                if query in self.books:
                    # Then, append a tuple of the stored Book dictionary and its count in the Inventory to the results
                    results.append((self.books[query]["title"], self.books[query]["author"], self.books[query]["ISBN"], self.books[query]["amount"], self.books[query]["price"]))

            except ValueError:
                # Except a ValueError if query is not an integer, search it as a string through the Titles and Authors of the Books
                for book in self.books.values:
                    if query in book["title"] or query in book["author"]:
                        # Append a tuple of the stored Book dictionary and its count in the Inventory to the results
                        results.append((self.books[query]["title"], self.books[query]["author"], self.books[query]["ISBN"], self.books[query]["amount"], self.books[query]["price"]))

        # Now all elements are in the results. Sort them by descening order using code I found at this link:
        # https://pythonguides.com/python-sort-list-of-tuples/
        # Reverse the sort so that the items with the highest quantity show up first
        results.sort(reverse=True, key=lambda a: a[3])

        # Finally, after each query has been handled, return the list of results, which will be displayed by the main() function, using the same helper function as listBooks()
        return results


    def listBooks(self):
        """ This function simply prepared every entry in the Inventory to be printed out by the main() function. The Main() handles the display, so this \
            funciton only needs to format all the entires into a list of tuples and to sort them. """

        # First, we populate a results list which we will eventually display:
        results = []
        for ISBN in self.books:
            results.append((self.books[query]["title"], self.books[query]["author"], self.books[query]["ISBN"], self.books[query]["amount"], self.books[query]["price"]))

        # Now all elements are in the results. Sort them by descening order using code I found at this link:
        # https://pythonguides.com/python-sort-list-of-tuples/
        # Reverse the sort so that the items with the highest quantity show up first
        results.sort(reverse=True, key=lambda a: a[3])
        
        # Finally, return the results for main() to display
        return results


