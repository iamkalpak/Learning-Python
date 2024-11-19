#Converting one type of data to another

# type_conversion_examples.py

# 1. Implicit Type Conversion
print("1. Implicit Type Conversion")
num_int = 10
num_float = 2.5
result = num_int + num_float
print(result)          # Output: 12.5
print(type(result))    # Output: <class 'float'>
print()

# 2a. Converting String to Integer
print("2a. Converting String to Integer")
str_num = "50"
int_num = int(str_num)
print(int_num)          # Output: 50
print(type(int_num))    # Output: <class 'int'>
print()

# 2b. Converting Integer to String
print("2b. Converting Integer to String")
num = 123
str_num = str(num)
print(str_num)          # Output: '123'
print(type(str_num))    # Output: <class 'str'>
print()

# 2c. Converting Float to Integer
print("2c. Converting Float to Integer")
float_num = 9.8
int_num = int(float_num)
print(int_num)          # Output: 9 (truncated, not rounded)
print(type(int_num))    # Output: <class 'int'>
print()

# 2d. Converting List to Tuple
print("2d. Converting List to Tuple")
list_data = [1, 2, 3, 4]
tuple_data = tuple(list_data)
print(tuple_data)       # Output: (1, 2, 3, 4)
print(type(tuple_data)) # Output: <class 'tuple'>
print()

# 2e. Converting Tuple to List
print("2e. Converting Tuple to List")
tuple_data = (1, 2, 3, 4)
list_data = list(tuple_data)
print(list_data)        # Output: [1, 2, 3, 4]
print(type(list_data))  # Output: <class 'list'>
print()

# 2f. Converting Integer to Float
print("2f. Converting Integer to Float")
int_num = 5
float_num = float(int_num)
print(float_num)        # Output: 5.0
print(type(float_num))  # Output: <class 'float'>
print()

# 2g. Converting List of Characters to String
print("2g. Converting List of Characters to String")
char_list = ['H', 'e', 'l', 'l', 'o']
str_data = ''.join(char_list)
print(str_data)         # Output: 'Hello'
print(type(str_data))   # Output: <class 'str'>
print()

# 2h. Converting Dictionary Keys to List
print("2h. Converting Dictionary Keys to List")
dict_data = {'a': 1, 'b': 2, 'c': 3}
keys_list = list(dict_data.keys())
print(keys_list)        # Output: ['a', 'b', 'c']
print(type(keys_list))  # Output: <class 'list'>
print()

# 2i. Converting Set to List
print("2i. Converting Set to List")
set_data = {1, 2, 3, 4}
list_data = list(set_data)
print(list_data)        # Output: [1, 2, 3, 4] (order may vary)
print(type(list_data))  # Output: <class 'list'>
print()

# 2j. Converting Boolean to Integer
print("2j. Converting Boolean to Integer")
bool_val = True
int_val = int(bool_val)
print(int_val)          # Output: 1
print(type(int_val))    # Output: <class 'int'>
print()