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
password = 'PASSWORD'
port = '5432'
db = 'avg_aqi'
uri = f'postgresql://{user}:{password}@{host}:{port}/{db}'

engine = create_engine(uri)

state = 'Alabama'
county = 'Baldwin'

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



dates = []
query_dates = engine.execute(f"SELECT date FROM aqi_2020 WHERE state = '{state}' AND county = '{county}'")
for date in query_dates:
    dates.append(date[0])

aqi_2020 = []
query_api_2020 = engine.execute(f"SELECT aqi FROM aqi_2020 WHERE state = '{state}' AND county = '{county}'")
for api in query_api_2020:
    aqi_2020.append(api[0])

aqi_5y = []
query_api_5y = engine.execute(f"SELECT five_year_avg FROM aqi_2020 WHERE state = '{state}' AND county = '{county}'")
for api in query_api_5y:
    aqi_5y.append(api[0])


aqi_data = {
        "date": dates,
        "aqi_2020": aqi_2020,
        "avg_5y": aqi_5y
}




# create route that renders index.html template
@app.route("/")
def home():
    # return jsonify(all_states)
    return render_template('index.html', state_list=all_states, county_list=all_counties)

@app.route("/county")
def county_data():
    return jsonify(aqi_data)



# # Query the database and send the jsonified results
# @app.route("/send", methods=["GET", "POST"])
# def send():
#     if request.method == "POST":
#         name = request.form["petName"]
#         lat = request.form["petLat"]
#         lon = request.form["petLon"]

#         pet = Pet(name=name, lat=lat, lon=lon)
#         db.session.add(pet)
#         db.session.commit()
#         return redirect("/", code=302)

#     return render_template("form.html")


# @app.route("/api/aqi")
# def aqi():
#     results = db.session.query(Pet.name, Pet.lat, Pet.lon).all()

#     hover_text = [result[0] for result in results]
#     lat = [result[1] for result in results]
#     lon = [result[2] for result in results]

#     pet_data = [{
#         "type": "scattergeo",
#         "locationmode": "USA-states",
#         "lat": lat,
#         "lon": lon,
#         "text": hover_text,
#         "hoverinfo": "text",
#         "marker": {
#             "size": 50,
#             "line": {
#                 "color": "rgb(8,8,8)",
#                 "width": 1
#             },
#         }
#     }]

#     return jsonify(pet_data)


if __name__ == "__main__":
    app.run(debug=True)
