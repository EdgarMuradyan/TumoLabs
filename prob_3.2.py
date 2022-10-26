 

def isPolindrome(string):
     
    length = len(string)
     
    for i in range(int((length)/2)):
         
        if(string[i] != string[length - 1 - i]):
             
            return 0
    
    return 1
 
 
def isSymmetrical(string):
    print(string)
    length = len(string)
    if length%2 != 0:
        return 0

    for i in range(int((length)/2)):
        
        if(string[i] != string[int(length/2 + i)]):
             
            return 0
    
    return 1


 

string = input("input string: ")
 
print ("Symmetrical: ", isSymmetrical(string))

print ("Polindrom: ", isPolindrome(string))

