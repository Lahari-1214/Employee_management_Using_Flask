### Project Title:
# Employee Management System
---
### Project Overview

The Employee Management System is a full-stack web application developed to manage employee records efficiently within an organization.
It replaces traditional manual systems (paper files, spreadsheets) with a secure, web-based solution that allows Admin/HR users to manage employee data effectively.

**The application is built using:**

1. Flask (Python) – Backend

2. MySQL – Database

3. HTML & CSS – Frontend

4. Session Management – Authentication & security

### Key Features

* Admin/HR Registration & Login

* Secure session-based authentication

* Employee record management (CRUD operations)

* Add, view, update, and delete employees

* Admin-only access to employee data

* Logout functionality
##  Project Workflow

Admin Registration  
       ↓  
Admin Login    
       ↓  
Dashboard  
       ↓  
Employee CRUD Operations  
(Add / View / Edit / Delete)  
       ↓  
Logout  
1.  **Role-Based Access**
* Admin / HR (Implemented)

* Registers and logs into the system

* Performs all CRUD operations

* Manages employee records

* Has full access to the system

2. **Employee (Future Enhancement)**

* Can log in

* Can view own details only

* No permission to modify data
---
- [X] Why Admin performs CRUD?
In real-world organizations, employee data is managed only by HR/Admin to ensure data integrity, security, and compliance.
---
## Project Structure
<pre>
employee_management/
│
├── app.py
│
├── templates/
│   ├── register.html
│   ├── login.html
│   ├── dashboard.html
│   ├── add_employee.html
│   ├── view_employee.html
│   └── edit_employee.html
│
└── static/
    └── style.css
</pre>
    

## Database Design
<pre>
Database Creation
CREATE DATABASE company;
USE company;

Users Table (Admin / HR)
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(50),
    role VARCHAR(20)
);

Employee Table
CREATE TABLE employee (
    eid INT PRIMARY KEY,
    ename VARCHAR(50),
    edept VARCHAR(50),
    esalary INT,
    ephone VARCHAR(15)
);

  </pre>

## Technologies Used

* Backend: Python, Flask

* Frontend: HTML, CSS

* Database: MySQL

* Security: Flask Sessions

* Architecture: MVC-style structure

## Installation & Setup
1️. **Clone the Repository**
git clone https://github.com/your-username/Employee_management_Using_Flask.git <br>
cd Employee_management_Using_Flask

2️. **Install Required Packages**
pip install flask mysql-connector-python

3️. **Configure Database**

      * Start MySQL server

      * Create database and tables using the provided SQL scripts

      * Update database credentials in app.py if required

4️.  **Run the Application**
python app.py

5️. **Open in Browser**
http://127.0.0.1:5000/

## Security Features

* Session-based authentication

* Restricted access to dashboard and CRUD operations

* Logout clears active session

## Future Enhancements

* Employee login module

* Role-based authorization (Admin / Employee)

* Password hashing

* Pagination & search

* Payroll & attendance modules

* Email notifications

## Final Summary

* Admin/HR controls employee data

* Employees are managed entities

* Real-time organizational workflow followed

* Secure full-stack Flask application

* Scalable and extendable design

