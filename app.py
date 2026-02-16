from flask import Flask, render_template, request,jsonify,redirect
import mysql.connector

app = Flask(__name__)
# Database connection
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "leela@123",
    database = "company"
)
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

@app.route('/')
def login():
    return "Welcome"

if __name__ == '__main__':
    app.run(debug=True)