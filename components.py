# CLASSES AND METHODS
class Store():
    def __init__(self, name):
        self.name = name
        self.products = []
        """
        Initializes a new store with a name.
        """
        # your code goes here!

    def add_product(self, product):
        self.products.append(product)
        """
        Adds a product to the list of products in this store.
        """
        # your code goes here!

    def print_products(self):
        print("----------------------")
        for product in self.products:
          print("\t" + str(product))
          # print("\tDescription: " + self.product.description)
          # print("\tPrice: " + str(self.product.price))

        """
        Prints all the products of this store in a nice readable format.
        """
        # your code goes here!


class Product():
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
        """
        Initializes a new product with a name, a description, and a price.
        """
        # your code goes here!

    def __str__(self):
        # your code goes here!
        return "\tProduct Name: " + self.name + "\nDescription: " + self.description +"\nPrice: " + str(self.price)


class Cart():
    def __init__(self):
        self.products = []
        """
        Initializes a new cart with an empty list of products.
        """
        # your code goes here!

    def add_to_cart(self, product):
        self.products.append(product)
        """
        Adds a product to this cart.
        """
        # your code goes here!

    def get_total_price(self):
        total = 0
        for item in self.products:
            total += item.price
        return total
        """
        Returns the total price of all the products in this cart.
        """
        # your code goes here!

    def print_receipt(self):
        for item in self.products:
            print(str(item))
        print("Your total is: " + str(self.get_total_price()))
        """
        Prints the receipt in a nice readable format.
        """
        # your code goes here!

    def checkout(self):
        self.print_receipt()
        response = input("Confirm?(y or n)")
        if(response == 'y'):
            print("Thank you, your order has been placed... stay tuned for shipping info")
        else:
            print("Boooo your order has been cancelled!!")
        """
        Does the checkout.
        """
        # your code goes here!
