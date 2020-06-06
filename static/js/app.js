// Complete the function and build a dropdown option.
//Use D3.json to fetch the metadata for sample

function buildPlot(id) {
   
    // load data from samples.json file
   
    d3.json("samples.json").then((data) => {
        console.log(data)
        var wfreq = data.metadata.map(d => d.wfreq)

        // values by its ID
        var samples = data.samples.filter(s => s.id.toString() === id)[0];

        // sample of top 10
        var samplevalues = samples.sample_values.slice(0, 10).reverse();

        // Get only the top 10 by slice
        var OTU_top = (samples.otu_ids.slice(0, 10)).reverse();

        // Ids
        var OTU_id = OTU_top.map(d => "OTU " + d)

        // get the top 10 labels
        var labels = samples.otu_labels.slice(0, 10).reverse();

        var trace = {
            x: samplevalues,
            y: OTU_id,
            text: labels,
            marker: {
                color: 'rgb(52,235,134)'
            },
            type: "bar",
            orientation: "h",
        };

        // create data variable
        var data = [trace];

        // create layout 
        var layout = {
            title: "Top 10 OTU Data Set ",
            yaxis: {
                tickmode: "linear",
            },
            margin: {
                l: 30,
                r: 30,
                t: 30,
                b: 100
            }
        };

        // Create a Bar _Plot
        Plotly.newPlot("bar", data, layout);

        // Bubble Chart
        var trace1 = {
            x: samples.otu_ids,
            y: samples.sample_values,
            mode: "markers",
            marker: {
                size: samples.sample_values,
                color: samples.otu_ids
            },
            text: samples.otu_labels


        };

        // Bubble Chart layout
        var layout_b = {
            xaxis: { title: "OTU ID" },
            height: 600,
            width: 1000
        };

        // creating data variable 
        var data1 = [trace1];

        // create the bubble plot
        Plotly.newPlot("bubble", data1, layout_b);


    });
}
// create the function to get the necessary data

function dropdowninfo(id) {

    d3.json("samples.json").then((data) => {

        // Get the meta Data
        var metadata = data.metadata;

        console.log(metadata)

        // filter meta data info by id
        var result = metadata.filter(meta => meta.id.toString() === id)[0];

        // select demographic panel to put data
        var demographicInfo = d3.select("#sample-metadata");

        // empty the demographic info panel each time before getting new id info
        demographicInfo.html("");

        // grab the necessary demographic data data for the id and append the info to the panel
        Object.entries(result).forEach((key) => {
            demographicInfo.append("h5").text(key[0] + ": " + key[1] + "\n");
        });
    });
}

// create the function for the change event
function optionChanged(id) {
    buildPlot(id);
    dropdowninfo(id);
}

// create the function for the initial data rendering

function init() {
    
    // select dropdown menu 
    var dropdown = d3.select("#selDataset");
 
    d3.json("samples.json").then((data) => {
        console.log(data)

        // drop down IDs
        data.names.forEach(function(name) {
            dropdown.append("option").text(name).property("value");
        });

        // Display the data and plot
        buildPlot(data.names[0]);
        dropdowninfo(data.names[0]);
    });
}

init();