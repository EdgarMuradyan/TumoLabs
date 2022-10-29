'''
Your task is to make a list, with the sum of a sequence of integers.
The sequence is defined by 3 non-negative values: begin, end, step
(inclusive).
If begin value is greater than the end, print 0
'''

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
