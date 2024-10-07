def findSecondLargestNumber(numbers):
    if len(numbers) > 1:
        numbers.sort()
        return numbers[-2]
    else:
        return None

numbers = list(map(int, input("Enter a list of numbers: ").split(",")))
secondLargestNumber = findSecondLargestNumber(numbers)
print(secondLargestNumber)