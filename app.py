from flask import Flask, render_template, request,jsonify,redirect,session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'emp_123'


# Database connection
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "leela@123",
    database = "employee_management"
)


# Register route only for admin 
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == "POST":
        uname = request.form['username']
        pwd = request.form['password']
        role = request.form['role']

        cursor = mydb.cursor()

        if role == "employee":
            # First create employee record
            cursor.execute(
                "INSERT INTO employee (ename, dept, salary, phone) VALUES (%s, %s, %s, %s)",
                (uname, "Not Assigned", 0, "0000000000")
            )
            mydb.commit()

            emp_id = cursor.lastrowid  # get inserted employee id

            # Now insert into users with emp_id
            cursor.execute(
                "INSERT INTO users (username, password, role, emp_id) VALUES (%s, %s, %s, %s)",
                (uname, pwd, role, emp_id)
            )

        else:  # admin
            cursor.execute(
                "INSERT INTO users (username, password, role, emp_id) VALUES (%s, %s, %s, NULL)",
                (uname, pwd, role)
            )

        mydb.commit()
        cursor.close()

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
            session["username"] = user[1]
            session["role"] = user[3]
            session["emp_id"] = user[4]   # very important

            if user[3] == "admin":
                return redirect("/admin_dashboard")
            elif user[3] == "employee":
                return redirect("/employee_dashboard")
            else:
                return "Invalid Role!"

        else:
            return "INVALID LOGIN REGISTER FIRST"
    return render_template('login.html')

# Admin dashboard route only accessible to admin users
@app.route("/admin_dashboard")
def admin_dashboard():

    # Check if user is logged in
    if "username" not in session:
        return redirect("/")

    # Check if role is admin
    if session["role"] != "admin":
        return "Access Denied! Admin Only."

    return render_template("admin_dashboard.html")
# Employee dashboard route only accessible to employee users
@app.route("/employee_dashboard")
def employee_dashboard():

    # Check if user is logged in
    if "username" not in session:
        return redirect("/")

    # Check if role is employee
    if session["role"] != "employee":
        return "Access Denied! Employees Only."

    return render_template("employee_dashboard.html")


# Dashboard route only accessible to admin users

# @app.route("/dashboard")
# def dashboard():
#     if "admin" not in session:
#         return redirect("/")
#     return render_template("dashboard.html")

# ADD EMPLOYEE route to add employee details to the database, only accessible to admin users
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":

        data = (
            # request.form["id"],
            request.form["ename"],
            request.form["dept"],
            request.form["salary"],
            request.form["phone"]
        )
        cursor = mydb.cursor()
        cursor.execute("""INSERT INTO employee (ename, dept, salary, phone)VALUES ( %s, %s, %s, %s)""", data)
        mydb.commit()
        cursor.close()
        return redirect("/view")
    
    return render_template("add_employee.html")

# VIEW EMPLOYEES 
@app.route("/view")
def view():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM employee")
    data = cursor.fetchall()
    cursor.close()
    return render_template("view_employee.html", employees=data)

# EDIT EMPLOYEE 
@app.route("/edit/<eid>")
def edit(eid):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM employee WHERE eid=%s", (eid,))
    emp = cursor.fetchone()
    cursor.close()
    return render_template("edit_employee.html", emp=emp)

# UPDATE EMPLOYEE 
@app.route("/update", methods=["POST"])
def update():
    data = (
        request.form["ename"],
        request.form["edept"],
        request.form["esalary"],
        request.form["ephone"],
        request.form["eid"]
    )
    cursor = mydb.cursor()
    cursor.execute("UPDATE employee SET ename=%s, edept=%s, esalary=%s, ephone=%s WHERE eid=%s", data)
    mydb.commit()
    cursor.close()
    return redirect("/view")

 # -------- DELETE EMPLOYEE --------
@app.route("/delete/<eid>")
def delete(eid):
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM employee WHERE eid=%s", (eid,))
    mydb.commit()
    cursor.close()
    return redirect("/view")

# -------- LOGOUT --------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

# Employee profile route to view their own details, only accessible to employee users
@app.route("/my_profile")
def my_profile():

    if "username" not in session or session["role"] != "employee":
        return redirect("/")

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM employee WHERE ename=%s", (session["username"],))
    data = cursor.fetchone()
    cursor.close()
    return render_template("my_profile.html", emp=data)





# run the app

if __name__ == '__main__':
    app.run(debug=True)