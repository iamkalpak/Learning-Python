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

def numberOfSubsequences(S,W):
        S=list(S)
        W=list(W)
        ans=0
    
        while True:  #  Untill no such subsequence exist
            i=0
            j=0
            flag=0
            while i<len(S):
                if S[i]==W[j]:
                    j+=1
                    S[i]='*'
                    if j==len(W):
                        ans+=1   # A subsequence found
                        flag=1
                        break
                i+=1
            if flag==0:   # No subsequence found in this iteration
                break    
        return ans  

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