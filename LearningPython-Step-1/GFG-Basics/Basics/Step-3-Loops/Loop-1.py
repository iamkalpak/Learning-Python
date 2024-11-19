#Table using different way
# n = int(input("Enter the no:"))
# n = 5
# for i in range(n,((n*10)+1),n):
#     print(i)


for i in range(1,7):
    for j in range(1,7):
        print(j, end=" ")
    print()

for i in range(1,6):
    for j in range(1,i):
        print("*", end=" ")
    print()

#If I roll 2 dices then in what cases the sum fof them will be 5
for n in range(1,13):
    countOfOccurrence = 0
    print(f"*****************Details of probability of getting {n} as sum:*****************")
    print(f"The pairs below will give the sum of {n}")
    for i in range(1, 7):
        for j in range(1, 7):
            if ((i + j) == n):
                countOfOccurrence += 1
                print("The pair is :(", i, ",", j, ")")


    print(f"Count of occurrence of getting {n} is :{countOfOccurrence}")
    print(f"% of chance to get {n} is :{round(((countOfOccurrence / (6*6)) * 100), 2)}%")


#If I roll 3 dices then in what cases the sum fof them will be 5
for n in range(1,19):
    countOfOccurrence = 0
    print(f"*****************Details of probability of getting {n} as sum:*****************")
    print(f"The pairs below will give the sum of {n}")
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1,7):
                if ((i + j + k) == n):
                    countOfOccurrence += 1

                    print("The pair is :(", i, ",", j,",", k,")")


    print(f"Count of occurrence of getting {n} is :{countOfOccurrence}")
    print(f"% of chance to get {n} is :{round(((countOfOccurrence / (6*6*6)) * 100), 2)}%")