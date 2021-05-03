#Stack overflow resource

string_name = "Alice"
string_code = "INFOTC4320"
string_row = "0"
string_col = "1"

res = "".join([string_name[i] + string_code[i] for i in range(len(string_name))]) + string_code[len(string_name):]

# print result
print("Congratulations " + str(string_name) + "!" + " Row:" + str(string_row) + " Seat:" + str(string_col) + " is now reserved! Enjoy the trip!")
print("Your e-ticket number is: " + str(res))
