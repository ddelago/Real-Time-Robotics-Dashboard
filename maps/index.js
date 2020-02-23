
var mymap = L.map('mapid').setView([32.732580, -97.113244], 1);
var url = 'RequestTiles/tiles/{z}/{x}/{y}.png';
var options = { 
    attribution: 'Map data',
    maxZoom: 20,
    minZoom: 5
}

L.tileLayer(url, options).addTo(mymap);

var marker = L.marker([32.732580, -97.113244]).addTo(mymap);

var circle = L.circle([51.508, -0.11], {
    color: 'red',
    fillColor: '#f03',
    fillOpacity: 0.5,
    radius: 500
}).addTo(mymap);

var polygon = L.polygon([
    [51.509, -0.08],
    [51.503, -0.06],
    [51.51, -0.047]
]).addTo(mymap);
