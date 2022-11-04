
'''
Given two matrix the task is that we will have to create a program to multiply two matrices in
python.
'''

 
def print_matrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print('{:>3}'.format(mat[i][j]), end = " ")
        
        print()

    

 
def multiply_matrix(A, B):
     
    matrix_result = []
    
    for i in range(len(A)):
        
        roow_result = []
        for j in range(len(B[0])):
            
            sum_result = 0
            for k in range(len(A[0])):
                sum_result += A[i][k]*B[k][j]
             
            roow_result.append(sum_result)
        matrix_result.append(roow_result)
    
    

    #print matrix

    print_matrix(A)
    print(" * ")
    print_matrix(B)
    print(" = ")
    print_matrix(matrix_result)

     










X = [[1, 7, 3],
     [3, 5, 6],
     [6, 8, 9]]
Y = [[1, 1, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]]

multiply_matrix(X, Y)
