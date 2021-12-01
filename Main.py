
#####
# Methods and Tools for Software Development Group 2 Fall 2021
# Final Project, Command Line Interface for a bookstore
# Due Wednesday, December 1st, 2021
# Ferrin Senter, fas96
# Chris Greene, cbg232
# Clark Hensley, ch3136
# Nick Beers, nlb196
#####

# Import relevant libraries
import json

# Importing the classes from other files here
from Inventory import Inventory
from Book import Book
from Customer import Customer
from ShoppingCart import ShoppingCart

# Main driver function
def main():
    """ Main function, handles input/output, acts as a command line interface to display the shop to the user. """

    # On startup, populate the list of current Customers, Shopping Carts, and Inventories
    # This function populates various dictionaries of stored users, Shopping Carts, and Inventories
    
    # The inventory
    inv = dictFromJson("inventory.json")

    inventory = Inventory(inv)

    # The Customers
    # Gets a dicitonary of dictionaries from the JSON file
    customers = dictFromJson("customers.json")
    # Convert this to a dictionary of Customer objects
    new_customers = {}
    for customer in customers:

        new_shopping_cart = ShoppingCart(customers[customer]["current_shopping_cart"][0], customers[customer]["current_shopping_cart"][1])
        new_customer = Customer(customers[customer]["username"], customers[customer]["password"], customers[customer]["billing_info"], customers[customer]["shipping_address"], customers[customer]["order_history"], new_shopping_cart)
        new_customers[new_customer.getUsername()] = new_customer
        
    customers = new_customers
    username = ""

    # Welcome the user
    print("Welcome to the Book Store!\nTo continue, please log in:\n")
    # Infinite Loop, broken when the user exists
    while True:
        # If customer is not logged in
        if username == "":
            print("To continue, please select an option:\n0. Exit Program\n1. Log In\n2. Create Account\n")
            user_choice = input()

            # Ensure that user_choice is an acceptable value, otherwise, prompt again
            try:
                user_choice = int(user_choice)
                if user_choice not in [0, 1, 2]:
                    raise ValueError
            except ValueError:
                print("Invalid choice.\n")
                continue

            # Choose the correct option based on user's choice
            if user_choice == 0: 
                print("Goodbye")
                break

            elif user_choice == 1:
                # Log-in
                print("Please enter your username: ", end="")
                username = input()
                # If the username exists
                if username in customers:
                    print("\nPlease enter your password: ", end="")
                    password = input()
                    if password == customers[username].getPassword():
                        print("\nLogging in...")
                    else:
                        print("\nInvalid password.")
                        username = ""
                else:
                    print("\nInvalid username. Considering creating user " + username + "\n")
                    username = ""

            elif user_choice == 2:
                # Create a new account
                print("Please enter a new username: ")
                new_username = input()
                # Ensure the username isn't taken
                if new_username in customers:
                    print("\n That username is taken. Please try again.\n")
                    continue
                print("\nPlease enter a new password for " + new_username + ": ")
                new_password = input()
                print("\nPlease confirm new password for " + new_username + ": ")
                check_password = input()
                if new_password != check_password:
                    print("\nPasswords do not match. Please try again.\n")
                    continue
                print("\nPlease enter your billing information (This can be changed later): ")
                new_billing_info = input()
                print("\nPlease enter your shipping address. (This can be changed later): ")
                new_shipping_address = input()

                # Instantiate a new Customer object, add it to the Customers dictionary
                new_customer = Customer(new_username, new_password, new_billing_info, new_shipping_address, [], ShoppingCart(new_username, {}))
                customers[new_username] = new_customer

                # Also, add this new customer to customers.json, via the dictionary
                updateCustomers(new_customer)

                # Done
                print("\nAccount " + new_username + " has been created!\n")

        # Otherwise, the user is logged in:
        else:
            print("Welcome " + username + "!\n Please select an option:")
            print("0. Exit\n1. Logout\n2. View and Filter All Books\n3. View, Edit, and Checkout User's Cart\n4. View and Edit Current User's Account")
            user_choice = input()

            # Ensure that user_choice is an acceptable value, otherwise, prompt again
            try:
                user_choice = int(user_choice)
                if user_choice not in [0, 1, 2, 3, 4]:
                    raise ValueError
            except ValueError:
                print("Invalid choice.\n")
                continue

            if user_choice == 0:
                print("\nGoodbye!")
                break
            elif user_choice == 1:
                print("\nLogging you out...")
                username = ""
            elif user_choice == 2:
                inventoryMenu(inventory)
            elif user_choice == 3:
                cartMenu(customers[username].getShoppingCart(), inventory, customers[username])



def dictFromJson(file):
    """ Attempt to open a .json file, which will be converted into a python Dictionary. These files store things such as the current inventory, the list of users, and the list of shopping carts """

    # Attempt to create a dictionary from the file and return it
    try:
        with open(file, "r") as h:
            h_content = h.read()
            temp = json.loads(h_content)
            return temp
    # If the file does not exist, return am empty dictionary
    except FileNotFoundError:
        return {}


def updateCustomers(new_customer):
    """ Customers json files gets updated in many ways, so it makes more sense to use a helper function that just updates it every time we need to. """
    
    old_customers = dictFromJson("customers.json")
    old_customers[new_customer.getUsername()] = {"username": new_customer.getUsername(), "password": new_customer.getPassword(), "billing_info": new_customer.getBillingInfo(), "shipping_address": new_customer.getShippingAddress(), "order_history": new_customer.viewOrderHistory(), "current_shopping_cart": new_customer.getShoppingCart().getValues()}
    with open("customers.json", "w") as h:
        json.dump(old_customers, h)

def inventoryMenu(inventory):
    """ Sub-menu for the inventory, with the ability to view all books, filter that list, and add/remove books from the inventory """

    while True:
        print("\nPlease select an option to interact with the inventory:\n0. Return to Main Menu\n1. View all Books\n2. Filter List of all books\n\nThe following two options would only be open to an \"employee\" type user, but we only have \"Customer\"\n3. Add Books to inventory\n4. Remove Books from inventory\n")

        # Ensure the user's choice is valid
        user_choice = input()
        try:
            user_choice = int(user_choice)
            if user_choice not in [0, 1, 2, 3, 4]:
                raise ValueError
        except ValueError:
            print("Invalid choice.\n")
            continue

        # Return to main menu
        if user_choice == 0:
            break

        # Display the entire inventory
        elif user_choice == 1:
            entry_list = inventory.listBooks()
            for entry in entry_list:
                print(entry)

        # Filter and display the inventory
        elif user_choice == 2:
            print("\nPlease enter one or more search terms to filter the list of books by\nEnter terms separated by pipes, such as term1|term2|term3")
            query_string = input()
            queries = query_string.split("|")
            if len(queries) <= 0:
                print("Invalid search. Your search must contain at least one search term.")
            else:
                entry_list = inventory.findBooks(queries)
                for entry in entry_list:
                    print(entry)
                
        # These two remaining functions would not normally be available unless the user had control over the Inventory, but this program doens't account for that, and we need a way to add/remove books from the Inventory.

        # Add a book to the Inventory
        elif user_choice == 3:
            print("\nEnter the ISBN of the book you are adding: ", end="")
            new_ISBN = input()
            print("\nEnter the Title of the book you are adding: ", end="")
            new_title = input()
            print("\nEnter the Author of the book you are adding: ", end="")
            new_author = input()
            print("\nEnter the Price of the book you are adding: ", end="")
            new_price = input()
            try:
                new_price = float(new_price)
                new_price = float("{:.2f}".format(new_price))
                if new_price <= 0:
                    raise ValueError
            except ValueError:
                print("Price of the new book must be a positive number.")
                continue
            new_book = Book(new_title, new_author, new_price, new_ISBN)
            print("\nEnter the number of copies of " + new_book.title + " by " + new_book.author + " to add to the Inventory: ", end="")
            count = input()
            try:
                count = int(count)
                inventory.addBooks(new_book, count)
                print(str(count) + " copy/copies of " + new_book.title + " by " + new_book.author + " has(have) been added to the Inventory")
                continue

            except ValueError:
                print("Number of copies of the new book to be added must be a positive integer")
                continue

        # Remove a book form the Inventory
        elif user_choice == 4:
            print("\nEnter the ISBN of the book you wish to remove: ", end="")
            removal_ISBN = input()
            print("\nEnter the number of books to remove from the inventory, enter \"0\" to remove all copies: ", end="")
            removal_count = input()

            try:
                removal_count = int(removal_count)
                inventory.removeBooks(removal_ISBN, removal_count)
                print("Removal Complete")
                continue
            except ValueError:
                print("Number of copies of this book to remove must be an positive integer less than or equal to the current quantity of that book in the Inventory (or \"0\" to remove all of the copies of that book")
                continue
            except KeyError:
                print("No book with that ISBN is currently in stock, and thus cannot be removed. Please try again.")
                continue

    
def cartMenu(cart, inventory, customer):
    """ Sub-menu for the shopping cart, with the ability to view the cart, add to or remove from the cart, and check the cart out. """

    while True:
        print("\nPlease select an option to interact with " + cart.getValues()[0] + "'s shopping cart:\n0. Return to Main Menu\n1. View the Cart\n2. Add Books to the Cart\n3. Remove Books from the Carts\n4. Checkout\n")

        # Ensure the user's choice is valid
        user_choice = input()
        try:
            user_choice = int(user_choice)
            if user_choice not in [0, 1, 2, 3, 4]:
                raise ValueError
        except ValueError:
            print("Invalid choice.\n")
            continue

        # Return to main menu
        if user_choice == 0:
            break

        # View the Cart
        if user_choice == 1:
            print(cart.displayCart())

        # Add items to the cart
        elif user_choice == 2:
            print("\nEnter the ISBN of the book you wish to add to your cart: ", end="")
            new_ISBN = input()
            
            # Ensure the requested ISBN is in the Inventory
            if not(new_ISBN in inventory):
                print("\nThat ISBN does not match any ISBN in our system. Please try again.")
                continue
            else:
                # Create a new Book object with the values of the book at that ISBN
                new_book = Book(inventory[new_ISBN]["title"], inventory[new_ISBN]["author"], inventory[new_ISBN]["price"], inventory[new_ISBN]["ISBN"])
                
                print("\nEnter the number of copies to add: ", end="")
                quantity = input()

                # Ensure the quantity is valid
                try:
                    quantity = int(quantity)
                    if quantity < 1 or quantity > inventory[new_ISBN]["amount"]:
                        raise ValueError
                except ValueError:
                    print("\nThe number of copies you wish to add must be an integer greater than 0 and at most the number of copies in stock.")
                    continue

                cart.addBook(new_book, quantity)

                updateCustomers()

        # Remove books from the cart
        elif user_choice == 3:

            print("\nEnter the ISBN of the book you wish to remove from your cart: ", end="")
            removal_ISBN = input()
            
            # Ensure the requested ISBN is in the Inventory
            if not(removal_ISBN in inventory):
                print("\nThat ISBN does not match any ISBN in our system. Please try again.")
                continue
            else:
                
                print("\nEnter the number of copies to remove (Enter \"0\" to remove all copies of this book): ", end="")
                quantity = input()

                # Ensure the quantity is valid
                try:
                    quantity = int(quantity)
                    if quantity < 0 or quantity > inventory[new_ISBN]["amount"]:
                        raise ValueError
                except ValueError:
                    print("\nThe number of copies you wish to remove must be an integer greater than or equal to 0 and at most the number of copies in your cart.")
                    continue

                cart.removeBook(removal_ISBN, quantity)

                updateCustomers()

        # Checkout
        elif user_choice == 4:
            final_order = cart.displayCart()

            removal_list = cart.checkout()

            for item in removal_list:
                inventory.removeBooks(item[0], item[1])

            customer.addOrderToHistory(final_order)

                
                            
def func():
    pass


    
if __name__ == "__main__":
    main()

