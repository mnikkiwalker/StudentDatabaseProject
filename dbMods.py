import sqlite3 as sql

#establishing database connection
con = sql.connect("studentData.db")
cur = con.cursor()


cur.execute(
    """
DROP TABLE students    
"""
)

con.commit()
con.close()