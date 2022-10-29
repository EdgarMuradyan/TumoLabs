
'''
Given a two list of numbers, write a program to create a new list such that the new list should
contain odd numbers from the first list and even numbers from the second list.
'''


def creat_list(Arr_1, Arr_2):
    new_list = []

    for i in Arr_1:
        if i % 2 != 0:
            new_list.append(i)

    for i in Arr_2:
        if i % 2 == 0:
            new_list.append(i)

    return new_list


list_1 = [10, 20, 25, 30]
list_2 = [40, 45, 60, 75, 90]

print (creat_list(list_1, list_2))


