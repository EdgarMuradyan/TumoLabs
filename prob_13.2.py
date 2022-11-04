
import  random

def Yoda_styl(Istr):

   str_list = []
   for i in Istr.split():
       str_list.append(i)
       #print (i)
     
   result = "a"
   for i in range(len(str_list)):
       print(str_list[i])
       random.seed(i)
       print(int(random.random()))
       result.join(str_list[int(random.random())])

   
       
       
   return result
     







input_string = "Luke, I'm your father"
print(Yoda_styl(input_string))








