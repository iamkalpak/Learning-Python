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

def changeCase(s):
    firstLetterCap = s.capitalize()
    upperCaseString = s.upper()
    print(firstLetterCap)
    print(upperCaseString)

def alphabets(c1, c2):
    start = ord(c1)  # Convert the start character to its ASCII value
    end = ord(c2)    # Convert the end character to its ASCII value
    for i in range(start, end + 1):
        print(chr(i), end=" ")  # Convert back to character and print on the same line

def numberOfSubsequences(S, W):
    n, m = len(S), len(W)  # Get the lengths of S and W
    count = 0  # Initialize count to store the number of times W appears as a subsequence
    i = 0  # This pointer will go through the characters in S

    while i < n:
        j = 0  # This pointer will go through the characters in W from the beginning
        
        # Try to match W as a subsequence in S starting from current i
        start_index = i  # Start from current i to avoid reuse
        while start_index < n and j < m:
            if S[start_index] == W[j]:  # If characters in S and W match
                j += 1  # Move to the next character in W
            start_index += 1  # Always move to the next character in S

        # If we completed W as a subsequence
        if j == m:
            count += 1  # We found one subsequence, increase count
            i = start_index  # Continue search from end of found subsequence
        else:
            break  # No further subsequences possible if W couldn't be completed

    return count  # Return the total count of subsequences

def numberOfSubseq(S, W):
    endOfS, endOfW = len(S),len(W)
    startOfS = 0
    # print(endOfS, endOfW, startOfS)
    while startOfS < endOfS:
        startOfW = 0
        while (startOfW < endOfW) & (startOfS<endOfS):
            if W[startOfW]==S[startOfS]:
                startOfW+=1
            else:
                continue


# numToCheck = int(input("Enter number to check palindrome:"))

# print(checkPalindrome(numToCheck))
# print(isPalindrome(numToCheck))

# changeCase("kalpak")
# print("kalpak".capitalize())

# alphabets("a",'z')

S = "abcdrtbwerrcokokokd"
W = "bcd"
# print(numberOfSubsequences(S, W))
print(numberOfSubseq(S, W))