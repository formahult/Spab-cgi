#!/home1/therevpr/opt/python27/bin/python
import sys
import cgi
import sqlite3
import cgitb
## enable displaying debug information in html
# cosider commenting this out for deployment
cgitb.enable()

# open the db
db = sqlite3.connect('../../db/spabLocation.db')
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
print "Content-type: text/html"
print

# header block
print """
<meta charset="UTF-8">
<html>
<head>
<title>Solar Powered Autonomous Boat</title>

</head>
"""

print """
<body>

"""
arguments = cgi.FieldStorage()

try:
    time = arguments["t"].value
    latitude = arguments["lat"].value
    longitude = arguments["long"].value

    cursor.execute("INSERT INTO Locations (Timestamp, Latitude, Longitude) VALUES (?, ?, ?)", (time, latitude, longitude))
    db.commit()
    print"Success"
except KeyError:
    print"Error"
except DatabaseError:
    print"DB Error"

db.close()
print """
</body>
</html>
"""
