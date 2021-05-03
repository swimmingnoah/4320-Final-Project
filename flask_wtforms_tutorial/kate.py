

# try:
#         file = open('reservations.txt','r')
#     except FileNotFoundError:
#         err = "ERROR: Can't find file."
#     else:
#          reservations = file.readlines()


# def reservationCode(name):
#
#     code = 'INFOTC4320'
#     reservation = alternate(name, code)
#     finalReservationCode(first_name, row, seat, reservation)
#     return final

# initializing list
test_list = ["abc", "xyz"]


# using list comprehension + list slicing
# Alternate Strings Concatenation
res = [" ".join(test_list[i : : 2]) for i in range(len(test_list) //
                                                  (len(test_list)//2))]

# print result
print("The reservation code : " + str(res))
