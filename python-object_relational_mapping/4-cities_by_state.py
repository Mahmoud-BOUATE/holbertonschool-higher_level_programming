#!/usr/bin/python3
"""Script that lists all cities with their state names."""
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
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )

    # Fetch all results
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

    # Close connection
    cursor.close()
    db.close()
