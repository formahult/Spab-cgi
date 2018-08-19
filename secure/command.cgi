#!/home1/therevpr/opt/python27/bin/python
import sys
import cgi
import sqlite3
import cgitb
#import cgitb
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
print "Content-type: text/html"
print

# header block
print """
<meta charset="UTF-8">
<html>
<head>
<title>SPAB Commander</title>

</head>
"""

print """
<body>
<h1>SPAB Commander</h1>
"""

arguments = cgi.FieldStorage()
validCommands = ('hold', 'goto')

if arguments['command'] in validCommands:
    # un set old command
    cursor.execute("UPDATE Comamnds SET Active=0 WHERE Active=1")
    # set new command
    if arguments['command'] == 'hold':
        values = (1,arguments['command'])
        cursor.execute("INSERT INTO Commands (Active, Command) VALUES (?, ?)", values)
    else if arguments['command'] == 'goto'
        values = (1,arguments['command'], str(arguments['lat']) + ',' + str(arguments['long']))
        cursor.execute("INSERT INTO Commands (Active, Command, Arguments) VALUES (?, ?, ?)", values)
    db.commit()
else:
    print "<h2>Error Parsing Commands</h2>"

print """
<h2>Current Status</h2>
At Time:
<h3>Waypoints</h3>
<h3>Battery Voltage</h3>
<h3>Leaks</h3>
<h2>Queue Command</h2>
<p>Choose one of the following commands to queue. Commands in the same set will overide previous commands of the same set.</p>
<form action="./command.cgi" method="post" accept-charset="utf-8" autocomplete="off">
<fieldset>
<legend>Navigation:</legend>
<input type="radio" name="command" value="goto">Go To:
Latitude: <input type="text" name ="lat">
Longitude: <input type="text" name="long"><br>
<input type="radio" name="command" value="goway">Go To
Waypoint: <input type="text" name="index"><br>
<input type="radio" name="command" value="hold">Hold Position<br>
<input type="radio" name="command" value="course">Set Course:
<input type="text" name="course"><br>
</fieldset>

<!--
<fieldset>
<legend>Configuration:</legend>
<input type="radio" name="command" value="newway">New Waypoint:
Index: <input type="text" name="index">
Latitude: <input type="text" name ="lat">
Longitude: <input type="text" name="long"><br>
<input type="radio" name="command" value="delway">Delete Waypoint:
Index: <input type="text" name="index"><br>
</fieldset>
-->

<input type="submit" value="Submit">
</form>
"""


print """
</body>
</html>
"""
