#!/usr/bin/python3
"""
Script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches
the argument.

Arguments:
    1: mysql username
    2: mysql password
    3: database name
    4: state name searched
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create cursor
    cursor = db.cursor()

    # Execute query
    cursor.execute(
        "SELECT * FROM states "
        "WHERE name LIKE BINARY 'N%' "
        "ORDER BY states.id ASC"
    )

    # Fetch all results
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

    # Close connection
    cursor.close()
    db.close()
