'''

'''


def search_x(Arr, x):

    for i in range(len(Arr)):
        if x == Arr[i]:
            return i
    
    return -1



#binary search forck then Array is sorted
def binary_search(Arr, x, start, end):
    
    

    if  end > 1:
        midle = (start + end) // 2
        if x == Arr[midle]:
             
            return midle
        elif x < Arr[midle]:
            
            return binary_search(Arr, x, start, midle - 1 )
        elif x > Arr[midle]:
            return binary_search(Arr, x, midle + 1, end)
    else:
        return -1
     










arr = [10, 20, 80, 30]
print (search_x(arr, 30))

arr.sort()
x = 80
print(binary_search(arr, x, 0, len(arr)))










#print(search_x(arr, 65))




