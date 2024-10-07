def multiplierUpto10(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

number = int(input("Enter a number: "))
multiplierUpto10(number)
