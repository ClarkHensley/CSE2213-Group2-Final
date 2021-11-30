
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
        new_shopping_cart = ShoppingCart(customer["current_shopping_cart"]["owners_name"], customer["current_shopping_cart"]["inventory"])
        new_customer = Customer(customer["username"], customer["password"], customer["billing_info"], customer["shipping_address"], customer["order_history"], new_shopping_cart)
        new_customers[new_customer.getUsername()] = new_customer
        
    customers = new_customers
    username = ""

    # Welcome the user
    print("Welcome to the Book Store!\nTo continue, please log in:\n")
    # Infinite Loop, broken when the user exists
    while True:
        # If customer is not logged in
        if username = "":
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
                print("Please enter your username: ")
                username = input()
                # If the username exists
                if username in customers:
                    print("\nPlease enter your password: ")
                    password = input()
                    if password = customers[username].getPassword():
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
                updateCustomers()

                # Done
                print("\nAccount " + new_username + " has been created!\n")

        # Otherwise, the user is logged in:
        else:
            print("Welcome " + username + "!\n Please select an option:")
            print("0. Exit\n1. Logout\n2. etc...")
            user_choice = input()

            # Ensure that user_choice is an acceptable value, otherwise, prompt again
            try:
                user_choice = int(user_choice)
                if user_choice not in [0, 1, 2]:
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
            else:
                pass






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


def updateCustomers():
    """ Customers json files gets updated in many ways, so it makes more sense to use a helper function that just updates it every time we need to. """
    
    old_customers = dictFromJson("customers.json")
    old_customers[new_username] = {"username": customers[new_username].getUsername(), "password": customer[new_username].getPassword(), "billing_info": customers[new_username].getBillingInfo(), "shipping_address": customers[new_username].getShippingAddress(), "order_history": customers[new_username].order_history, "current_shopping_cart": customers[new_username].shoppingCart}
    with open("customers.json", "w") as h:
        json.dump(old_customers, h)


if __name__ == "__main__":
    main()

