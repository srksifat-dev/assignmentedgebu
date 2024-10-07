import math

def primeChecker(number):
    if number > 1:
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
                break
        return True
    else:
        return False

number = int(input("Enter a number: "))
if primeChecker(number):
    print("Prime")
else:
    print("Not Prime")

