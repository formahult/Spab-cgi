#!/home1/therevpr/opt/python27/bin/python
import sys
import cgi
import json
import sqlite3
import cgitb
## enable displaying debug information in html
# cosider commenting this out for deployment
cgitb.enable()

# open the db
db = sqlite3.connect('../db/spabLocation.db')
cursor = db.cursor()

##############################
# future students avoid SQL Injections
# # Never do this -- insecure!
# symbol = 'RHAT'
# c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)
#
# # Do this instead
# t = ('RHAT',)
# c.execute('SELECT * FROM stocks WHERE symbol=?', t)
# print(c.fetchone())
###############################


# http header, must contain this in order to function.
print "Content-type: application/json\n\n"

try:
    #print lines
    data = json.load(sys.stdin)
    for elem in data:
        values = (elem["timestamp"], elem["latitude"], elem["longitude"])
        cursor.execute("INSERT INTO Locations (Timestamp, Latitude, Longitude) VALUES (?, ?, ?)",
values)
    db.commit()
    print('{"success":"true","message":"Inserted successfully"}')
except ValueError:
    print('{"success":"false","message":"JSON could not be decoded"}')
except:
    print('{"success":"false","message":"Unspecified error"}')

db.close()
