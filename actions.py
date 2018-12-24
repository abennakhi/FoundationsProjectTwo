# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "Ahmad and Mariam's Emporium"  # Give your site a name

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
    for store in stores:
      print("- "+ store.name)
    """
    prints the list of stores in a nice readable format.
    """
    # your code goes here!

def get_store(store_name):
    for store in stores:
      if(store_name == store.name):
        return store
    return False
    """
    receives a name for a store, and returns the store object with that name.
    """
    # your code goes here!
def check_product(store, product_name):
    for product in store.products:
      if(product_name == product.name):
        return product
    else:
        return False


def pick_store(cart):
    print("Please pick a store from our glorious selection:(enter 'checkout' to checkout) ")
    selection = input(print_stores())

    while not selection == "checkout":
        if(get_store(selection) == False):
            print("No store with that name!!")
            selection = input(">> ")
        else:
            pick_products(cart, get_store(selection))
            selection = input(print_stores())


    cart.checkout()
    """
    prints list of stores and prompts user to pick a store.
    """
    # your code goes here!

def pick_products(cart, picked_store):
    print("Please pick a prodoct from the list: (enter 'back' to view the list of stores) ")
    picked_store.print_products()
    selection = input(">> ")
    while not selection == "back":
        if check_product(picked_store, selection):
            cart.add_to_cart( check_product(picked_store, selection))
            selection = input(">> ")
        else:
            selection = input(">> ")
    pick_store(cart)    
    """
    prints list of products and prompts user to add products to card.
    """
    # your code goes here!

def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    # your code goes here!
    pick_store(cart)


def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
