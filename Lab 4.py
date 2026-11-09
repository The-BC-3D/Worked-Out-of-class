
class Customer:
    def __init__(self, cid, cname, acc_no, balance):
        self.cid = cid
        self.cname = cname
        self.acc_no = acc_no
        self.balance = balance
        self.credit_card = []

    def transfer_funds(self, beneficiary_cust_object, amount):
        if amount <= 0:
            print("Invalid amount!")
        elif self.balance >= amount:
            self.balance -= amount
            beneficiary_cust_object.balance += amount
            print("Funds transferred successfully!")
        else:
            print("Insufficient balance!")


class Card:
    def __init__(self, card_no, cvv, expiry_date, balance):
        self.card_no = card_no
        self.cvv = cvv
        self.expiry_date = expiry_date
        self.balance = balance

customers = []
cards = []

while True:
    print("\n========== MAIN MENU ==========")
    print("1. Create Customer objects")
    print("2. Create Card objects")
    print("3. Transfer funds between customer objects")
    print("4. Assign card objects to customer objects")
    print("5. Display Customer Info")
    print("6. Display Card Info")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        cid = input("Enter Customer ID: ")
        cname = input("Enter Customer Name: ")
        acc_no = input("Enter Account Number: ")
        balance = float(input("Enter Balance: "))

        customer = Customer(cid, cname, acc_no, balance)
        customers.append(customer)

        print("Customer created successfully!")

    elif choice == "2":
        card_no = input("Enter Card Number: ")
        cvv = input("Enter CVV: ")
        expiry_date = input("Enter Expiry Date: ")
        balance = float(input("Enter Card Balance: "))

        card = Card(card_no, cvv, expiry_date, balance)
        cards.append(card)

        print("Card created successfully!")

    elif choice == "3":
        if len(customers) < 2:
            print("At least two customers are required!")
        else:
            print("\nCustomers:")
            for i, customer in enumerate(customers):
                print(i, "-", customer.cname)

            sender = int(input("Select sender index: "))
            receiver = int(input("Select beneficiary index: "))
            amount = float(input("Enter amount to transfer: "))

            if (0 <= sender < len(customers) and
                    0 <= receiver < len(customers) and
                    sender != receiver):

                customers[sender].transfer_funds(
                    customers[receiver], amount
                )
            else:
                print("Invalid customer selection!")

    elif choice == "4":
        if not customers or not cards:
            print("Create at least one customer and one card first!")
        else:
            print("\nCustomers:")
            for i, customer in enumerate(customers):
                print(i, "-", customer.cname)

            customer_index = int(input("Select customer index: "))

            print("\nCards:")
            for i, card in enumerate(cards):
                print(i, "-", card.card_no)

            card_index = int(input("Select card index: "))

            if (0 <= customer_index < len(customers) and
                    0 <= card_index < len(cards)):

                customers[customer_index].credit_card.append(
                    cards[card_index]
                )
                print("Card assigned successfully!")
            else:
                print("Invalid selection!")

    elif choice == "5":
        if not customers:
            print("No customers available!")
        else:
            for customer in customers:
                print("\nCustomer ID:", customer.cid)
                print("Customer Name:", customer.cname)
                print("Account Number:", customer.acc_no)
                print("Account Balance:", customer.balance)

                print("Assigned Cards:")
                if customer.credit_card:
                    for card in customer.credit_card:
                        print("Card Number:", card.card_no)
                else:
                    print("No cards assigned.")

    elif choice == "6":
        if not cards:
            print("No cards available!")
        else:
            for card in cards:
                print("\nCard Number:", card.card_no)
                print("CVV:", card.cvv)
                print("Expiry Date:", card.expiry_date)
                print("Card Balance:", card.balance)

    elif choice == "7":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
