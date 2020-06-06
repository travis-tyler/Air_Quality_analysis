from sqlalchemy import func
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#################################################
# Database Setup
#################################################

app.config['SQLALCHEMY_DATABASE_URI'] = "path_to/postgresdb"
db = SQLAlchemy(app)

@app.route("/")
def home():
    return render_template("index.html")

# Delete this if not needed
@app.before_first_request
def setup():
    
    # Recreate database each time for demo
    db.drop_all()
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)