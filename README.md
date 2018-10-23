# Spab-cgi
CGI interface for controlling/monitoring the SPAB. Don't break the main therevproject.com website. Probably best to keep everything in /spab.

## Leaflet
The map for displaying locations is powered by [Leaflet.js](https://leafletjs.com/examples.html).

## DB
Keep any databases in this directory. It should never be publicly available, otherwise people could delete it if they wanted to. Using `deny from all` in the .htaccess file should prevent trivial access to it.

If the database ever gets destroyed running `sqlite3 initSpabDB.sql` should recreate all the necessary tables to get things working.

## JS
For the sake of clarity keep any javascript sources here. There is no harm in this folder being publicly accessible. In fact it must be.

## Secure Directory
Certain interfaces such as the command.cgi and data.cgi should be placed in a secure sub directory and require HTTP Basic Auth or similar. This was on my TO DO list but I ran out of time. This will require rewriting client side scripts to deal with the basic authentication however.

The /db folder should not be publicly accessible and already contains
