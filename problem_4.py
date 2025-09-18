def isPalindrome(valStr):
    return valStr == valStr[::-1]

def toBinaryIfNumber(value):
    if value.isdigit():
        num = int(value)
        return bin(num)[2:]
    else:
        return None

user_input = input("Enter a value: ")

if isPalindrome(user_input):
    print("Input is a palindrome: True")
else:
    print("Input is a palindrome: False")

binary_val = toBinaryIfNumber(user_input)
if binary_val is not None:
    print("Binary equivalent:", binary_val)
    if isPalindrome(binary_val):
        print("Binary is a palindrome: True")
    else:
        print("Binary is a palindrome: False")
else:
    print("(No binary conversion since input is text)")
