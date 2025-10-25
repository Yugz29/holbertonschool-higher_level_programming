#!/usr/bin/python3
"""
Connects to a MySQL database and lists all states from the `states`
table where the state's name matches the given argument. This version
is safe from MySQL injections by using parameterized queries.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC",
        (state_name,)
    )

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    db.close()
