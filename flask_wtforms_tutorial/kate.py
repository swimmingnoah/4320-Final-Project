#Stack overflow resource

string_one = "AAA"
string_two = "INFOTC4320"

res = "".join([string_one[i] + string_two[i] for i in range(len(string_one))]) + string_two[len(string_one):]

# print result
print("The reservation code : " + str(res))
