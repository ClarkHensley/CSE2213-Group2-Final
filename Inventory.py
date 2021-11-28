
# File for the main Inventory class, "from Inventory import Inventory" in Main.py

# Import the Book class, as Books are passed in and out of the Inventory
from Book import Book

# Inventory class
Class Inventory:
    """ Inventory class which is used to keep track of the amounts of books in the book store, and the names of those books by ISBN. Implements this with two Python dictionaries. \
        This class can add and remove arbitrary numbers of books in arbitrary quantities, search its list of books for results matching search queries, and display the whole \
        Inventory out. """

    def __init__(self, books_count=None, books=None):
        """ Create a new instance of the inventory class. If an old instance of the inventory exists saved in the program .json files, these will be interpreted as Python \
            dictionaries and passed as arguments to the new object, which will use them as parameters. If these do not exist, default None type arguments will be passed \
            in, and the Inventory will be initialized with empty dictionaries """
        
        # Populate the dictionary elements of this class.
        if books_count is None:
            self.books_count = {}
        else:
            self.books_count = books_count

        if books is None:
            self.books = {}
        else:
            self.books = books

        # This is possibly redundant, but ensure that the keys in both dictionaries are the same, and thus the Inventory is constructed correctly.
        # Raise a ValueError if this is not the case, which will be handled during initialization of the program.

        # Create sets of the keys of the dictionaries. The dictionaries don't need to be in the same order, they just need to have the same elements.
        # There should be no duplicate ISBNs in the system, so there will be only one instance of each number, thus a set handles this appropriately
        temp1 = set([x for x in self.books_count])
        temp2 = set([x for x in self.books])
        if not( temp1 == temp2 ):
            raise ValueError

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
            self.books_count[book.ISBN] += count

        else:
            # Otherwise, we have to add the book to the list of books too.
            self.books[book.ISBN] = book
            self.books_count[book.ISBN] = count

        # TODO
        # Implement the writing to the .json file(s) here (Inventories and maybe Books)

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
        num_books = self.books_count[ISBN]

        # Now, if the user has requested removing more books than there are in the inventory, raise another ValueError
        if count > num_books:
            raise ValueError

        # Set the new number of books in the Inventory
        if count == 0:
            self.books_count[ISBN] = 0
        else:
            self.books_count[ISBN] -= count

        # TODO
        # Implement the writing to the .json file here

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
                    # Then, append a tuple of the stored Book object and its count in the Inventory to the results
                    results.append((self.books[query], self.books_count[query]))

            except ValueError:
                # Except a ValueError if query is not an integer, search it as a string through the Titles and Authors of the Books
                for book in self.books.values:
                    if query in book.title or query in book.author:
                        # Append a tuple of the stored Book object and its count in the Inventory to the results
                        results.append((book, self.books_count[book.ISBN]))

        # Now all elements are in the results. Sort them by descening order using code I found at this link:
        # https://pythonguides.com/python-sort-list-of-tuples/
        # Reverse the sort so that the items with the highest quantity show up first
        results.sort(reverse=True, key=lambda a: a[1])

        # Finally, after each query has been handled, return the list of results, which will be displayed by the main() function, using the same helper function as listBooks()
        return results

    def listBooks(self):
        """ This function simply prepared every entry in the Inventory to be printed out by the main() function. The Main() handles the display, so this \
            funciton only needs to format all the entires into a list of tuples and to sort them. """

        # First, we populate a results list which we will eventually display:
        results = []
        for ISBN in self.books:
            results.append(self.books[ISBN], self.books_count[ISBN])

        # Now all elements are in the results. Sort them by descening order using code I found at this link:
        # https://pythonguides.com/python-sort-list-of-tuples/
        # Reverse the sort so that the items with the highest quantity show up first
        results.sort(reverse=True, key=lambda a: a[1])
        
        # Finally, return the results for main() to display
        return results

