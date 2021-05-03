#Stack overflow resource
string_one = "x"
string_two = "INFOTC4320"

def alt(s, t):
    if not (s and t):
        return s + t
    return s[0] + t[0] + alt(s[1:], t[1:])

# print result
print("The reservation code : " + str())
