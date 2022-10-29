'''
Get an input and insert in list and print a list of all the powers of 2 with the
exponent ranging from 0 to n ( inclusive ).
'''

n = int(input('input: '))

listO = []

for i in range(n + 1):
    listO.append(2**i)
    #listO[i] = i**2

print (listO)






