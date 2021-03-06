def get_cost_matrix():
    cost_matrix = [ [100, 75, 50, 100] ]
    return cost_matrix

# credits to Livvy and Li for creating the seatChart() I add the money handling
def cost():
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
    total_cost = 0
    cost_matrix = get_cost_matrix()
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
            for money in cost_matrix:
                if chart[row][seat] == 'X':
                    total_cost = total_cost + money[seat]
    return total_cost
