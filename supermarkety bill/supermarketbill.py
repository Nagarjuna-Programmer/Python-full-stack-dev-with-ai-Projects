name = input("Enter your name: ")

# list of items
list = '''
Wheat       Rs 45/kg
Tomato      Rs 35/kg
Potato      Rs 30/kg
Milk        Rs 60/litre
Biscuits    Rs 20/pack
Soap        Rs 35/piece
Shampoo     Rs 80/bottle
Tea         Rs 120/pack
Coffee      Rs 150/pack
'''

# declaration
price = 0
totalprice = 0
item_list = []
quantity_list = []
price_list = []

# rate for each item
items = {
    'wheat': 45,
    'tomato': 35,
    'potato': 30,
    'milk': 60,
    'biscuits': 20,
    'soap': 35,
    'shampoo': 80,
    'tea': 120,
    'coffee': 150
}

while True:
    option = input("Press 1 for list or 2 to exit: ")

    if option == '2':
        print("Thank you for shopping")
        break

    elif option == '1':
        print(list)

        while True:
            inpt_1 = input("To buy press 1 or 2 to exit: ")

            if inpt_1 == '2':
                print("Thank you for shopping")
                break

            elif inpt_1 == '1':
                item = input("Choose your item: ").lower()

                if item in items:
                    quantity_input = input("Please enter quantity: ")

                    if quantity_input.isdigit():
                        quantity = int(quantity_input)

                        price = quantity * items[item]
                        totalprice += price

                        item_list.append(item)
                        quantity_list.append(quantity)
                        price_list.append(price)

                    else:
                        print("Please enter valid quantity.")

                else:
                    print("Selected item is not available.")

        if totalprice > 0:
            tax = (totalprice * 18) / 100
            final_amount = totalprice + tax

            print("=" * 50)
            print("             SUPER MARKET")
            print("=" * 50)

            print("Name:", name)
            print("-" * 50)

            print("S.No    Item        Quantity       Price")
            print("-" * 50)

            for i in range(len(item_list)):
                print(i + 1, "     ", item_list[i],
                      "       ", quantity_list[i],
                      "       ", price_list[i])

            print("-" * 50)
            print("Total Amount: Rs", totalprice)
            print("Tax Amount:   Rs", round(tax))
            print("Final Amount: Rs", round(final_amount))

            print("-" * 50)
            print("       Thank you and visit again")
            print("-" * 50)

            break