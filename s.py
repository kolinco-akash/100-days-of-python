def shopping_cart():
    cart_items = []
    cart_prices = {}  # Store item prices in a dictionary

    def add_item(new_item, price):
        cart_items.append(new_item)
        cart_prices[new_item] = price
        print(f"Added '{new_item}' to the cart with a price of {price}.")

    def remove_item():
        if not is_empty():
            removed_item = cart_items.pop()
            print(f"Removed '{removed_item}' from the cart.")
            return removed_item
        else:
            print("The cart is empty. Cannot remove an item.")

    def view_cart():
        if not is_empty():
            print("Items in the cart:")
            for item in reversed(cart_items):
                print(f"- {item} (Price: {cart_prices[item]})")
        else:
            print("The cart is empty.")

    def price_calculation():
        total_items = len(cart_items)
        total_price = sum(cart_prices[item] for item in cart_items)
        print(f"Total items in the cart: {total_items}")
        print(f"Total price of the cart: {total_price}")

    def is_empty():
        return len(cart_items) == 0

    while True:
        print()
        print("Please type in one of these:")
        print("1. View cart")
        print("2. Add item")
        print("3. Remove Item")
        print("4. Price calculation")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            view_cart()

        elif choice == "2":
            item_to_add = input("Enter the item to add: ")
            price = float(input("Enter the price of the item: "))  # Assuming the price is a float
            add_item(item_to_add, price)

        elif choice == "3":
            removed_item = remove_item()
            if removed_item:
                print(f"Removed item: {removed_item}")
        elif choice == "4":
            price_calculation()
        elif choice == "5":
            print("Exiting the shopping cart.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


shopping_cart()
