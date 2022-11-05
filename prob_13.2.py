
import  random

def Yoda_styl(Istr):

   str_list = []
   for i in Istr.split():
       str_list.append(i)
       #print (i)
     
   result = ""
   for i in range(len(str_list)):
       index = random.randint(0, len(str_list) - 1)
       while str_list[index] == -1:
           index = random.randint(0, len(str_list) - 1)
       
       result += str_list[index] + " "
       str_list[index] = -1
   
   
       
       
   return result
     







input_string = "Luke, I'm your father"
print(Yoda_styl(input_string))








