'''
Given a string. the task is to check if the string is symmetrical and palindrome or not. A string
is said to be symmetrical if both the halves of the string are the same and a string is said to
be a palindrome string if one half of the string is the reverse of the other half or if a string
appears same when read forward or backward.
'''

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

