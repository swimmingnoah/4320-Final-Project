# Livvy and Li's code
def seatchart():
    chart = [['O','O','O','O'],
             ['O','O','O','O'],
             ['O','O','O','O'],
             ['O','O','O','O'],
             ['O','O','O','O'],
             ['O','O','O','O'],
             ['O','O','O','O'],
             ['O','O','O','O'],
             ['O','O','O','O'],
             ['O','O','O','O'],
             ['O','O','O','O'],
             ['O','O','O','O']]

    try:
        file = open('reservations.txt','r')
    except FileNotFoundError:
        err = "ERROR: Can't find file."
    else:
         reservations = file.readlines()
    for  reservation in reservations:
        row = int(reservation.split(',')[1])
        seat = int(reservation.split(',')[2])
        chart[row][seat] = 'X'
    return chart
