#!/home1/therevpr/opt/python27/bin/python
import sys
import cgi
import sqlite3
import cgitb
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
validCommands = ('hold', 'moveto')

try:
    if arguments['command'].value in validCommands:
        # un set old command
        cursor.execute("UPDATE Commands SET Active=0 WHERE Active=1")
        # set new command
        if arguments['command'].value == 'hold':
            values = (1, arguments['command'].value)
            cursor.execute("INSERT INTO Commands (Active, Command) VALUES (?, ?)", values)
        elif arguments['command'].value == 'moveto':
            values = (1, str(arguments['command'].value), float(arguments['lat'].value),float(arguments['long'].value))
            cursor.execute("INSERT INTO Commands (Active, Command, Latitude, Longitude) VALUES (?, ?, ?, ?)", values)
        db.commit()
        print "<h2>Command Saved</h2>"
    else:
        print "<h2>Error Parsing Commands</h2>"
except KeyError:
    pass

print """
<h2>Current Status</h2>
At Time:
<h3>Waypoints</h3>
<h3>Battery Voltage</h3>
<h3>Leaks</h3>
<h2>Queue Command</h2>
<p>Choose one of the following commands to queue. Commands in the same set will overide previous
commands of the same set.</p>
<form action="./command.cgi" method="post" accept-charset="utf-8" autocomplete="off">
<fieldset>
<legend>Navigation:</legend>
<input type="radio" name="command" value="moveto">Go To:
Latitude: <input type="text" name ="lat">
Longitude: <input type="text" name="long"><br>
</fieldset>

<input type="submit" value="Submit">
</form>
"""


print """
</body>
</html>
"""
