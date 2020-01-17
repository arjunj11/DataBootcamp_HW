// from data.js

var tableData = data;
// YOUR CODE HERE!
var tbody=d3.select("tbody");
// grab the searched date
//tableData.forEach(addin)
d3.selectAll("#filter-btn").on("click",searchappend)
//defining a function for checking the value of the search

function searchappend(){
    var grab = d3.select("#datetime").property("value")
    console.log(grab)
    
    if ((tableData.map(a=>a.datetime)).includes(grab)){
        
        console.log("Eurekaaaaaaaaaaa")
        //var tableData1 = tableData.filter(row=>(grab==row.datetime));
        var tableData1 = tableData.filter(function(row){
            if(grab==row.datetime){return true}
            else{return false}
        });
    }
    else if (grab==""){
        var tableData1 = tableData;
        console.log("nothing")
    }
    else if (grab=="refresh"){
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


//filter the data showing only the searched item based on date
//tableData.filter()



