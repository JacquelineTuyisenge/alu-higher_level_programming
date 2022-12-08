#!/usr/bin/python3
# script that takes in an argument and displays all values
# in the states table of hbtn_0e_0_usa where name matches the argument.
"""import 'sys' & 'MySQLdb'."""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    b = db.cursor()
    b.execute("SELECT * \
                 FROM `states` \
                WHERE BINARY `name` = '{}'".format(sys.argv[4]))
    [print(state) for state in b.fetchall()]
