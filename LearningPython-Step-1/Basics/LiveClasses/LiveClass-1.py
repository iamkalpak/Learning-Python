#Live class
ToDo_List = ["meeting", 'pay bills', "buy groceries", "clean house"]
ToDo_List.append("buy phone")
print(ToDo_List)
ToDo_List.remove('pay bills')
print(ToDo_List)
if 'meeting' in ToDo_List:
    print("Meeting is in the list")
    ToDo_List.remove('meeting')
else:
    print("Meeting is not in the list")
print(ToDo_List)

# grades = [20,30,60,90,45,45,85,75]
# grades.append(35)
# print(grades)
# print(len(grades))
# for i in grades:
#     sum = sum+i
# print(sum/ len(grades))
# print(max(grades))
# print((min(grades)))

#packing and unpacking tuple/list

#Nested lists and tuples
nested_list = [(1,2,3),[1,2,3],(1,"KK",True)]
print(type(nested_list[0]))
print(type(nested_list[1]))
print(type(nested_list[2]))
print(type(nested_list))