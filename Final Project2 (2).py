print('\n================== MINI PROJECT==================')
print('\n================== SHOPPING SERVICE ==================')
# print('\n================ 1st step: Catalogue parent class creation =============')

from datetime import datetime
from datetime import date as dt_date

class Catalogue:           # note:parent class or the superclass
    def __init__(self, electronics, books):
        self.electronics = electronics
        self.books = books

    def __str__(self):
        return f' Electronics = {self.electronics}, Books = {self.books}'

# print('\n================ 2nd step:  Electronic class creation =============')
class ElectronicProduct:
    def __init__(self, brand, type, display_name, price, n_inventory, inventory_status, warranty):
        self.brand = brand
        self.type = type
        self.display_name = display_name
        self.price = price
        self.n_inventory = n_inventory
        self.inventory_status = inventory_status
        self.warranty = warranty   #note: warranty only applies for electronic class so, subclasses wont inherit the same sample variable or attribute.

    def __str__(self):
        return f' {self.brand}, {self.type}, {self.display_name}, ${self.price}, {self.n_inventory}, {self.inventory_status}, {self.warranty}'

    def buy_product(self):    #note:add function definition (buy_product) for the shoping cart later
        if self.n_inventory > 0:
            self.n_inventory -= 1
            if self.n_inventory < 15:   #note: add some 'if' statement for conditioning the shoping cart and restock inventory.
                self.inventory_status = "Low Stock"
                self.restock_inventory()
            return True
        else:
            print("Product out of stock!")
            return False

    def restock_inventory(self):
        if self.n_inventory < 5:
         print(f"Restocking {self.display_name}.")
         self.n_inventory += 10
         print(f"{self.display_name} inventory restocked. New inventory: {self.n_inventory}")

        else:
            print(f"No need to restock {self.display_name}. Inventory is sufficient.")  # Adds 10 items after the user has bought something, but only if the inventory is less than 5 (Only for Eletronic products)


class Computers(ElectronicProduct):    #hierarchy: computers---> ElectronicProduct ------> Catalogue
    def __init__(self, brand, type, display_name, price, n_inventory, inventory_status, bluetooth, wifi, hdmi_output,
                 ram_size, warranty):
        super().__init__(brand, type, display_name, price, n_inventory, inventory_status, warranty)     #note: computers class inherite from parent class, but some attributes need to be defined yet.
        self.bluetooth = bluetooth
        self.wifi = wifi
        self.hdmi_output = hdmi_output
        self.ram_size = ram_size

    def __str__(self):           #Note: add string method (__str__) to print computers data later, only to the attributes that were missing, or aren't included on inheritance from electronic parent class.
        return f' {super().__str__()}, Bluetooth: {self.bluetooth}, WIFI: {self.wifi}, HDMI output: {self.hdmi_output}, RAM size: {self.ram_size}'


class Tablets(ElectronicProduct):     #note: computers, tables and cellphones are subclasses of electronic product
    pass


class Cellphones(ElectronicProduct):     #hierarchy: Cellphones---> ElectronicProduct ------> Catalogue
    pass

# print('\n================ 3rd step:  BookProduct class creation =============')
class BookProduct:
    def __init__(self, area_of_study, display_name, publisher, author, price, isbn, n_inventory, inventory_status,language):  #note: we have to define new attributes since is a total new different class
        self.area_of_study = area_of_study
        self.display_name = display_name
        self.publisher = publisher
        self.author = author
        self.price = price
        self.isbn = isbn
        self.n_inventory = n_inventory
        self.inventory_status = inventory_status
        self.language = language

    def __str__(self):   #Note: add string method (__str__) to print Bookproduct data later,
        return f' {self.area_of_study}, {self.display_name}, {self.publisher}, {self.author}, ${self.price}, {self.isbn},{self.n_inventory},{self.inventory_status} {self.language}'

    def buy_product(self):
        if self.n_inventory > 0:
            self.n_inventory -= 1     #note: the assigment oerator (-=) indicates it will subtracted 1 when constumer buy the product.
            if self.n_inventory < 15:
                self.inventory_status = "Low Stock"
                self.restock_inventory()  # Shows "Low Stock" if the inventory is less than 15
            return True
        else:
            print("Product out of stock!")
            return False


    def restock_inventory(self):
        if self.n_inventory < 5:
            print(f"Restocking {self.display_name}.")
            self.n_inventory += 10
            print(f"{self.display_name} inventory restocked. New inventory: {self.n_inventory}")
        else:
            print(
                f"No need to restock {self.display_name}. Inventory is sufficient.")  # Adds 10 items after the user has bought something, but only if the inventory is less than 5 (Only for books)

# print('\n================ 4th step: shopping class creation =============')
class ShoppingCart:
    def __init__(self):
        self.items = []   # Note:add some default value, to later modify it, since will be the costumer choice

    def add_to_cart(self, product):  # here the creation of parameter product since will be called later.
        self.items.append(product)

    def display_cart(self):   # Note:here, the only parameter you have is the object itself.
        total = 0
        for item in self.items:
            print(f"{item.display_name}: ${item.price}")
            total += item.price
        print(f"Total: ${total}")

    def clear_cart(self):
        self.items = []  # Show the items in the cart and adds more when the used chooses to, plus, it clears everything after it has completed the transaction


# print('\n================ 5th step: payment card class creation =============')
class PaymentCard:
    def __init__(self, card_number, expiry_date, card_holder_name, card_balance):
        self.__card_number = card_number
        self.__expiry_date = expiry_date
        self.__card_holder_name = card_holder_name
        self.card_balance = card_balance

    def get_card_number(self):                  # encapsulation define setter and getter in our attributes to keep it private.
        return self.__card_number

    def set_card_number(self, card_number):
        self.__card_number = card_number

    def get_expiry_date(self):
        return self.__expiry_date

    def set_expiry_date(self, expiry_date):
        self.__expiry_date = expiry_date

    def get_card_holder_name(self):
        return self.__card_holder_name

    def set_card_holder_name(self, card_holder_name):
        self.__card_holder_name = card_holder_name

    def validate_card_details(self):
        if len(self.__card_number) != 16:
            print("Invalid card number. It must be 16 digits.")
            return False
        try:
            exp_date = datetime.strptime(self.__expiry_date, "%m/%y").date()
            if exp_date < dt_date.today():
                print("Invalid expiry date. The card is expired.")
                return False
        except ValueError:
            print("Invalid expiry date format. Use MM/YY.")
            return False
        return True

    def process_payment(self, order_total):
        if order_total > self.card_balance:
            print("Payment declined. Insufficient funds.")
            return False
        else:
            self.card_balance -= order_total
            return True  # Returns False if the card has less money than the order and True if it has more money

    def __str__(self):
        return f'Card Number: {self.__card_number}, Expiry Date: {self.__expiry_date}, Card Holder Name: {self.__card_holder_name}, Card Balance: ${self.card_balance}'

# print('\n================ 6th step: delivery service cost class creation =============')
class DeliveryService:
    def calculate_shipping_cost(self, order_total):
        if order_total >= 100:
            return 0
        else:
            return 10  # Returns the value of the delivery service, if the total order is >100, it returns 0
class Address:
    def __init__(self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state} {self.zip_code}"

# print('\n================ 7th step: delivery service sample or object creation =============')
# List of electronic products
laptops = Computers("BrandA", "Laptop", "ModelX", 999, 10, "In Stock", "Y", "Y", "N", "2GB RAM", "Warranty of 2 Years")
macbook = Computers("BrandB", "Macbook", "ModelY", 1299, 5, "Low Stock", "Y", "Y", "N", "2GB RAM",
                    "Warranty of 2 Years")
chromebook = Computers("BrandC", "Chromebook", "ModelZ", 699, 20, "In Stock", "Y", "Y", "N", "2GB RAM",
                       "Warranty of 2 Years")
amazon_fire = Tablets("BrandX", "Tablet", "Fire", 199, 15, "In Stock", "Warranty of 2 Years")
ipad = Tablets("BrandY", "Tablet", "Model2024", 799, 8, "Low Stock", "Warranty of 2 Years")
samsung_galaxy = Tablets("BrandZ", "Tablet", "Galaxy Tab", 499, 12, "In Stock", "Warranty of 2 Years")
iphone = Cellphones("BrandX", "Smartphone", "iPhone11", 999, 10, "In Stock", "Warranty of 2 Years")
samsung_galaxy_phone = Cellphones("BrandY", "SmartphoneX", "Galaxy", 899, 15, "In Stock", "Warranty of 2 Years")
google_pixel = Cellphones("BrandZ", "Smartphone", "Pixel2024", 799, 20, "In Stock", "Warranty of 2 Years")
devices_5g = Cellphones("BrandA", "Smartphone", "5G Device", 899, 8, "Low Stock", "Warranty of 2 Years")

# List of book products
statistics = BookProduct("Mathematics", "Statistics", "PublisherX", "AuthorX", 29.99, "ISBNX", 30, "In Stock", "English")
machine_learning = BookProduct("Mathematics", "Machine Learning", "PublisherY", "AuthorY", 39.99, "ISBNY", 40, "In Stock","English")
microeconomics = BookProduct("Economics", "Microeconomics", "PublisherZ", "AuthorZ", 19.99, "ISBNZ", 60, "In Stock", "English")
macroeconomics = BookProduct("Economics", "Macroeconomics", "PublisherW", "AuthorW", 29.99, "ISBNW", 70, "In Stock", "English")

# print('\n================ 8th step: Menu displayed creation I PART =============')

print("WELCOME! Here we are focused on 2 different types of products and we can guarantee we have the best of them")
cart =ShoppingCart()
while True:                     # note: add while loop statement, 'If' statement and other logical operator to condition the costumer's choice
    print("Please select an action by entering a number:")
    print("1 to view products")
    print("2 to buy a product")
    print("3 to view shopping cart and checkout")
    print("4 to exit")
    choice = input("Enter your choice: ")

    if choice == "1":  # Note: view products option
        while True:
            print("Please select a category:")
            print("1 for Electronics")
            print("2 for Books")
            print("0 to go back to initial menu")
            category_choice = input("Enter your choice: ")

            # note: menu diplayed creation for electronics (option 1)

            if category_choice == "1":
                while True:
                    print("Please select a subcategory:")
                    print("1 for Computers")
                    print("2 for Tablets")
                    print("3 for Cellphones")
                    print("0 to go back to categories")
                    subcategory_choice = input("Enter your choice: ")

                    if subcategory_choice == "1":
                        print("Computers information here:")
                        print(laptops)
                        print(macbook)
                        print(chromebook)
                    elif subcategory_choice == "2":
                        print("Tablets information here:")
                        print(amazon_fire)
                        print(ipad)
                        print(samsung_galaxy)
                    elif subcategory_choice == "3":
                        print("Cellphones information here:")
                        print(iphone)
                        print(samsung_galaxy_phone)
                        print(google_pixel)
                        print(devices_5g)
                    elif subcategory_choice == "0":
                        break
                    else:
                        print("Invalid choice!")

                    more_products = input("Would you like to see more products? (yes/no): ")
                    if more_products.lower() != "yes":  # Let the user view all eletronics and return to previous menu in case it is needed
                        break

                     # note: menu diplayed creation for book product (option 2)
            elif category_choice == "2":
                while True:
                    print("Please select a subcategory:")
                    print("1 for Computer Science")
                    print("2 for Mathematics")
                    print("3 for Economics")
                    print("0 to go back to categories")
                    subcategory_choice = input("Enter your choice: ")

                    if subcategory_choice == "1":
                        print("We don't have any book available right now")
                    elif subcategory_choice == "2":
                        print("Mathematics books information here:")
                        print(statistics)
                        print(machine_learning)
                    elif subcategory_choice == "3":
                        print("Economics books information here:")
                        print(microeconomics)
                        print(macroeconomics)
                    elif subcategory_choice == "0":
                        break
                    else:
                        print("Invalid choice!")

                    more_products = input("Would you like to see more products? (yes/no): ")
                    if more_products.lower() != "yes":  # Let the user view all books and return to previous menu in case it is needed
                        break
            elif category_choice == "0":
                break
            else:
                print("Invalid choice!")
        # print('\n================ 8th step: Menu displayed creation II PART =============')
    elif choice == "2":   # Note: buy a product option
        cart = ShoppingCart()
        while True:
            print("Please select a product to buy:")
            print("1 for ModelX Laptop")
            print("2 for ModelY Macbook")
            print("3 for ModelZ Chromebook")
            print("4 for Fire Tablets")
            print("5 for iPads")
            print("6 for Samsung Galaxy Tablets")
            print("7 for iPhones")
            print("8 for Samsung Galaxy Phones")
            print("9 for Google Pixel Phones")
            print("10 for 5G Devices")
            print("11 for Statistics Book")
            print("12 for Machine Learning Book")
            print("13 for Microeconomics Book")
            print("14 for Macroeconomics Book")
            print("0 to go back")
            product_choice = input("Enter your choice: ")
            print("")
            if product_choice == "1":
                cart.add_to_cart(laptops)
            elif product_choice == "2":
                cart.add_to_cart(macbook)
            elif product_choice == "3":
                cart.add_to_cart(chromebook)       # Note:In the option to buy, we made use of polymorphism,
            elif product_choice == "4":            # since we call the function definition 'add_to_card' but has different behaviour (or price) in diffrent objects or products.
                cart.add_to_cart(amazon_fire)
            elif product_choice == "5":
                cart.add_to_cart(ipad)
            elif product_choice == "6":
                cart.add_to_cart(samsung_galaxy)
            elif product_choice == "7":
                cart.add_to_cart(iphone)
            elif product_choice == "8":
                cart.add_to_cart(samsung_galaxy_phone)
            elif product_choice == "9":
                cart.add_to_cart(google_pixel)
            elif product_choice == "10":
                cart.add_to_cart(devices_5g)
            elif product_choice == "11":
                cart.add_to_cart(statistics)
            elif product_choice == "12":
                cart.add_to_cart(machine_learning)
            elif product_choice == "13":
                cart.add_to_cart(microeconomics)
            elif product_choice == "14":
                cart.add_to_cart(macroeconomics)
            elif product_choice == "0":
                break
            else:
                print("Invalid choice. Please enter a valid option.")
            print("Product added to cart successfully!")
            print("")
            choice_add_more = input("Do you want to buy more products? (Y/N): ")
            if choice_add_more.upper() != "Y":
                break  # Adds products to the cart for as long as the user wants
            print("")

    elif choice == "3":   #Note: view cart and checkout (option 3)
        if len(cart.items) == 0:
            print("Your cart is empty.")
        else:
            print("Shopping Cart:")
            cart.display_cart()
            total_price = sum(item.price for item in cart.items)
            print(f"Total Price: ${total_price}")
            delivery_service = DeliveryService()
            shipping_cost = delivery_service.calculate_shipping_cost(total_price)
            print(f"Shipping Cost: ${shipping_cost}")
            total_with_shipping = total_price + shipping_cost
            print(
                f"Total with Shipping: ${total_with_shipping}")  # Processes the total amount and adds the shipping cost in case it is less than 100

            card_number = input("Enter your 16-digit card number: ")
            expiry_date = input("Enter the card expiry date (MM/YY): ")
            card_holder_name = input("Enter card holder name: ")
            card_balance = float(input("Enter card balance: "))
            payment_card = PaymentCard(card_number, expiry_date, card_holder_name, card_balance)

            if payment_card.process_payment(total_with_shipping):
                print("Payment successful!")
                print("Order Summary:")
                for item in cart.items:
                    item.buy_product()
                cart.display_cart()
                print(f"Total Price: ${total_price}")
                print(f"New Card Balance: ${payment_card.card_balance}")  # Checks the card and processes the payment

                # Get delivery address details
                street = input("Enter your street address: ")
                city = input("Enter your city: ")
                state = input("Enter your state: ")
                zip_code = input("Enter your zip code: ")

                delivery_address = Address(street, city, state, zip_code)
                print(f"Your order will be shipped to: {delivery_address}")

                cart.clear_cart()
                for item in cart.items:
                    item.buy_product()  # rebuy iteams just bought
            else:
                print("Payment declined. Insufficient funds.")

    elif choice == "4":  # Note: exit (option 4)
        print("Thank you for shopping with us!")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
