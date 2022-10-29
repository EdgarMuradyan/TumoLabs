'''
Given a string (s), find the length of the longest substring without repeating characters.
'''

def check(s, checkList):
 
    for i in checkList:
        if s == i:
            return 0
    
    checkList.append(s)
    return 1
 
def findeLongLength(l):
    maxLength = l[0]
    
    for i in l:
        if i > maxLength:
            maxLength = i
    return maxLength

def substring(S):
    lengthList = []
    length = 0
    i = 0
    while(i < len(S) - 1):
        checkList = []
     
        while check(S[i], checkList) and (i < len(S) - 1):         
            length += 1
            i += 1

        lengthList.append(length)
        length = 0  
        i += 1
    
    print ( findeLongLength(lengthList) )

    
     
S = "abcabcbb"
print (S)
substring(S)


















