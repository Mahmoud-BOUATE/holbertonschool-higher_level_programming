#!/usr/bin/python3
"""
Script that lists all states from a MySQL database.
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
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'  ORDER BY id ASC")

    # Fetch all results
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

    # Close connection
    cursor.close()
    db.close()
