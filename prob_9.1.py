'''
Find the nearest value to the given one.
You are given a set of integers and a value for which you need to find the nearest one.
For example, we have the following sequence of numbers: 4, 7, 10, 11, 12, 17, and we need to find the
nearest value to the number 9.
If we sort this sequence in the ascending order, then to the left of number 9 will be number 7 and to the
right - will be number 10. But 10 is closer than 7,
which means that the correct answer is 10.
A few clarifications:
If 2 numbers are at the same distance, you need to choose the smallest one;
The sequence of numbers is always non-empty;
The given value can be in this sequence, which means that it�s the answer;
The sequence may contain both positive and negative numbers, but they are always integers;
The sequence isn�t sorted and consists only unique numbers.
Input: Two arguments. A set of integers. The sought value as an integer.
'''

   
def finde_nearest_number(Arr, n):
    index = 0
    dictance = abs(n - Arr[index])
    
    for i in range(len(Arr)):
        
        if (abs(n - Arr[i]) < dictance):

            dictance = abs(n - Arr[i])
            index = i

    print (Arr[index])
     

numbers = [4, 7, 10, 11, 12, 9]
n = 9

finde_nearest_number(numbers, n)
 