def gcdFinder(number1,number2):
    smallerNumebr = min(number1,number2)
    for i in range(smallerNumebr,0,-1):
        if number1 % i == 0 and number2 % i == 0:
            return i

numbers = list(map(int,input("Enter two numbers: ").split(",")))
print(f"GCD of {numbers[0]} and {numbers[1]} is : {gcdFinder(numbers[0],numbers[1])}")