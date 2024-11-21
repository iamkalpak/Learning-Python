# For loop demonstration: Print numbers 1 to 5
print("For loop:")
for i in range(1, 6):
    print(i, end=" ")
print("\n")

# While loop demonstration: Print numbers 1 to 5
print("While loop:")
i = 1
while i <= 5:
    print(i, end=" ")
    i += 1
print("\n")

# Simulated Do-While loop demonstration: Print numbers 1 to 5
# Python doesn't have a do-while loop, so we use a while loop to simulate it.
print("Do-While loop (simulated):")
i = 1
while True:
    print(i, end=" ")
    i += 1
    if i > 5:
        break
print("\n")

# Recursion demonstration: Print numbers 1 to 5
def recursive_loop(n):
    if n > 5:
        return
    print(n, end=" ")
    recursive_loop(n + 1)

print("Recursion loop:")
recursive_loop(1)
