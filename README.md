# Visualizing Air Quality Analysis
### An analysis of trends of air quality indexes in the U.S.

How does U.S. air quality in 2020 compare to previous years given the coronavirus pandemic, nationwide lockdowns, economic slowdown, and decreased travel? 

We will look at air quality data collected from the EPA for multiple locations in the U.S. This data will be downloaded as several CSV files, cleaned using Python/Pandas, fed into SQL, and used to create visualizations, which we will display on our Flask-powered app. 

We will be looking at the daily AQIs (air quality indexes) for counties across the U.S. in 2019 and 2020. These datasets will be cleaned, filtered, and merged on county code, then fed into SQL. We will use JS/Plotly to graph the data. The user will be able to select a specific county from a dropdown menu. The site will also employ a JS library that allows us to display a Tableau dashboard, which will provide more visualizations. 

### Tools Used for the Project:<br />
Back end database:  SQL Database, SQLite<br />
Front end:  HTML, CSS, JavaScript<br />
Connecting front end and back end:  Python Flask<br />
Charts:  JavaScript Libraries ( Plotly)<br />
Deploying Application:  Heroku
