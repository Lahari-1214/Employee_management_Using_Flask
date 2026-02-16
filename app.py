from flask import Flask, render_template, request,jsonify,redirect,session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'emp_123'


# Database connection
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "leela@123",
    database = "company"
)


# Register route only for admin 
@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == "POST":
        uname = request.form['username']
        pwd = request.form['password']
        cursor = mydb.cursor()
        cursor.execute( "INSERT INTO users (username,password,role) VALUES (%s,%s,%s)",(uname,pwd,"admin"))
        mydb.commit()
        cursor.close()
        mydb.close()
        return redirect("/")
    return render_template('register.html')

# Login route for admin to access dashboard

@app.route('/',methods=['GET','POST'])
def login():
    if request.method == "POST":
        uname = request.form['username']
        pwd = request.form['password']
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM users where username = %s AND password = %s",(uname,pwd))
        user = cursor.fetchone()
        cursor.close()
        if user:
            session["admin"] = uname
            return redirect("/dashboard")
        else:
            return "INVALID LOGIN REGISTER FIRST"
    return render_template("login.html")

# Dashboard route only accessible to admin users

@app.route("/dashboard")
def dashboard():
    if "admin" not in session:
        return redirect("/")
    return render_template("dashboard.html")


# run the app

if __name__ == '__main__':
    app.run(debug=True)