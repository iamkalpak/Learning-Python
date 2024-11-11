# Example of basic if statement
x = 10
print("Basic if statement:")
if x > 5:
    print("x is greater than 5")
print("\n")

# Example of if-else statement
y = 3
print("If-else statement:")
if y > 5:
    print("y is greater than 5")
else:
    print("y is not greater than 5")
print("\n")

# Example of if-elif-else statement
z = 7
print("If-elif-else statement:")
if z > 10:
    print("z is greater than 10")
elif z == 7:
    print("z is equal to 7")
else:
    print("z is less than 10 and not equal to 7")
print("\n")

# Example of nested if statements
a = 15
b = 20
print("Nested if statement:")
if a > 10:
    print("a is greater than 10")
    if b > 15:
        print("b is also greater than 15")
print("\n")

# Example of using conditional expressions (ternary operator)
c = 5
d = 12
print("Conditional expression (ternary operator):")
result = "c is greater than d" if c > d else "c is not greater than d"
print(result)
