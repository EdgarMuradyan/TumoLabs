 

def generate_permutation(numbers):
    new_list = []
    n = len(numbers)
    num_index = []
    bool_check = []
    for i in range(n):
        num_index.append(i)
        bool_check.append(0)
 
  
    def permutations(step):
    
        if step == n:
            current_list = []
            for i in range (n):
                
                current_list.append(numbers[num_index[i]])
             
            new_list.append(current_list)
        for i in range (n):
            if bool_check[i] == False:
                num_index[step] = i
                bool_check[i] = True
                permutations(step + 1)
                bool_check[i] = False
    
    permutations(0)
    return new_list


 
nums = [0, 1]
print(generate_permutation(nums))



