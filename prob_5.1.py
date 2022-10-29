'''
Create a Python program to repeat M characters of string N times.
'''

def repeat(string, index, N):

    tempString = ''

    i = 0
    while (i < len(string)):
        
        if(i == index):
            while(N > 0):
                
                tempString += string[i]
                N -= 1
        else:
            tempString += string[i]
        
        i += 1
        
    return tempString

 
def repeatString(string, M, N):
    
    temp = ''

    listIndex = []
    i = 0
    while( i < len(string)):

        if(string[i] == M):
            
            string = repeat(string, i, N)
            i += N
        
        i += 1

    return string
 



string = input('input string: ')
M = input("letter: ")
N = int(input('input N: '))
newString = repeatString(string, M, N)
print (newString)

