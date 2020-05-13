import re

number = input("ingrese número de extension inicial: ")
cantidad =input("ingrese cantidad de extension a crear: ")


def isNumber(p):
    valor=False
    x = re.findall("[0-9]", p)
    

    if (len(x)>0):
        valor=True
    return valor

string = """
        [9999]
        username=9999
        type=friend
        secret=*****
        qualify=no
        port=5060
        pickupgroup=
        nat=yes  
        mailbox=
        dtmfmode=rfc2833
        context=context-inconcert
        canreinvite=no
        callgroup= 
        callerid=9999  
        record=no \n
        """
i=0

if (number):
    if (cantidad):
        while i < int(cantidad):
            #print(int(number)+i)
            val=int(number)+i
            print ( string.replace("9999",str(val)) )
            i+=1
