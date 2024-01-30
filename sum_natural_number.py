def is_int(value):
    for char in value:
        if char < '0' or char > '9':
            return False
    return True

def sum_nn(n):
    if not is_int(n) or int(n) < 1:
        print("Please enter a positive integer.")
        return

    n = int(n)
    sum_natural = n * (n + 1) // 2
    print(f"The sum of the first {n} natural numbers is: {sum_natural}")

number = input("Enter a positive integer (N): ")
sum_nn(number)

