 
#aditional 
def calculate(a, b, op):
     
    if ord(op) == 43:  
        return a + b
    elif ord(op) == 45: 
        return a - b
    elif ord(op) == 42:
        return a * b
    elif ord(op) == 47:
        return a / b

'''
a = int(input("input: a "))
op = input("input operator: ")
b = int(input("input: b "))
print(" = ", calculate(a,b,op))
'''

def calculate_all(a,b):
     print(a, " + ", b, " = ", a + b)
     print(a, " - ", b, " = ", a - b)
     print(a, " * ", b, " = ", a * b)
     print(a, " / ", b, " = ", a / b)
     
a = int(input("input: a "))
b = int(input("input: b "))

calculate_all(a,b)

