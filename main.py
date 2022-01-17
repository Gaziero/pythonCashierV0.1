import modules as m #Custom functions made for this application
import sys
from datetime import datetime
import os
#====================================================================
#This whole code was designed based on the needs of a Brazilian store
#====================================================================
#kind of operation being made, no use for now
#Future plans iclude being able to sell, buy, permute or return
operation = "VENDA" 

#The store's data. Used to print the invoice after the purchase is completed
data = {
"name" : "NOME DA EMPRESA",
"cnpj" : "00.000.000/0001-00",
"adress" : "AVENIDA OU RUA, N°, SALA 00, BAIRRO, CIDADE",
"cep" : "00000-000",
"contact" : "(00)12345-6789 seu_email@email.com"
}

#==========================================

#This part asks for the product's bar code:
#If the code is on products.py: The product data is stored in list 'cart';
#If the user types an int number followed by * (E.g. n*), the next product is stored in 'cart' n times;
#Only accepts int numbers as input

cart = []
while True :
    c, mult = m.check("Próximo código: ") 
    op = m.sendToCart(c, mult)
    if op == 0 : #Ends the operation
        break
    elif op == -1 : #This happens in case the bar code (c) doesn't exists in the system
        print ("Código não existente") #Inform the user that said code doesn't exist
    else :
        cart.append(op) #Stores product (c) in 'cart[]' with a quantity of (mult) 
        
#============================================

#This part writes the invoice as a .txt file:

original_stdout = sys.stdout #Stores the original stdout path
with open("toPrint.txt", "w") as f: #Creates the .txt, erasing all the content of the previous one
    sys.stdout = f #Sets the stdout as the created .txt file
    m.line()
    for v in data.values() : #Writes all the store's data previously provided:
        print (v.center(48)) #48 characters is the max len to print on the 80mm printer that I have
    print ("NÃO É DOCUMENTO FISCAL".center(48))
    m.line()
    print (operation.center(48))
    m.line("-")
    #Writes a line describing the product's info that will be bellow it
    print (f"{'Produto|Código':<30}{'|Qtd|ValUn|ValTot'}")

    endTot = 0 #Final price to be paid
    qntTot = 0 #Final quantity of products
    for i in cart :
        #Each i is a list composed by a dict with all the product info [0], and an int number [1]
        cod = i[0]["cod"] #Prod bar code
        name = i[0]["name"] #Prod name
        qnt = i[1] #Quantity of product in the cart
        val = i[0]["valor"] #Prod price
        tot = qnt*val 
        endTot += tot
        qntTot += qnt
        #Writes all the product's info
        print (name) 
        print (f"{cod:<30}|{qnt:>3}|{val:>5.2f}|{tot:>7.2f}")
        
    m.line("-")
    #Writes the total number of itens and the total price
    print (f"N° de itens: {qntTot:0>3}".ljust(24) +f"{'Total: R$':>}{endTot:>.2f}".rjust(24))
sys.stdout = original_stdout #Returns the stdout to its original path

print (f"O total é de {endTot}") #Shows on screen the final price
pago = m.readFloat("Valor pago: R$") #Asks for how much will be paid
troco = pago - endTot #Calculates the change

with open("toPrint.txt", "a") as f:
    #Writes the total price, price paid, change, and current date and hours
    sys.stdout = f
    print (f"{'Valor pago: R$':>}{pago:>.2f}".rjust(48))
    print (f"{'Troco: R$':>}{troco:>.2f}".rjust(48))
    m.line("-")
    data = str(datetime.today()).replace("-", "/")
    print (data[:19]) #The index selection is used to exclude the miliseconds from datetime
    m.line("-")
os.startfile("toPrint.txt", "print") #Sends the .txt file to be printed on the default printer
    
sys.stdout = original_stdout
