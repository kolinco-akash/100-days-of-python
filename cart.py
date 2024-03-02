print("Welcome to the Shopping Cart Program!")

available_items = ["apple", "banana", "orange", "grapes", "watermelon"]
cart = []

while True:
    print()
    print("Please type in one of these")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove Item")
    print("4. Compute total")
    print("5. Exit")

    select = int(input("Type in a number to proceed: "))

    if select == 1:
        while True:
            print("Available items:", available_items)
            item = input("What would you like to add? (Type 'ok' to finish) ")
            if item.lower() == "ok":
                break
            if item.lower() in available_items:
                price = float(input("Type in the price: $"))
                cart.append((item, price))
                print(f"'{item}' has been added to your cart. Price: ${price}")
            else:
                print(f"'{item}' is not in the available items. Please choose from the list.")

    elif select == 2:
        print("This is what is in your shopping cart:")
        for item, price in cart:
            print(f"{item} - ${price}")
        input("Press Enter when you're done.")

    elif select == 3:
        takeout = input("Type in what you would like to remove: ")
        cart = [(item, price) for item, price in cart if item != takeout]

    elif select == 4:
        total_price = sum(item[1] for item in cart)
        print(f"Total price in your cart: ${total_price}")
        input("Press Enter when you're done.")

    elif select == 5:
        print("Come back soon.")
        break
