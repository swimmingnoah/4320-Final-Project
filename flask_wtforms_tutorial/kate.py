#Alternate string name and code INFOTC4320

def eticket(string_name, string_code, string_row, string_col):
    res = "".join([string_name[i] + string_code[i] for i in range(len(string_name))]) + string_code[len(string_name):]

    #Print reservation row, seat, and ticket number
    return "Congratulations " + str(string_name) + "!" + " Row:" + str(string_row) + " Seat:" + str(string_col) + " is now reserved! Enjoy the trip!" + "Your e-ticket number is: " + str(res))

print(eticket(string_name, string_code, string_row, string_col))
