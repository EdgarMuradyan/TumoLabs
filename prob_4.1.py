'''
Your task is to convert dash/underscore delimited words into camel casing. 
The first word within the output should be capitalized only if the original word was capitalized
'''
  
def convertCapitalLetter(letter):
    if(122 > ord(letter) > 97):
        return chr((ord(letter) - 32))
    else:
        return letter
 

dashWord = input("dash/underscore delimited words: ")


tempWord = ''
i = 0
while i < len(dashWord):
    if(dashWord[i] == '_') or (dashWord[i] == '-'):
        tempWord += convertCapitalLetter(dashWord[i+1])
        i += 2
    else:
        tempWord += dashWord[i]
        i += 1

dashWord = tempWord
print(dashWord)