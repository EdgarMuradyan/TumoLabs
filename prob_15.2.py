 
import os, random
 
os.system('cls' if os.name == 'nt' else 'clear')

def print_variants(start, end):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Guess the number ", start, " -> ", end)
    for i in range(start, end):
        print(i, end=" ")
    

    print()
        
     



print("Guess the number 0 - 99։ ")
num = random.randint(0,99)
chances = 11
in_num = -1 
start = 0
end = 99


while ((chances != 0) and (num != in_num)):

    in_num = int(input("input Your answer: "))
    if in_num < start or in_num > end:
        print("input correct number!!!")
        #print_variants(start, end)
        continue
  
    if in_num == num:
        print ("It's right, you did it")
        break
    elif in_num > num:
        end = in_num
        print_variants(start, end)
        if abs(num - in_num) < 7:
            print("Too far! add")
        else:
            print ("Too far! deduct")
    elif in_num < num:
        start = in_num
        print_variants(start, end)
        if abs(num - in_num) < 7:
            print("Too far! add")
        else:
            print ("Too far! deduct")

    chances -= 1 
    print ("You have: ", chances, " chances")
    if chances == 0:
        print("~~~You lost~~~")
    
     



