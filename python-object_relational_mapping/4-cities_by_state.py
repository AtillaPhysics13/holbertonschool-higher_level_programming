#!/usr/bin/python3
"""Module for selecting cities"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cursor = db.cursor()

    cursor.execute("""SELECT cities.id, cities.name, states.name
                      FROM cities
                      JOIN states ON cities.state_id = states.id
                      ORDER BY cities.id ASC""")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
