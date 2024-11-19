print('Kalpak '+" Kannaujia")
print('-'*20)
print('Kalpak '*3)
print('-'*20)

#String length
print(f'The length of string is {len("Kalpak Kannaujia")}')
print(f'The length of string is {len(" Kalpak Kannaujia ")}')

#String slicing
print("Kalpak"[0])
print("Kalpak"[-2])
print("Kalpak Kannaujia"[0:7])
print("Kalpak Kannaujia"[:7])
print("Kalpak Kannaujia"[7:16])
print("Kalpak Kannaujia"[4:16])
print("Kalpak Kannaujia"[4:])
# print("Kalpak Kannaujia"[17])#Error index out of bounds
print("Kalpak Kannaujia"[-5:])
print('-'*20)

#Case conversion
print("Kalpak Kannaujia".lower())
print("Kalpak Kannaujia".upper())
print('-'*20)

#String stripping
print("    Kalpak Kannaujia     ")
print("    Kalpak Kannaujia     ".strip())
print('-'*20)

#String replacing
print("Kalpak Kannaujia")
print("Kalpak Kannaujia".replace('k','*'))
print("Kalpak Kannaujia".replace('K','*'))
print("Kalpak Kannaujia".replace('ak','**'))
print('-'*20)

#String count
print("Kalpak Kannaujia".count('k'))
print("Kalpak Kannaujia".lower().count('k'))
print('-'*20)

#String find
print("Kalpak Kannaujia".find('pak'))
print('-'*20)

#String check
print("Kalpak".isalpha())
print("1236544".isdigit())
print("kalpak".islower())
print("KALPAK".isupper())
print('-'*20)

#String Capitilization
print("kalpak kannaujia".capitalize())
print("kalpak kannaujia".title())
print('-'*20)

#Check for start and end
print("Kalpak Kannaujia".startswith("Ka"))
print("Kalpak Kannaujia".endswith("a"))
print('-'*20)

#Alignment
print("Kalpak Kannaujia".center(20,'*'))
print("Kalpak Kannaujia".ljust(20,'*'))
print("Kalpak Kannaujia".rjust(20,'*'))
print('-'*20)