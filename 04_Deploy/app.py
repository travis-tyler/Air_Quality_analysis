# Import libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
app = Flask(__name__)

#################################################
# Database Setup
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create engine
# Note: User will need to supply their own PostgreSQL password under variable below
user = 'postgres'
host = 'localhost'
password = 'thehawk-2002'
port = '5432'
db = 'avg_aqi'
uri = f'postgresql://{user}:{password}@{host}:{port}/{db}'

engine = create_engine(uri)

state = 'California'
county = 'Riverside'

sql = engine.execute(f"SELECT date, aqi, five_year_avg FROM aqi_2020 WHERE county = '{county}'")

results = []
for x in sql:
    results.append(list(x))




all_states = []
states = engine.execute(f"SELECT DISTINCT state FROM aqi_2020 ORDER BY state")
for s in states:
    all_states.append(s[0])

all_counties = []
counties = engine.execute(f"SELECT DISTINCT county FROM aqi_2020 WHERE state = '{state}' ORDER BY county")
for c in counties:
    all_counties.append(c[0])





# create route that renders index.html template
@app.route("/")
def home():
    # return jsonify(all_states)
    return render_template('index.html', state_list=all_states, county_list=all_counties)

# @app.route("/county")
# def county_data():
#     return jsonify(aqi_data)

@app.route("/test" , methods=['GET', 'POST'])
def test():

    # if request.method == "POST":
    county = request.form['selCounty']

    # county = request.form.get('selCounty')

    dates = []
    query_dates = engine.execute(f"SELECT date FROM aqi_2020 WHERE county = '{county}' ORDER BY date")
    for date in query_dates:
        dates.append(date[0])

    aqi_2020 = []
    query_api_2020 = engine.execute(f"SELECT aqi FROM aqi_2020 WHERE county = '{county}' ORDER BY date")
    for api in query_api_2020:
        aqi_2020.append(api[0])

    aqi_5y = []
    query_api_5y = engine.execute(f"SELECT five_year_avg FROM aqi_2020 WHERE county = '{county}' ORDER BY date")
    for api in query_api_5y:
        aqi_5y.append(api[0])

    aqi_data = {
        "date": dates,
        "aqi_2020": aqi_2020,
        "avg_5y": aqi_5y
    }

    print(county)
    print(aqi_data)

    return jsonify(aqi_data)




if __name__ == "__main__":
    app.run(debug=True)
