'''
Print multiplication table form 1 to 10.
'''
 
#version_1
def multiplication_table(n):
 
    for i in range(1, 10):
        print ("        ", n, " * ", i," = ", n * i)

  

#version_2
def matrix_multiplication_table():
    
    for i in range(1, 10):
        for j in range(1, 10):
            print (i*j, end = "| ")
        print ()
        for j in range(1, 10):
            print("---", end = "")
        print ()
 

#version_1
for i in range(1, 10):
    print ("\n Multiplication Table For: ", i)
    multiplication_table(i)

#version_2    
matrix_multiplication_table()
