'''
Given a string and we need to reverse words of a given string
Examples:
Input : "Python is a programming language "
Output : language programming a is Python
'''
 
string = input('input string: ')
#stack for help to reverse string
stack = []

temp = ''
string += ' ' 
for x in string:

    if x != ' ':
        temp += x
    else:
        stack.append(temp)
        temp = ''



string = ''
while len(stack):
    string += (stack.pop() + ' ') 
     

print (string)





