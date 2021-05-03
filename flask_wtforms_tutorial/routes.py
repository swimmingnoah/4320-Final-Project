from flask import current_app as app
from flask import redirect, render_template, url_for, request, flash

from .forms import *
from .seatingChart import *
from .kyle import *
from .checkCredentials import *
from .calculate_Money import *

#@app.route("/", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def user_options():

    form = UserOptionForm()
    if request.method == 'POST' and form.validate_on_submit():
        option = request.form['option']

        if option == "1":
            return redirect('/admin')
        else:
            return redirect("/reservations")

    return render_template("options.html", form=form, template="form-template")

@app.route("/admin", methods=['GET', 'POST'])
def admin():
    form = AdminLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
            username = request.form['username']
            password = request.form['password']
            token = request.form['csrf_token']
            #CSVCHECK RETURNS TRUE IF THERE IS A MATCHING USER/PASS COMBO IN PASSCODES.TXT
            #if csvCheck(username, password):
            if checkCredentials(username, password):
                totalSales = cost()
                seatingChart = seatchart()

                return render_template("admin.html", form = form, template = "form-template", seatingChart = seatingChart, sales = totalSales)
            else:
                error = 'Invalid Username or Password'

                return render_template("admin.html", form = form, template = "form-template", error = error)

    return render_template("admin.html", form = form, template = "form-template")

@app.route("/reservations", methods=['GET', 'POST'])
def reservations():
    form = ReservationForm()
    initialReservations = seatchart()
    if request.method == 'POST' and form.validate_on_submit():
            rowInp = int(request.form['row'])
            colInp = int(request.form['seat'])
            name = request.form['first_name']

            # WE DO THIS BECAUSE COMPUTERS COUNT FROM 0 AND THE ROW 1 SHOULD BE CONSIDERED ROW 0 TO THE PROGRAMMER
            row = rowInp - 1
            col = colInp - 1

            #SEAT_OPEN RETURNS TRUE IF THE SEAT IS NOT CURRENTLY BOOKED IN RESERVATIONS.TXT
            if seatOpen(row,col):
                #CREATE_RESERVATION CREATES A RESERVATION WITH NAME, ROW, AND COLUMN OF THE USERS INPUT, IT RETURNS A RESERVATION NUMBER
                resNum = createReservation(name, row, col)
                seatingChart = seatchart()
                message = 'Congratulations {} Row: {} Seat: {} is now reserved for you!\nYour eTicket information is {}'.format(name, rowInp, colInp, resNum)

                return render_template("reservations.html", form = form, template = "form-template", success = message, seatingChart = seatingChart)
            else:
                error = 'The Seat at Row: {} Seat: {} is Taken! Please Choose a Differernt Seat!'.format(rowInp,colInp)
                seatingChart = seatchart()

                return render_template("reservations.html", form = form, template = "form-template", error = error, seatingChart = seatingChart)

    return render_template("reservations.html", form = form, template = "form-template", seatingChart = initialReservations)
