# Palindrome Checker

def isPalindrome(valStr):
    if valStr == valStr[::-1]:
        return True
    else:
        return False


def toBinaryIfNumber(value):
    try:
        intValue = int(value)
        return bin(intValue).replace("0b", "")
    except ValueError:
        return "Not a number"


while True:

    txt = input("\nEnter a word or number: ")
    if txt.isalpha():
        if isPalindrome(txt):
            print(f"{txt} is a palindrome")
        else:
            print(f"{txt} is not a palindrome")
    elif txt.isnumeric():
        if isPalindrome(txt):
            print(f"Number {txt} is a palindrome")
        else:
            print
        print(f"Binary equivalent: {toBinaryIfNumber(txt)}")
        if isPalindrome(toBinaryIfNumber(txt)):
            print(f"Binary {toBinaryIfNumber(txt)} is a palindrome")
        else:
            print(f"Binary {toBinaryIfNumber(txt)} is not a palindrome")
