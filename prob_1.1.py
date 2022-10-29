'''
Given an integer array (nums), move all 0’s to the end of it while maintaining the relative order of the non-zero elements.

'''


def shift(Arr, firstIndex):

    i = firstIndex

    while (i < (len(Arr) - 1)):
        Arr[i] = Arr[i+1]
        i += 1


def addZero(Arr, count):


    index = len(Arr) - 1
    while count > 0:
        Arr[index] = 0
        index -= 1
        count -= 1




def getZeroCount(Arr):
    i=0
    zeroCount = 0
    length = len(Arr)
    while (i < length):
        if Arr[i] == 0:
            shift(Arr,i)
            length -= 1
            zeroCount += 1

        i += 1

    return zeroCount


#main
nums = [0,1,3,0,2]
 
countOfZero = getZeroCount(nums)

print ("Input: ", nums)
addZero(nums, countOfZero)
 
print ("Output: ", nums)
