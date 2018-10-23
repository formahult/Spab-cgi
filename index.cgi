#!/home1/therevpr/opt/python27/bin/python
import sys
import cgi
import sqlite3
import cgitb

# enable displaying debug information in html
# cosider commenting this out for deployment
cgitb.enable()

# connect to the DB
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

#### Render the webpage in html ###
# setup the html
print "Content-type: text/html"
print

# setup the head
print """
<meta charset="UTF-8">
<html>
<head>
<title>Solar Powered Autonomous Boat</title>

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.3.1/dist/leaflet.css"
integrity="sha512-Rksm5RenBEKSKFjgI3a41vrjkw4EVPlJ3+OiI65vTjIdo9brlAacEuKOiQ5OFh7cOI1bkDwLqdLw3Zg0cRJAAQ=="
   crossorigin=""/>

<script src="https://unpkg.com/leaflet@1.3.1/dist/leaflet.js" integrity="sha512-/Nsx9X4HebavoBvEBuyp3I7od5tA0UzAxs+j83KgC8PU0kgB4XiK4Lfe4y4cgBtaRJQEIFCW+oC506aPT2L1zw==" crossorigin=""></script>
</head>
"""

arguments = cgi.FieldStorage()

try:
    limit = arguments["limit"].value
    limit = (limit,)
except:
    # if no limit specified, return everything the boat never sailed before 2018
    limit = ('2000-01-01 12:00:00',)

try:
    cursor.execute("SELECT * FROM Locations WHERE Timestamp>=?", limit)
except:
    print "<h1>DB Execution Error</h1>"

# setup where the map will go
print """
<body>

<h1>Solar Powered Boat</h1>
<div style="height: 720px; width: 1440;" id="mapid"></div>
"""

# form for setting date limit
print """
<form>
<h2>Show after date:</h2>
<input type="text" name="limit">
<input type="submit">
</form>
"""

print """
<script type="text/javascript" src="js/map.js"></script>
"""

print """
<script type="text/javascript">
"""
row = cursor.fetchone()
while row is not None:
    print "var marker = L.marker([" + str(row[2]) + "," + str(row[3]) + "]).addTo(mymap);"
    print 'marker.bindPopup("' + str(row[1]) + ":" + str(row[2]) + "," + str(row[3]) + '");'
    row = cursor.fetchone()

print "</script>"

print """
</body>
</html>
"""
