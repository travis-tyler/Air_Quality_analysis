function buildPlot(county) {

    /* data route */
    const url = `/county_data?county=${county}`;
    d3.json(url).then(function(response) {

        // Trace for 2020 data
        let trace2020 = {
            x: response.date,
            y: response.aqi_2020,
            type:"line",
            name:"2020 AQI"
        };

        // Trace for 5y data
        let trace5y = {
            x: response.date,
            y: response.avg_5y,
            type: "line",
            name: "5Y average"
        };

        let data = [trace2020, trace5y];

        // Layout for line graph
        let layout = {
            title: "2020 AQI vs. 5Y average",
            height: 700,
            width: 1200,
            xaxis: {
                title: "Date"
              },
              yaxis: {
                title: "Air quality index",
                tick0: 0
              },
            paper_bgcolor: 'rgba(0,0,0,0)',
            plot_bgcolor: 'rgba(0,0,0,0)',
            font: {
                color: "white"
            }        
        };

        Plotly.newPlot("plot", data, layout);
    });
}

// Select dropdown menu using D3
var selectDrop = d3.select("#selDataset");


// Create event handler
selectDrop.on("change",runEnter);
// Event handler function
function runEnter() {
    // Prevent the page from refreshing
    d3.event.preventDefault();
    // Select the input element and get HTML node
    var inputElement = d3.select("select");
    // Get the value property of the input element
    var userCounty = inputElement.property("value");

    buildPlot(userCounty);
};





