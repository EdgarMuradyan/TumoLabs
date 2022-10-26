

def sumList (Arr):

    sum = 0
    for it in Arr:
        sum += it
    return sum

 

#created list
Olist = []
begin = int(input('start: '))
end = int(input('end: '))
step = int(input('step: '))


if begin > end:
        print (0)
else:

    i = 0
    Olist.append(begin)
    while Olist[i] < end:
        i += 1
        Olist.append(Olist[i - 1] + step)

    print (sumList(Olist), "=>", Olist)
