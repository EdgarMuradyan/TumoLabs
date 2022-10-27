 
 
def check(Arr, k):
    
    for i in range(len(Arr) - 1 - k):
        
        for j  in range(i + 1, i + 1 + k):
             
            if Arr[i] == Arr[j]:
                #print (Arr[i], Arr[j])
                return True

    return False

 

nums = [1,2,3,1,2,3]
k = 2

print(check (nums, k))


        


