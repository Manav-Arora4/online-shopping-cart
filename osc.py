class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate(self, username, password):
        return self.username == username and self.password == password


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def view_cart(self):
        return self.items


class PaymentGateway:
    def process_payment(self, amount, payment_option):
        return f"Payment of {amount} via {payment_option} processed successfully"


class Customer(User, Cart, PaymentGateway):
    def __init__(self, username, password):
        User.__init__(self, username, password)
        Cart.__init__(self)

    def select_payment_option(self):
        while True:
            payment_option = input("Choose payment option (UPI/Credit Card/Debit Card/Cash): ").lower()
            if payment_option in ['upi', 'credit card', 'debit card', 'cash']:
                return payment_option
            else:
                print("Invalid payment option. Please choose from the provided options.")

    def purchase_items(self):
        total_amount = sum(item['price'] for item in self.items)
        payment_option = self.select_payment_option()
        return self.process_payment(total_amount, payment_option)


username = input("Enter your username: ")
password = input("Enter your password: ")

customer = Customer(username, password)
customer.add_item({"name": "Laptop", "price": 50000})
customer.add_item({"name": "Mouse", "price": 2000})
if customer.authenticate(username, password):
    print("Authentication successful.")
    print("Items in cart:", customer.view_cart())
    print("Payment result:", customer.purchase_items())
else:
    print("Authentication failed.")
