#Task 3: MySQL Database Operations with Python ( Compulsory ) Problem Statement: Your task is to write a Python program that accomplishes the following: First create a database , table and add these column ‘student_id’, ‘first_name’, ‘last_name’, ‘age’, ‘grade’. Connects to your MySQL database with python. Inserts a new student record into the "students" table with the following details: First Name: "Alice" Last Name: "Smith" Age: 18 Grade: 95.5 Updates the grade of the student with the first name "Alice" to 97.0. Deletes the student with the last name "Smith." Fetches and displays all student records from the "students" table.

#pip install mysql-connector-python

import mysql.connector

def create_database_and_table():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
    )
    cursor = conn.cursor()

    
    cursor.execute("CREATE DATABASE IF NOT EXISTS school")
    conn.database = "school"


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            age INT,
            grade FLOAT
        )
    """)

    conn.commit()
    conn.close()


def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="school"
    )


def main():
    create_database_and_table()

    conn = connect_to_database()
    cursor = conn.cursor()


    cursor.execute("""
        INSERT INTO students (first_name, last_name, age, grade)
        VALUES (%s, %s, %s, %s)
    """, ("Alice", "Smith", 18, 95.5))

    
    cursor.execute("""
        UPDATE students
        SET grade = 97.0
        WHERE first_name = 'Alice'
    """)

    
    cursor.execute("""
        DELETE FROM students
        WHERE last_name = 'Smith'
    """)


    cursor.execute("SELECT * FROM students")
    all_students = cursor.fetchall()
    for student in all_students:
        print(student)

    conn.commit()
    conn.close()
if _name_ == "_main_":
    main()
