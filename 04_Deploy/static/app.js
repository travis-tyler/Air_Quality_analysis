function buildPlot() {
    // let d3;
    // let Plotly;

    /* data route */
    const url = "/county";
    d3.json(url).then(function(response) {

        console.log(response.date);


        // Trace for 2020 data
        const trace2020 = {
            x: response.date,
            y: response.aqi_2020,
            type:"line",
            name:"2020 AQI"
        };

        // Trace for 5y data
        const trace5y = {
            x: response.date,
            y: response.avg_5y,
            type: "line",
            name: "5Y average"
        };

        const data = [trace2020, trace5y];

        // Layout for line graph
        const layout = {
            title: "2020 AQI vs. 5Y average",
            height: 700,
            width: 1000,
            xaxis: {
                title: "Date"
              },
              yaxis: {
                title: "Air quality index",
                tick0: 0,
              },
            paper_bgcolor: 'rgba(0,0,0,0)',
            plot_bgcolor: 'rgba(0,0,0,0)'        
        };

        Plotly.newPlot("plot", data, layout);
    });
}

buildPlot();

