# import sqlite3 as sql
from django.db import models

class Student(models.Model):
    studentId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length = 50)
    lastName = models.CharField(max_lenght = 50)

    class Meta:
        db+table = 'studentData'

# #establishing database connection
# con = sql.connect("studentData.db")
# cur = con.cursor()

# #creating students table
# cur.execute("""
# CREATE TABLE IF NOT EXISTS students (
#     studentId INTEGER PRIMARY KEY AUTOINCREMENT
#    , firstName varchar(50)
#    , lastName varchar(50));
# """
# )

# cur.execute("""
# CREATE TABLE IF NOT EXISTS professors (
#    professorId INTEGER PRIMARY KEY AUTOINCREMENT
#    , firstName varchar(50)
#    , lastName varchar(50));
# """
# )

# cur.execute("""
# CREATE TABLE IF NOT EXISTS courses (
#    courseId INTEGER PRIMARY KEY AUTOINCREMENT
#    , courseDesc varchar(50)
#    , professorID_fk bigint);
# """
# )

# cur.execute("""
# CREATE TABLE IF NOT EXISTS registrar (
#    registrationKey INTEGER PRIMARY KEY AUTOINCREMENT
#    , studentId_fk bigint
#    , courseId_fk bigint);
# """
# )

# cur.execute("""
# CREATE TABLE IF NOT EXISTS grades (
#    gradeKey INTEGER PRIMARY KEY AUTOINCREMENT
#    , courseId_fk bigint
#    , studentId_fk bigint
#    , grade int);
# """
# )

# con.commit()
# con.close()