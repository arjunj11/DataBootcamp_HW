
// <select id="selDataset" onchange="optionChanged(this.value)"></select>


d3.json("././samples.json").then(function(data){
    d3.select("#personid").on("click",yesman)
    function yesman(){
        var person = d3.select("#personid").attr("value")
        console.log(person)
    }
    var a =data.samples.filter( d=> (d.id == "940"))
    var b = a.map(d=>d.otu_ids)
    console.log(b[0])
    trace1 ={
        x:data.samples.map(d=>d.sample_values),
        y:data.samples.map(d=>d.otu_ids),
        type:"bar",
        orientation:'h'
    } 
    var ldata=[trace1];
    var layout = {
        xaxis: { 
            title:"Sample Values"
        },
        yaxis:{
            title:"OTU_IDs"
        }
    }
    Plotly.newPlot("bar",ldata,layout)



})