 
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





