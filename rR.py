
shopping_cart = []


def add_item():
    item = input("Enter the item: ")
    price = float(input("Enter the price: "))
    shopping_cart.append((item, price))
    print(f"Added {item} to the shopping cart. Price: ${price:.2f}")


def remove_item():
    if shopping_cart:
        removed_item = shopping_cart.pop()
        print(f"Removed {removed_item[0]} from the shopping cart. Price: ${removed_item[1]:.2f}")
    else:
        print("Shopping cart is empty. Cannot remove.")


def view_cart():
    if shopping_cart:
        print("\nShopping Cart:")
        for item, price in reversed(shopping_cart):
            print(f"{item} - ${price:.2f}")
        print(f"Total Price: ${sum(price for _, price in shopping_cart):.2f}")
    else:
        print("Shopping cart is empty.")


while True:
    print("\nMenu:")
    print("1. Add Item")
    print("2. Remove Last Item")
    print("3. View Cart")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_item()
    elif choice == '2':
        remove_item()
    elif choice == '3':
        view_cart()
    elif choice == '4':
        print(" Goodbye!")
        break
    else:
        print("Invalid choice.")
