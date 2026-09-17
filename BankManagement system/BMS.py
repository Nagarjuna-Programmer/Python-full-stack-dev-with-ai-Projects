# # This is a basic Bank Management System implemented using Python OOP concepts.
# # It allows users to create accounts, login, deposit money, withdraw money,
# # check balance, view mini statements, check account type, and logout.
# #
# # The program uses three classes:
# # 1. Account          -> Parent class
# # 2. SavingsAccount  -> Child class
# # 3. Bank            -> Manages all accounts
# #
# # The program demonstrates:
# # Class, Object, Constructor, Instance Variables, Methods,
# # Inheritance, super(), List, Dictionary, if-else, and while loop.


# # ---------------- BANK MANAGEMENT SYSTEM ----------------


# # ---------------- PARENT CLASS ----------------

class Account:

    def __init__(self, username, password, balance=0):

        self.username = username
        self.password = password
        self.balance = balance
        self.transactions = []

# # The Account class is the parent class.
# # The __init__() method is the constructor.
# # It runs automatically when an Account object is created.
# #
# # username stores the username of the customer.
# # password stores the password of the customer.
# # balance stores the current account balance.
# # transactions is an empty list used to store deposit and withdrawal details.


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

# # The deposit() method is used to deposit money into the account.
# # It takes amount as an argument.
# #
# # First, it checks whether the amount is greater than 0.
# # If the amount is valid, it is added to the account balance.
# #
# # The transaction is also stored inside the transactions list.
# # For example:
# # ["Deposited: 5000"]
# #
# # Finally, the deposited amount and updated balance are displayed.


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

# # The withdraw() method is used to withdraw money from the account.
# # It takes amount as an argument.
# #
# # First, it checks whether the amount is valid.
# # Then it checks whether sufficient balance is available.
# #
# # If the balance is sufficient, the amount is deducted from the balance.
# # The withdrawal transaction is also added to the transactions list.
# #
# # If the user tries to withdraw more money than the available balance,
# # the program displays "Insufficient balance".


    # # ---------------- CHECK BALANCE ----------------

    def check_balance(self):

        print("Current balance:", self.balance)

# # The check_balance() method displays the current balance of the account.
# # It uses self.balance to access the balance of the current account.


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

# # The mini_statement() method displays the transaction history of the account.
# #
# # First, it displays the username.
# # Then it checks whether the transactions list is empty.
# #
# # If there are no transactions, it displays "No transactions".
# #
# # Otherwise, the for loop goes through each transaction
# # in the transactions list and displays it.
# #
# # Finally, the current balance is displayed.
# #
# # Example:
# #
# # ------ MINI STATEMENT ------
# # Username: vasu
# # Deposited: 5000
# # Withdrawn: 1000
# # Deposited: 2000
# # Current Balance: 6000


# # ---------------- CHILD CLASS ----------------

class SavingsAccount(Account):

    def __init__(self, username, password, balance=0):

        super().__init__(username, password, balance)

# # SavingsAccount is the child class.
# # Account is the parent class.
# #
# # SavingsAccount inherits the properties and methods
# # from the Account class.
# #
# # Therefore, SavingsAccount can use:
# # deposit()
# # withdraw()
# # check_balance()
# # mini_statement()
# #
# # super() is used to call the constructor of the parent class.
# # It initializes username, password, balance, and transactions.


    # # ---------------- ACCOUNT TYPE ----------------

    def show_account_type(self):

        print("Account Type: Savings Account")

# # The show_account_type() method belongs to the SavingsAccount class.
# # It displays the type of account.
# #
# # This is an additional method provided by the child class.


# # ---------------- BANK CLASS ----------------

class Bank:

    def __init__(self):

        self.accounts = {}

# # The Bank class is used to manage all customer accounts.
# #
# # The accounts dictionary stores the username as the key
# # and the Account object as the value.
# #
# # Example:
# #
# # {
# #     "vasu": Account object,
# #     "rahul": Account object
# # }


    # # ---------------- CREATE ACCOUNT ----------------

    def create_account(self, username, password):

        if username in self.accounts:

            print("Username already exists")

        else:

            account = SavingsAccount(username, password)

            self.accounts[username] = account

            print("Account created successfully")

# # The create_account() method creates a new bank account.
# #
# # First, it checks whether the username already exists
# # in the accounts dictionary.
# #
# # If the username already exists, it displays:
# # "Username already exists"
# #
# # Otherwise, a new SavingsAccount object is created.
# #
# # The account object is then stored in the accounts dictionary.
# #
# # The username is used as the key and the account object
# # is stored as the value.


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

# # The login() method is used to authenticate the user.
# #
# # First, it checks whether the username exists in the dictionary.
# #
# # If the username exists, the corresponding Account object
# # is retrieved from the dictionary.
# #
# # Then the entered password is compared with the stored password.
# #
# # If both username and password are correct:
# #     Login successful
# #
# # The account object is returned.
# #
# # If the username or password is incorrect,
# # the appropriate error message is displayed.
# #
# # None is returned when login fails.


# # ---------------- CREATE BANK OBJECT ----------------

bank = Bank()

# # Here we create an object of the Bank class.
# # The object is stored in the variable named bank.
# #
# # We can now use:
# # bank.create_account()
# # bank.login()


# # ---------------- MAIN MENU ----------------

while True:

    print("\n------ PYTHON BANK ------")

    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

# # The while True loop continuously displays the main menu.
# # The loop continues until the user selects the Exit option.
# #
# # The user gets three options:
# # 1. Create Account
# # 2. Login
# # 3. Exit


    # # ---------------- CREATE ACCOUNT ----------------

    if choice == "1":

        username = input("Enter username: ")

        password = input("Enter password: ")

        bank.create_account(username, password)

# # If the user selects option 1,
# # the program asks for username and password.
# #
# # Then the create_account() method of the Bank object is called.
# #
# # The username and password are passed as arguments.


    # # ---------------- LOGIN ----------------

    elif choice == "2":

        username = input("Enter username: ")

        password = input("Enter password: ")

        account = bank.login(username, password)

# # If the user selects option 2,
# # the program asks for username and password.
# #
# # The login() method checks the entered details.
# #
# # If login is successful, it returns the Account object.
# # That object is stored in the account variable.


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

# # If login is successful, the account menu is displayed.
# #
# # The account menu contains:
# # 1. Deposit
# # 2. Withdraw
# # 3. Check Balance
# # 4. Mini Statement
# # 5. Account Type
# # 6. Logout
# #
# # Another while loop is used here so that the user can
# # perform multiple banking operations after logging in.


                # # ---------------- DEPOSIT ----------------

                if choice == "1":

                    amount = int(
                        input("Enter amount: ")
                    )

                    account.deposit(amount)

# # If the user selects option 1,
# # the program asks for the deposit amount.
# #
# # The deposit() method of the Account object is called.
# # The amount is passed as an argument.
# #
# # Example:
# # account.deposit(5000)


                # # ---------------- WITHDRAW ----------------

                elif choice == "2":

                    amount = int(
                        input("Enter amount: ")
                    )

                    account.withdraw(amount)

# # If the user selects option 2,
# # the program asks for the withdrawal amount.
# #
# # The withdraw() method is called using the Account object.
# #
# # Example:
# # account.withdraw(1000)


                # # ---------------- CHECK BALANCE ----------------

                elif choice == "3":

                    account.check_balance()

# # If the user selects option 3,
# # the check_balance() method is called.
# #
# # It displays the current account balance.


                # # ---------------- MINI STATEMENT ----------------

                elif choice == "4":

                    account.mini_statement()

# # If the user selects option 4,
# # the mini_statement() method is called.
# #
# # It displays the username, all transactions,
# # and the current account balance.


                # # ---------------- ACCOUNT TYPE ----------------

                elif choice == "5":

                    account.show_account_type()

# # If the user selects option 5,
# # the show_account_type() method is called.
# #
# # This method belongs to the SavingsAccount child class.
# #
# # It displays:
# # Account Type: Savings Account
# #
# # This demonstrates that the child class can have
# # its own methods in addition to inherited methods.


                # # ---------------- LOGOUT ----------------

                elif choice == "6":

                    print("Logged out successfully")

                    break

# # If the user selects option 6,
# # the user is logged out.
# #
# # The break statement exits the inner while loop
# # and takes the user back to the main bank menu.


                # # ---------------- INVALID ACCOUNT MENU ----------------

                else:

                    print("Invalid choice")

# # If the user enters a choice other than 1 to 6,
# # the program displays "Invalid choice".


    # # ---------------- EXIT ----------------

    elif choice == "3":

        print("\nThank you for using Python Bank")

        break

# # If the user selects option 3 from the main menu,
# # the program displays a thank-you message.
# #
# # The break statement exits the outer while loop
# # and completely stops the program.


    # # ---------------- INVALID MAIN MENU ----------------

    else:

        print("Invalid choice")

# # If the user enters a choice other than 1, 2, or 3,
# # the program displays "Invalid choice".


# # ---------------- FINISHED ----------------
# # ---------------- THANK YOU ----------------