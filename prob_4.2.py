 
def isAscending(Arr):
    
    for i in range(len(Arr) - 1):
        if(Arr[i] >= Arr[i +1]):
            return 0


    return 1

def isDescending(Arr):
    
    for i in range(len(Arr) - 1):
        if(Arr[i] <= Arr[i +1]):
            return 0
        
    return 1


def analysList(Arr):
    if(isAscending(Arr)):
        print (Arr, "=> yes, ascending")
        return
    if(isDescending(Arr)):
        print (Arr, "=> yes, descending")
        return
    else:
        print (Arr, "=> No")
        return
    
     
list_1 = [3,  4, 12, 56]
list_2 = [98, 65, 43, 2]
list_3 = [71, 32, 55, 9] 
 
analysList(list_1)
analysList(list_2)
analysList(list_3)
