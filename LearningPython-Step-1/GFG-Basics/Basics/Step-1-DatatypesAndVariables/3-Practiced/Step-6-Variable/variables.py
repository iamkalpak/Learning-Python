a,b=20,10
x=0
y=0
z=0
print(f'The values are a={a}, b={b}, x={x}, y={y}, z={z}')
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)

x=y=z = 6
print(x,y,z)
print(f'The values are x={x}, y={y}, z={z}')

data = [1,2,3,4]
print(data)
a,b,c,d = data #unpacking
print(a,b,c,d)

#user input
firstNum = float(input("Enter first number:"))#values typecasted
secondNum = float(input("Enter second number:"))#values typecasted

sumOfNum = firstNum+secondNum
print(sumOfNum)

'''
Rules to keep in mind wile naming variable 
1. Use either snake_case or camelCase
2. It should not start with a number
3. No python constants
4. It should start with a letter or a underscore(_)
'''