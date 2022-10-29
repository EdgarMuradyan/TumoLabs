'''
Given an array of integers of any length, return an array that has 1 added to the value
represented by the array.
the array can&#39;t be empty
only non-negative, single digit integers are allowed
Return None for invalid inputs.
'''

def list_to_number(Arr):
    number = 0
    
    i = len(Arr) - 1
    while i >= 0:
        
        number += Arr[len(Arr) - 1 - i] * (10**i)
        i -= 1

    return number


def number_to_list(number):
    num_stack = []

    while number / 10 != 0:

        num_stack.append(number % 10)         
        number //= 10

    num_list = []
    while len(num_stack) != 0:
         
        num_list.append(num_stack.pop())

    return num_list


        

 

def add_one(arr): 
    print(number_to_list(list_to_number(arr) + 1))

   
num = [9, 9, 9]
print (num)
add_one(num)



