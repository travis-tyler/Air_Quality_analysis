# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################


# Import dependencies
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('postgresql://postgres:thehawk-2002@localhost:5432/avg_aqi', '') 
# or "sqlite:///db.sqlite"

# Remove tracking modifications
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# Create engine
# Note: User will need to supply their own PostgreSQL password under variable below
user = 'postgres'
host = 'localhost'
password = 'thehawk-2002'
port = '5432'
db = 'avg_aqi'
uri = f'postgresql://{user}:{password}@{host}:{port}/{db}'

engine = create_engine(uri)


county = 'Baldwin'

sql = engine.execute(f"SELECT date, aqi, five_year_avg FROM aqi_2020 WHERE county = '{county}' LIMIT 10")

results = []
for x in sql:
    results.append(list(x))

all_states = []
states = engine.execute(f"SELECT DISTINCT state FROM aqi_2020")
for s in states:
    all_states.append(s[0])

all_counties = []
counties = engine.execute(f"SELECT DISTINCT county FROM aqi_2020 ORDER BY county")
for c in counties:
    all_counties.append(c[0])




# create route that renders index.html template
@app.route("/")
def home():
    # return jsonify(all_states)
    return render_template('index.html', list=all_counties)




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
