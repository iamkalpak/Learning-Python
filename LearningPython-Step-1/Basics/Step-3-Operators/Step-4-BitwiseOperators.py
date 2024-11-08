# Initializing two numbers
a = 10  # In binary: 1010
b = 4   # In binary: 0100

# Bitwise AND (&)
result_and = a & b  # Only bits that are 1 in both numbers remain 1
print("Bitwise AND (a & b):", result_and)  # Output: 0

# Bitwise OR (|)
result_or = a | b  # Bits that are 1 in either number become 1
print("Bitwise OR (a | b):", result_or)  # Output: 14

# Bitwise XOR (^)
result_xor = a ^ b  # Bits that are different between a and b become 1
print("Bitwise XOR (a ^ b):", result_xor)  # Output: 14

# Bitwise NOT (~)
result_not = ~a  # Flips all bits in the number (two's complement representation)
print("Bitwise NOT (~a):", result_not)  # Output: -11

# Bitwise left shift (<<)
shift_left = a << 1  # Shifts all bits in 'a' to the left by 1 (equivalent to a * 2)
print("Left Shift (a << 1):", shift_left)  # Output: 20

# Bitwise right shift (>>)
shift_right = a >> 1  # Shifts all bits in 'a' to the right by 1 (equivalent to a // 2)
print("Right Shift (a >> 1):", shift_right)  # Output: 5
