import csv

PASSCODES = 'passcodes.txt'
RESERVATIONS = 'reservations.txt'

#CSVCHECK TAKES TWO PARAMETERS (USERNAME AND PASSWORD)
#ITS PURPOSE IS TO CHECK IF THOSE PARAMETERS MATCH A ROW IN THE CSV FILE
#IF A MATCH EXISTS; IT WILL RETURN TRUE
def csvCheck(user,userPass):
    with open(PASSCODES) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            username = row[0].lstrip()
            password = row[1].lstrip()
            if username == user and password == userPass:
                return True
    return False


#WRITERESERVATION TAKES FOUR PARAMETERS(NAME, ROW, COLUMN, RESERVATION NUMBER)
#ITS PURPOSE IS TO APPEND A NEW RESERVATION TO THE TEXT FILE
#IT OPENS THE GLOBAL RESERVATIONS FILE AND APPENDS A ROW WITH THE INPUTS.
def writeReservation(name, rowInp, colInp, resNum):
    with open(RESERVATIONS, mode='a+') as reservations:
        reservations_writer = csv.writer(reservations, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        reservations_writer.writerow([name,rowInp,colInp,resNum])


#ALTERNATE TAKES TWO PARAMETERS(STRING1, STRING2)
#ITS PURPOSE IS TO CREATE A NEW STRING THAT IS AN ALTERNATING CHARACTER STRING OF THE TWO PARAMETERS
#IT TEST THAT STRING1 OR STRING2 IS EMPTY AND RETURNS THE ALT VALUE IF ONE OF THEM IS
# SOURCE - https://stackoverflow.com/questions/37535313/return-alternating-letters-in-two-strings-of-different-lengths
def alternate(s1, s2):
    if not (s1 and s2):
        return s1 + s2
    return s1[0] + s2[0] + alternate(s1[1:], s2[1:])
# END CODE FROM https://stackoverflow.com/questions/37535313/return-alternating-letters-in-two-strings-of-different-lengths


#CREATERESERVATION TAKES THREE PARAMETERS(NAME, ROW, COLUMN)
#ITS PURPOSE IS TO CREATE THE RESERVATION NUMBER AND AND WRITE THE RESERVATION TO THE TEXT FILE
#IT CHECKS IF THE SEAT IS AVAILABLE; THEN WE ALTERNATE OUR MIX STRING AND THE USERS INPUTTED NAME TO CREATE THE RESERVATION NUMBER
#THEN IT WRITES THE RESERVATION TO THE FILE AND RETURNS THE RESERVATION NUMBER
def createReservation(name, rowInp, colInp):
    if seatOpen(rowInp, colInp):
        mix = 'INFOTC4320'
        resNum = alternate(name, mix)
        writeReservation(name, rowInp, colInp, resNum)
        return resNum


#SEATOPEN TAKES TWO PARAMETERS(ROW, COLUMN)
#ITS PURPOSE IS TO CHECK IF THOSE PARAMETERS ARE AVAILABLE TO BOOK
#IF THE SEAT IS AVAILABLE; IT WILL RETURN TRUE
def seatOpen(rowInp,colInp):
    if rowInp <= 11 and rowInp >= 0:
        if colInp <= 3 and colInp >= 0:
            with open(RESERVATIONS) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:
                    rowRes = int(row[1].lstrip())
                    colRes = int(row[2].lstrip())
                    if rowInp == rowRes and colInp == colRes:
                        return False
                return True
