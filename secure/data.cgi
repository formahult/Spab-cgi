#!/home1/therevpr/opt/python27/bin/python
import sys
import cgi
import json
import sqlite3
import cgitb
import datetime
## enable displaying debug information in html
# cosider commenting this out for deployment
cgitb.enable()

# open the db
db = sqlite3.connect('db/spabLocation.db')
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
    data = json.load(sys.stdin)
    for elem in data:
        timestamp = elem["timestamp"]/100000 + 1420070400
        dateTime = datetime.datetime.fromtimestamp(timestamp)
        dateString = dateTime.strftime('%Y-%m-%d %H:%M:%S')
        values = (dateString, elem["latitude"], elem["longitude"])
        cursor.execute("INSERT INTO Locations (Timestamp, Latitude, Longitude) VALUES (?, ?, ?)",
values)
    db.commit()
    print('[{"type":"telemAck"},{"success":"true","message":"Inserted successfully"}]')
except ValueError:
    print('[{"type":"telemAck"},{"success":"false","message":"JSON could not be decoded"}]')
except Exception, e:
    print('[{"type":"telemAck"},{"success":"false","message":'+ str(e) + '}]')

db.close()
