'''
Write a Python program to create all possible strings by using &#39;a&#39;, &#39;e&#39;, &#39;i&#39;, &#39;o&#39;, &#39;u&#39;. Use the characters
exactly once.
'''

def generate_word(letters):
    n = len(letters)
    let_index = []
    bool_check = []
    for i in range(n):
        let_index.append(i)
        bool_check.append(0)
 
  
    def permutations(step):
    
        if step == n:

            for i in range (n):
                print (letters[let_index[i]], end = '')
            print (" ")
            
        for i in range (n):
            if bool_check[i] == False:
                let_index[step] = i
                bool_check[i] = True
                permutations(step + 1)
                bool_check[i] = False
    
    permutations(0)

print (1)  
Iletters = ['a', 'b', 'c', 'd']
generate_word(Iletters)