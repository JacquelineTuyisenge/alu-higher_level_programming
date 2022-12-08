#!/usr/bin/python3
# script that lists all 'states' from the database 'hbtn_0e_0_usa'
"""import 'sys' & 'MySQLdb'."""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    b = db.cursor()
    b.execute("SELECT * FROM `states`")
    [print(state) for state in b.fetchall()]
