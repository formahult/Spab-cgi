#!/home1/therevpr/opt/python27/bin/python
import sys
import cgi
import sqlite3
import cgitb
import json
import time
import random
## enable displaying debug information in html
# cosider commenting this out for deployment
cgitb.enable()

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
print "Content-type: application/json"
print

# open the db
try:
    db = sqlite3.connect('db/spabLocation.db')
    cursor = db.cursor()
except Exception as e:
    print('[{"type":"command"},{"action":"failure","message":"' + str(e) + '"}]')

try:
    # Get the latest command only.
    cursor.execute("SELECT * FROM Commands WHERE Active=1;")
except Exception as e:
    print('[{"type":"command"},{"action":"failure","message":"' + str(e) + '"}]')

try:
    row = cursor.fetchone()
    object = []
    object.append({"type":"command"})
    while row is not None:
        timestamp = int((time.time() - 1420070400) * 100000) #spab wants times in us from 1/1/2015
        ranint = random.randrange(10**80)
        somehex = "%064x" % ranint
        tid = somehex[0:9] + "-" + somehex[9:13] + "-" + somehex[13:17] + "-" + somehex[17:21] + "-" + somehex[21:33]
        object.append({"action":str(row[2]), "timestamp":str(timestamp), "latitude":str(row[3]),
"longitude":str(row[4]), "taskId":str(tid)})
        row = cursor.fetchone()
    print(json.dumps(object))
except Exception as e:
    print('[{"type":"command"},{"action":"failure","message":"' + str(e) + '"}]')
