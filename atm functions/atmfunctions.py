balance = 0
mini_statement = []


def credit():
    global balance

    amount = float(input("Enter amount to credit: "))

    if amount <= 0:
        print("Please enter a positive amount.")

    else:
        balance += amount
        mini_statement.append(f"Credited: ${amount}")
        print(f"${amount} credited to your account.")


def debit():
    global balance

    amount = float(input("Enter amount to debit: "))

    if amount <= 0:
        print("Please enter a positive amount.")

    elif amount > balance:
        print("Insufficient balance.")

    else:
        balance -= amount
        mini_statement.append(f"Debited: ${amount}")
        print(f"${amount} debited from your account.")


def check_balance():
    print(f"Your current balance is: ${balance}")


def show_mini_statement():
    print("\n------ MINI STATEMENT ------")

    if len(mini_statement) == 0:
        print("No transactions found.")

    else:
        for i in mini_statement:
            print(i)

    print(f"Available Balance: ${balance}")


def menu():
    while True:

        print("\nATM Menu:")
        print("1. Credit")
        print("2. Debit")
        print("3. Balance")
        print("4. Mini Statement")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            credit()

        elif choice == '2':
            debit()

        elif choice == '3':
            check_balance()

        elif choice == '4':
            show_mini_statement()

        elif choice == '5':
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Function Calling
menu()