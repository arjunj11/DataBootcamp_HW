d3.csv("assets/data/data.csv").then(function(data){

    var trace1={
        x:data.map(d=>d.poverty),
        y:data.map(d=>d.healthcare),
        type:"scatter",
        mode:'markers+text',
        marker:{size:20},
        text:data.map(d=>d.abbr),
        textposition:'center',
        textfont:{
            color:'white'
        },
        opacity:0.5
    }
    data=[trace1]
    layout={
        x:{
            title:"Healthcare"
        },
        y:{
            title:"Poverty"
        }
    }
    Plotly.newPlot("scatter",data,layout)
})




// var trace1 = {
//     x:data.map(god=>god.pair),
//     y:data.map(god=>god.greekSearchResults),
//     type:"scatter",
//     text : data.map(god=>god.greekName),
//     name:"Greek"
// }

// var trace2 = {
//     x:data.map(god=>god.pair),
//     y:data.map(god=>god.romanSearchResults),
//     type:"scatter",
//     text : data.map(god=>god.romanName),
//     name:"Roman"
// }

// data=[trace1,trace2]
// layout={}

// Plotly.newPlot("plot",data,layout)
