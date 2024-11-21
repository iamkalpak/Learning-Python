#while loops
n = 30
i = 1
s = 0

while n>s:
    print(s)
    s+=i
    i+=1

#reverse a number
def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num
num = int(input("Enter number to reverse:"))
str_num = str(num)
print(str_num[::-1])
print(reverse_number(num))