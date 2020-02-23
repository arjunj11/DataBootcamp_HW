
// <select id="selDataset" onchange="optionChanged(this.value)"></select>


d3.json("././samples.json").then(function(data){

    d3.select("#personid").on("change",yesman)
    function yesman(){
        var person = d3.select("#personid").property("value")
        console.log(data.samples)
        data.samples.forEach(element => {
            for (z=0;z<element.otu_ids.length;z++){
                if(element.otu_ids[z]==2722){console.log(element)}
            }
        });
        //console.log(b)
        var a = data.samples.filter( d=> (d.id == person))
        console.log(a)
        var otudis = a.map(d=>d.otu_ids)
        var samplevalues = a.map(d=>d.sample_values);
        var otulabels=[];
        var hoverlabels= a.map(d=>d.otu_labels)[0].slice(0,10).reverse();
        (otudis[0].slice(0,10)).forEach(function(d){
            otulabels.push(`OTU ID ${String(d)}`)
        })
        console.log(hoverlabels)
        trace1 ={
            x:samplevalues[0].slice(0,10).sort((a,b)=>(a-b)),//sorting and slicing the samplevalues
            y:otulabels.reverse(),
            text:hoverlabels ,
            type:"bar",
            orientation:'h'
        } 
        ldata=[trace1];
        layout = {
            xaxis: { 
                title:"Sample Values"
            },

            //margin: { t: 0 },
            
            //margin: { t: 30}
        }
        Plotly.newPlot("bar",ldata,layout)

        trace2 ={
            x:otudis[0],
            y:samplevalues[0],
            text:hoverlabels ,
            mode:"markers",
            marker:{
                color:otudis[0],
                size:samplevalues[0]
            }
        } 
        ldata2=[trace2];
        layout2 = {
            title: 'Marker Size',
            showlegend: false,
            height: 600,
            width: 1200,
            xaxis: { 
                title:"OTU ID"
            },
          }
        Plotly.newPlot("bubble",ldata2,layout2)
        
        var a1=data.metadata.filter(d=>d.id==person);
        console.log(a1[0])
        console.log(Object.entries(a1[0]))
        console.log((Object.entries(a1[0])).length)
        for (i=0;i<((Object.entries(a1[0])).length);i++){
            d3.select("#sample-metadata").append("li")
            .text(`${(Object.entries(a1[0]))[i][0]}:${(Object.entries(a1[0]))[i][1]}`)
        }
        
        var data3 = [
            {
                domain: { x: [0, 1], y: [0, 1] },
                value: (Object.entries(a1[0]))[6][1],
                title: { text: "Washing frequency of the person" },
                type: "indicator",
                mode: "gauge+number"
            }
        ];
        
        var layout3 = { width: 500, height: 500, margin: { t: 0, b: 0 } };
        Plotly.newPlot('gauge', data3, layout3);
    }
})