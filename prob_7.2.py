'''
Write a Python program to sort a list of elements using the bubble sort algorithm.
'''

# buble sort 
def buble_sort(Arr):
    
    i = 0
    while i < len(Arr) - 1:
        
        j = 0
        while j < len(Arr) - 1:

            if Arr[j] > Arr[j+1]:                
                Arr[j], Arr[j + 1] = Arr[j + 1], Arr[j]
            j += 1

        i += 1



#Selection Sort   
def selection_sort(Arr):
    
    i = 0
    while i < len(Arr) - 1:
        
        j = i
        while j < len(Arr):

            if Arr[i] > Arr[j]:                
                Arr[i], Arr[j] = Arr[j], Arr[i]
            j += 1

        i += 1

  
#quick sort 
def partition(Arr, first, last):
    pivot = Arr[last]
       
    i = first - 1

    j = first
    while j <= last - 1:
       
        if Arr[j] <=  pivot :
            i += 1
            Arr[i], Arr[j] = Arr[j], Arr[i]
            
        j += 1
         
    Arr[i+1], Arr[last] = Arr[last], Arr[i+1]
    return (i + 1)
        
#interface for quick sort
def quick_sort(Arr):
    quickSort(Arr, 0, len(Arr) - 1)
      
def quickSort(Arr,first, last):
    
    if first < last:
        pivot = partition(Arr, first, last)
        quickSort(Arr, first, pivot - 1)
        quickSort(Arr, pivot + 1, last)


        



#main
Arr = [14,46,43,27,-57,41,45,-21,0]
 
#buble_sort(Arr)
#selection_sort(Arr)
quick_sort(Arr)

print (Arr)

