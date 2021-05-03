

def checkCredentials(uname, pword):

    k = 0
    check = 0
    
    try:
        file = open('passcodes.txt','r')
    except FileNotFoundError:
        err = "ERROR: Can't find file."
    else:
         admins = file.readlines()

         for  admin in admins:
            name = admins[k].split(', ')[0] #get the user name
            code = admins[k].split(', ')[1] #get the password
            code = code.rstrip(code[-1])    #remove the extra index
            if uname == name:          #check for matching username and password
               if pword == code:
                  return 1             #return 1 if username and password are correct
                  break      
            k += 1
    return 0

def formatMoney(money):
    
   cash = "${:,.2f}".format(money)
   
   return cash



