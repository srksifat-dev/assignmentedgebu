def digitCounter(s):
    digits = 0
    for char in s:
        if char.isdigit():
            digits += 1
    return digits

word = input("Enter a random string: ")
print(f"Total digits are : {digitCounter(word)}")