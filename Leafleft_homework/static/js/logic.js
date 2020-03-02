// API key
var API_KEY = "pk.eyJ1IjoiYXJqdW4xMSIsImEiOiJjazV4M3IzNWMwMXY0M2VsNXZvaXBnYWE1In0.0uWUvBwL6pdmSQTIURjVfw";


function createMap(EQStations) {

    // Create the tile layer that will be the background of our map
    var lightmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?access_token={accessToken}", {
      attribution: "Map data &copy; <a href=\"http://openstreetmap.org\">OpenStreetMap</a> contributors, <a href=\"http://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"http://mapbox.com\">Mapbox</a>",
      maxZoom: 20,
      id: "mapbox.light",
      accessToken: API_KEY
    });
  
    // Create a baseMaps object to hold the lightmap layer
    var baseMaps = {
      "Light Map": lightmap
    };
  
    // Create an overlayMaps object to hold the EQStations layer
    var overlayMaps = {
      "EQ Stations": EQStations
    };
  
    // Create the map object with options
    var map = L.map("map", {
      center: [0, 0],
      zoom: 2, 
      layers: [lightmap,EQStations]
    });
  
    // Create a layer control, pass in the baseMaps and overlayMaps. Add the layer control to the map
    L.control.layers(baseMaps,overlayMaps, {
      collapsed: false
    }).addTo(map);

    //creating a legend
    var legend = L.control({
        position: "bottomright"
    });

    legend.onAdd = function(){
        var div = L.DomUtil.create("div","infolegend");
        return div;
    }
    
    legend.addTo(map);
    document.querySelector(".infolegend").innerHTML=legendshow();

  }
  
  function createMarkers(response) {

    var EQMarkers = [];
    
    var stations = response.features
    function colorchooser(mag){
        
        if (mag>=0 && mag<1) {color = "#E6B0AA"}
        else if (mag>=1 && mag<2) {color = "#D98880"}
        else if (mag>=2 && mag<3) {color = "#C0392B"}
        else if (mag>=3 && mag<4) {color = "#A93226"}
        else if (mag>=4 && mag<5) {color = "#922B21"}
        else {color = "#641E16"}
        return color;
    }
    // Loop through the stations array
    for (var index = 0; index < stations.length; index++) {
        
        var EQMarker = L.circle([stations[index].geometry.coordinates[1],stations[index].geometry.coordinates[0]],{
                fillOpacity: 0.75,
                color: colorchooser(stations[index].properties.mag),
                // Adjust radius
                radius: stations[index].properties.mag * 15000
              }).bindPopup("<h3>" + stations[index].properties.place + "</h3><h3>Magnitude: "+ stations[index].properties.mag);
      EQMarkers.push(EQMarker);
      
    }
    
    //Create a layer group made from the bike markers array, pass it into the createMap function
    createMap(L.layerGroup(EQMarkers));
  }
  
  function legendshow(){
    var legendInfo = [{limit: "0-1",color: "#E6B0AA"},
        {limit: "1-2",color: "#D98880"},{limit:"2-3",color:"#C0392B"},{limit:"3-4",color:"#A93226"},{limit:"4-5",color:"#922B21"},
        {limit:"5+",color:"#641E16"}];

    var header = "<h3>Magnitude</h3>";

    var bc = "";
   
    for (i = 0; i < legendInfo.length; i++){
        bc += "<p style = \"background-color: "+legendInfo[i].color+"\">"+legendInfo[i].limit+"</p> ";
    }
    
    return header+bc;

}
  
  // Perform an API call to the Citi Bike API to get station information. Call createMarkers when complete
  d3.json("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson", createMarkers);