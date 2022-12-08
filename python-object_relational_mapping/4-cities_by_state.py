#!/usr/bin/python3
# script that lists all cities from the database hbtn_0e_4_usa
# script should connect to a MySQL server running on localhost at port 3306
# You must use the module MySQLdb (import MySQLdb)
"""import 'sys' & 'MySQLdb'."""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    m = db.cursor()
    m.execute("SELECT `m`.`id`, `m`.`name`, `s`.`name` \
                 FROM `cities` as `m` \
                INNER JOIN `states` as `s` \
                   ON `m`.`state_id` = `s`.`id` \
                ORDER BY `m`.`id`")
    [print(city) for city in m.fetchall()]
