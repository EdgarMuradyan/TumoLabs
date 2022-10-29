'''
Create a function that will take a HEX number and returns the binary equivalent (as a
string).
'''
 
def HexToDecimal(Hex): 
    #print (Hex)
    if(97 <= ord(Hex) <= 102):
        #print(ord(Hex) - 87)
        return (ord(Hex) - 87)
    elif(65 <= ord(Hex) <= 70):
        #print(ord(Hex) - 55)
        return (ord(Hex) - 55)
    elif(0 <= int(Hex) <= 9):
        #print (Hex)
        return Hex


def DecimalToBinary(Decimal):

    listBinary = [0,0,0,0]
    Dec = int(Decimal)
 
    i = 0
    while (Dec > 1) or (i != 4):        
        listBinary[i] =  int(Dec % 2)
        #print (listBinary[i])
        Dec /= 2
        i += 1
     
    binary = ''     
    while len(listBinary):
        binary += str(listBinary.pop()) 
    
    #print (binary) 
    return binary

 
def HexToBinary(Hex):
    binary = ''
    
    for i in range(len(Hex)):
        #print (Hex[i])
        dec_ = HexToDecimal(Hex[i])
        #print ('ddd',dec_)
        binary += DecimalToBinary(dec_)
        #print ('gg',binary)
        
    return binary
            

 


 

HEX = input('input HEX: ')

BINARY = HexToBinary(HEX)

print('00b', BINARY)



