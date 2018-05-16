var mymap = L.map('mapid').setView([-31.98, 115.81], 13);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoidXdhc29sYXJib2F0IiwiYSI6ImNqaDh0OGk3dzAzazMzNmw4bnU0cjV1aG0ifQ.FP5p--Ilf_4WIGdKszDxbg', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox.streets',
    accessToken: 'pk.eyJ1IjoidXdhc29sYXJib2F0IiwiYSI6ImNqaDh0OGk3dzAzazMzNmw4bnU0cjV1aG0ifQ.FP5p--Ilf_4WIGdKszDxbg'
}).addTo(mymap);
