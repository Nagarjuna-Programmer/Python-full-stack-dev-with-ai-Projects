
# # The program uses three classes:
# # 1. Account          -> Parent class
# # 2. SavingsAccount  -> Child class
# # 3. Bank            -> Manages all accounts


# # ---------------- BANK MANAGEMENT SYSTEM ----------------


# # ---------------- PARENT CLASS ----------------

class Account:

    def __init__(self, username, password, balance=0):

        self.username = username
        self.password = password
        self.balance = balance
        self.transactions = []




    # # ---------------- DEPOSIT ----------------

    def deposit(self, amount):

        if amount > 0:

            self.balance += amount

            self.transactions.append(
                f"Deposited: {amount}"
            )

            print("Amount deposited:", amount)
            print("Current balance:", self.balance)

        else:

            print("Enter a valid amount")



    # # ---------------- WITHDRAW ----------------

    def withdraw(self, amount):

        if amount <= 0:

            print("Enter a valid amount")

        elif amount <= self.balance:

            self.balance -= amount

            self.transactions.append(
                f"Withdrawn: {amount}"
            )

            print("Amount withdrawn:", amount)
            print("Remaining balance:", self.balance)

        else:

            print("Insufficient balance")




    # # ---------------- CHECK BALANCE ----------------

    def check_balance(self):

        print("Current balance:", self.balance)



    # # ---------------- MINI STATEMENT ----------------

    def mini_statement(self):

        print("\n------ MINI STATEMENT ------")

        print("Username:", self.username)

        if len(self.transactions) == 0:

            print("No transactions")

        else:

            for transaction in self.transactions:

                print(transaction)

        print("Current Balance:", self.balance)


# # ---------------- CHILD CLASS ----------------

class SavingsAccount(Account):

    def __init__(self, username, password, balance=0):

        super().__init__(username, password, balance)



    # # ---------------- ACCOUNT TYPE ----------------

    def show_account_type(self):

        print("Account Type: Savings Account")


# # ---------------- BANK CLASS ----------------

class Bank:

    def __init__(self):

        self.accounts = {}


    # # ---------------- CREATE ACCOUNT ----------------

    def create_account(self, username, password):

        if username in self.accounts:

            print("Username already exists")

        else:

            account = SavingsAccount(username, password)

            self.accounts[username] = account

            print("Account created successfully")


    # # ---------------- LOGIN ----------------

    def login(self, username, password):

        if username in self.accounts:

            account = self.accounts[username]

            if account.password == password:

                print("Login successful")

                return account

            else:

                print("Invalid password")

        else:

            print("Invalid username")

        return None


# # ---------------- CREATE BANK OBJECT ----------------

bank = Bank()


# # ---------------- MAIN MENU ----------------

while True:

    print("\n------ PYTHON BANK ------")

    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")


    # # ---------------- CREATE ACCOUNT ----------------

    if choice == "1":

        username = input("Enter username: ")

        password = input("Enter password: ")

        bank.create_account(username, password)




    # # ---------------- LOGIN ----------------

    elif choice == "2":

        username = input("Enter username: ")

        password = input("Enter password: ")

        account = bank.login(username, password)




        if account is not None:

            while True:

                print("\n------ ACCOUNT MENU ------")

                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Mini Statement")
                print("5. Account Type")
                print("6. Logout")

                choice = input("Enter your choice: ")



                # # ---------------- DEPOSIT ----------------

                if choice == "1":

                    amount = int(
                        input("Enter amount: ")
                    )

                    account.deposit(amount)




                # # ---------------- WITHDRAW ----------------

                elif choice == "2":

                    amount = int(
                        input("Enter amount: ")
                    )

                    account.withdraw(amount)




                # # ---------------- CHECK BALANCE ----------------

                elif choice == "3":

                    account.check_balance()




                # # ---------------- MINI STATEMENT ----------------

                elif choice == "4":

                    account.mini_statement()


                # # ---------------- ACCOUNT TYPE ----------------

                elif choice == "5":

                    account.show_account_type()




                # # ---------------- LOGOUT ----------------

                elif choice == "6":

                    print("Logged out successfully")

                    break


                # # ---------------- INVALID ACCOUNT MENU ----------------

                else:

                    print("Invalid choice")


    # # ---------------- EXIT ----------------

    elif choice == "3":

        print("\nThank you for using Python Bank")

        break



    # # ---------------- INVALID MAIN MENU ----------------

    else:

        print("Invalid choice")

