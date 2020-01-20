// from data.js

var tableData = data;
// YOUR CODE HERE!
var tbody=d3.select("tbody");

function refreshed(){
    window.location.reload()
}

d3.select("#filter-btn").on("click",searchappend)

d3.select("#refresh").on("click",refreshed)
//defining a function for checking the value of the search

function searchappend(){
    
    var grabdate = d3.select("#datecol").property("value")
    console.log(grabdate)
    var grabcity = d3.select("#citycol").property("value")
    console.log(grabcity)
    var grabstate = d3.select("#statecol").property("value")
    console.log(grabstate)
    var grabcountry = d3.select("#countrycol").property("value")
    console.log(grabcountry)
    var grabshape = d3.select("#shapecol").property("value")
    console.log(grabshape)
    
    if ((tableData.map(a=>a.datetime)).includes(grabdate)){
        
        console.log("Eurekaaaaaaaaaaa")
        //var tableData1 = tableData.filter(row=>(grabdate==row.datetime));
        var tableData1 = tableData.filter(function(row){
            if(grabdate==row.datetime){return true}
            else{return false}
        });

    }
    else if (grabdate==""){
        var tableData1 = tableData;
        console.log("nothing")
    }
    else if (grabdate=="refresh"){
        window.location.reload();
    }
    else{
        var tableData1 = [];
        console.log("search doesnt match")
    }
    // check for city
    if ((tableData1.map(a=>a.city)).includes(grabcity)){
        console.log("city")
        var tableData1 = tableData1.filter(row=>grabcity==row.city)        
    }
    else if (grabcity==""){
        var tableData1 = tableData1;
        console.log("citynothing")
    }
    else if (grabdate=="refresh"){
        window.location.reload();
    }
    else{
        var tableData1 = [];
        console.log("search doesnt match")
    }
    // check for State
    if ((tableData1.map(a=>a.state)).includes(grabstate)){
        console.log("state")
        var tableData1 = tableData1.filter(row=>grabstate==row.state)        
    }
    else if (grabstate==""){
        var tableData1 = tableData1;
        console.log("statenothing")
    }
    else if (grabstate=="refresh"){
        window.location.reload();
    }
    else{
        var tableData1 = [];
        console.log("search doesnt match")
    }
    // check for country
    if ((tableData1.map(a=>a.country)).includes(grabcountry)){
        console.log("country")
        var tableData1 = tableData1.filter(row=>grabcountry==row.country)        
    }
    else if (grabcountry==""){
        var tableData1 = tableData1;
        console.log("countrynothing")
    }
    else if (grabcountry=="refresh"){
        window.location.reload();
    }
    else{
        var tableData1 = [];
        console.log("search doesnt match")
    }
    // check for shape
    if ((tableData1.map(a=>a.shape)).includes(grabshape)){
        console.log("shape")
        var tableData1 = tableData1.filter(row=>grabshape==row.shape)        
    }
    else if (grabshape==""){
        var tableData1 = tableData1;
        console.log("shapenothing")
    }
    else if (grabshape=="refresh"){
        window.location.reload();
    }
    else{
        var tableData1 = [];
        console.log("search doesnt match")
    }
    //console.log(Object.values(tableData1.map(row=>row.datetime)));
    
    tableData1.forEach(addin)
}


function addin(tablerows){
    var row = tbody.append("tr")
    row.append("td").text(tablerows.datetime)
    row.append("td").text(tablerows.city)
    row.append("td").text(tablerows.state)
    row.append("td").text(tablerows.country)
    row.append("td").text(tablerows.shape)
    row.append("td").text(tablerows.durationMinutes)
    row.append("td").text(tablerows.comments)
}

console.log(tableData);

//filter the data showing only the searched item based on date
//tableData.filter()



