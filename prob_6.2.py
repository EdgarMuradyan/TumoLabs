 

def is_exists(d, m, y):
    
    if 12 < m or 1 > m: 

        return False


    if m == 2:
        if (y % 10) % 4 == 0:
            if d > 29:
                print(3)
                return False
        elif d > 28:
            print(1)
            return False

    if d > 31 or d < 1:
        print(2)
        return False

     
    if m == 4 or m == 6 or m == 9 or m == 11:
        if d > 30:
            print(4)
            return False
    return True
    
     



day   = int(input('day: '))
month = int(input('month: '))
year  = int(input('year: '))
print(is_exists(day, month, year))

 