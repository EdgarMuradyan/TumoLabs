'''
Given the names and grades for each student in a class of
students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names alphabetically and print
each name on a new line.
'''
 
dict_stud = {
                15: ["Davit", "Vardan"],
                10: ["Artur", "Njdeh"],
                5:  ["Arman", "Hayk"]
}
 

key_list = [key for key in dict_stud]

key_list.sort()
min_score = key_list[1]
      
    
dict_stud[min_score].sort()
print(dict_stud[min_score])
    