 

def change_tuple(in_tuple):

    temp_list = list(in_tuple)
    temp_list[-1] = 100
    in_tuple = tuple(temp_list)
    return (in_tuple)
    


def change_last(tuple_list):

    for i in range(len(tuple_list)):
        tuple_list[i] = change_tuple(tuple_list[i])

         


tuple_list =  [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print (tuple_list)
change_last(tuple_list)
print (tuple_list)
