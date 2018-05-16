#!/home1/therevpr/opt/python27/bin/python

import sys
import cgi

print "Content-type: text/html"
print


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
<body>

<h3>Solar Powered Boat</h3>
<div style="height: 360px; width: 720;" id="mapid"></div>
"""

print "<p> Args</p>"
arguments = cgi.FieldStorage()
for key in arguments.keys():
	print key + ":" + arguments[key].value + "<br>"

print """
<script type="text/javascript" src="../js/map.js"></script>
"""

print """
</body>
</html>
"""
