def mullti(n):
    if n <= 0:
        print("Please enter a positive integer.")
        return

    for i in range(1, 11):
        result = n * i
        print(f"{n} x {i} = {result}")


number = int(input("Enter a positive integer: "))
mullti(number)
