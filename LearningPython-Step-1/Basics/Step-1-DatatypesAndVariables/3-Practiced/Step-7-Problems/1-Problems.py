def checkPalindrome(num):
    original_num = num#copy the orignal num
    reversed_num = 0#initialize rev to 0
    while num > 0:#while num is greater than 0
        digit = num % 10 #extract last digit
        reversed_num = reversed_num * 10 + digit #store in reversed order
        num //= 10 #remove the laat digit
    return original_num == reversed_num

def isPalindrome(num):
    str_num = str(num)#convert to string
    return str_num == str_num[::-1]#check reversed string is equal to orignal one

numToCheck = int(input("Enter number to check palindrome:"))

print(checkPalindrome(numToCheck))
print(isPalindrome(numToCheck))

def changeCase(s):
    firstLetterCap = s.capitalize()
    upperCaseString = s.upper()
    print(firstLetterCap)
    print(upperCaseString)

changeCase("kalpak")
print("kalpak".capitalize())