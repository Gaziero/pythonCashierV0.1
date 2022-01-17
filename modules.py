import products

def line (char = "=") :
    print(char*48)

def title(msg, char = "=") :
    line(char)
    print(msg.center(48))
    line(char)

def readInt(msg) :
    #Only accepts the input of int numbers. Displays an error message if input isn't an int
    #Keeps asking for input untill it recieves an int or a KeyboardInterrupt
    while True :
        try :
            n = int(input(msg))
        except (ValueError, TypeError) :
            print ("\033[1;31mERROR! Invalid input.\033[m")
            continue
        except KeyboardInterrupt :
            print ("\033[1;31mAction interrupted by the user.\033[m")
            n = 0
            return n
        else:
            return n
        
def checkInt(val) :
    #Tries to convert val into int, if possible, returns val, else, displays Error
    while True :
        try :
            n = int(val)
            return n
        except :
            print ("\033[1;31mERROR! Invalid input.\033[m")
            return -1

def readFloat(msg) :
    #Only accepts the input of int or float numbers. Displays an error message if input isn't a float
    #Keeps asking for input untill it recieves a float or a KeyboardInterrupt
    while True :
        try :
            n = float(input(msg).strip().replace(",", "."))
        except (ValueError, TypeError):
            print ("\033[1;31mERROR! Invalid input.\033[m")
            continue
        except KeyboardInterrupt :
            print ("\033[1;31mAction interrupted by the user.\033[m")
            n = 0
            return n
        else :
            return n
        
def check(msg) :
    #This is responsible for checking if the input is to be used as product bar code or
    # as product multiplier
    multi = 1 #Default multiplier
    ok = False #Only turns True when the input is not a multiplier and is a valid int number
    while True :
        n = input(msg)
        if (n.endswith("*")) and n.replace("*", "").isnumeric() : #Checks if its multiplier
            multi = int(n.replace("*", ""))
        else :
            n = checkInt(n)
            if n != -1 :
                cod = n
                ok = True
        if ok :
            return cod, multi #Returns the code (int) and the multiplier (default 1)

def sendToCart(cod, multi = 1) :
    exists = False #Tells if the bar code exists in the system or not.
    cart = [] #List that will receive the product's data[0] and the multiplier[1]
    if cod == 0 :
        return 0 #Will end the operation
    else :
        for p in products.prods : #Checks all the registered products in products.py
            if cod == p["cod"] : #If the code belongs to any product:
                cart.append(p)  #Stores the product's data
                cart.append(multi) #Stores the multiplier
                exists = True 
        if exists is False : #Will tell that this code doesn't exist
            return -1
        else :
            return cart #Return the product's data and multiplier
