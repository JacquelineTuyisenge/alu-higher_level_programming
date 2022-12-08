#!/usr/bin/python3
# script that lists all 'states' with a name starting with 'N'
"""import 'sys' & 'MySQLdb'."""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    b = db.cursor()
    b.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in b.fetchall() if state[1][0] == "N"]
