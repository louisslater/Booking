from flask import Flask, request, render_template_string
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_USER'] = 'web_user'
app.config['MYSQL_PASSWORD'] = 'pwd'
app.config['MYSQL_DB'] = 'booking'
app.config['MYSQL_HOST'] = 'localhost'
mysql = MySQL()
mysql.init_app(app) 



HTML_FORM = '''
<!DOCTYPE html>
<html>
<head>
    <title>Submit Your Info</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</head>
<body>
     <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
        <a class="navbar-brand" href="#">Booking</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
            <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="/">Home</a>
            </li>
            <li class="nav-item">
            <a class="nav-link" href="/book">Book</a>
            </li>
            <li class="nav-item">
            <a class="nav-link" href="/bookings">Bookings</a>
            </li>
            <li class="nav-item">
            <a class="nav-link disabled">Disabled</a>
            </li>
        </ul>
        </div>
    </div>
    </nav>

    <h2>Enter your name and age</h2>
    <form method="post">
        Name: <input type="text" name="name"><br>
        Age: <input type="number" name="age"><br>
        <input type="submit" value="Submit">
    </form>
    {% if name and age %}
        <h3>Hello {{ name }}, you are {{ age }} years old.</h3>
    {% endif %}
</body>
</html>
'''

@app.route('/')
def main():
    return render_template_string(HTML_FORM)


@app.route('/book', methods=['GET','POST'])
def add_user():
    name = request.form.get('name')
    age = request.form.get('age')
    if name and age:
        cursor = mysql.connection.cursor()  # Use mysql.connection directly
        cursor.execute("INSERT INTO Users (name, age) VALUES (%s, %s)", (name, age))
        mysql.connection.commit()
        cursor.close()
    return render_template_string(HTML_FORM, name=name, age=age)
 
if __name__ == "__main__":
    app.run(debug=True)