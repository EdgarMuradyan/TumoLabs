'''
Write a program that returns true if the number entered is prime, false otherwise.
'''
 

def is_prime(num):
   
    if num < 3:      
        return True
    elif num % 2 ==0:     
        return False
    elif num % 3 ==0:       
        return False    

    x = 5
    while x < int(num/2):
        if num % x == 0:
            
            return False
        x += 1
    return True

  


num = int(input('input number: '))
 
print ('is number prime: ',is_prime(num))


