from flask import Flask, request, render_template_string, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_USER'] = 'web_user'
app.config['MYSQL_PASSWORD'] = 'pwd'
app.config['MYSQL_DB'] = 'booking'
app.config['MYSQL_HOST'] = 'localhost'
mysql = MySQL()
mysql.init_app(app) 






@app.route('/')
def main():
    return render_template_string("")


@app.route('/book', methods=['GET'])
def get_id():
    booking_id = request.args.get('booking_id')
    cursor = mysql.connection.cursor()  # Use mysql.connection directly
    cursor.execute("SELECT * from booking.bookings where booking_id = %s", (booking_id,))
    booking = cursor.fetchone()
    cursor.close()
    booking = {'booking_id': booking[0], 'name': booking[1], 'email': booking[2], 'booking_datetime': booking[3]}
    return render_template("book.html", booking = booking)

@app.route('/book', methods=['POST'])
def book():
    name = request.form.get('name')
    email = request.form.get('email')
    booking_datetime = request.form.get('booking_datetime')
    booking_id = request.form.get('booking_id')
    cursor = mysql.connection.cursor()  # Use mysql.connection directly
    cursor.execute("UPDATE booking.bookings SET name = %s, email = %s where booking_id = %s;", (name, email, booking_id))
    mysql.connection.commit()
    cursor.close()
    booking = {'name': name, 'booking_datetime': booking_datetime}
    return render_template("booked.html", booking = booking)

@app.route('/bookings', methods=['GET'])
def get_bookings():
    cursor = mysql.connection.cursor()  # Use mysql.connection directly
    cursor.execute("SELECT * from booking.bookings order by booking_datetime")
    bookings = cursor.fetchall()
    bookings_list = [{'booking_id': booking[0], 'name': booking[1], 'email': booking[2], 'booking_datetime': booking[3]} for booking in bookings]
    cursor.close()
    return render_template('bookings.html', bookings = bookings_list)

 
if __name__ == "__main__":
    app.run(debug=True)