#!/home1/therevpr/opt/python27/bin/python
import sys
import cgi
import sqlite3
import cgitb
## enable displaying debug information in html
# cosider commenting this out for deployment
cgitb.enable()

# open the db
try:
    db = sqlite3.connect('../db/spabLocation.db')
    cursor = db.cursor()
except:
    print "Error,DB Connection"

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

try:
    # Get the latest command only.
    cursor.execute("SELECT * FROM Commands ORDER BY ID DESC LIMIT 1;")
except:
    print "Error,DB Execution"

try:
    row = cursor.fetchone()
    if row is not None:
        s = 'Command,'
        for elem in row[2:]:
            s += str(elem) + ","
        print s
except:
    print("Error,Generic")
