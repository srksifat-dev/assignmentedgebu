def palindromeChecker(s):
    s = s.lower()
    s = s.strip()
    if s == s[::-1]:
        return True
    else:
        return False

word = input("Enter a string: ")
print(palindromeChecker(word))