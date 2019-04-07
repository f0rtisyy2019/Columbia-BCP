import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

import datetime as dt


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite",
    connect_args={'check_same_thread': False})

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/2015-10-10<br/>"
        f"/api/v1.0/2015-10-10/2015-10-12"

    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    results = session.query(Measurement.date,Measurement.prcp).all()

    all_prcp = {}
    for date,prcp in results:
        all_prcp[date] = prcp

    return jsonify(all_prcp)


@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station).all()

    all_stations = []
    for r in results:
        station_dict = {}
        station_dict["id"] = r.id
        station_dict["station"] = r.station
        station_dict["name"] = r.name
        station_dict["latitude"] = r.latitude
        station_dict["longitude"] = r.longitude
        station_dict["elevation"] = r.elevation
        all_stations.append(station_dict)

    return jsonify(all_stations)


@app.route("/api/v1.0/tobs")
def tobs():
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    one_year_ago = dt.datetime.strptime(last_date, '%Y-%m-%d') - dt.timedelta(days=365)
    one_year_ago = one_year_ago.strftime("%Y-%m-%d")
    results = session.query(Measurement.date, Measurement.prcp).\
                    filter(Measurement.date >= one_year_ago).\
                    filter(Measurement.date <= last_date).\
                    all()

    all_tobs = []
    for date, tobs in results:
        tobs_dict = {}
        tobs_dict[date] = tobs
        all_tobs.append(tobs_dict)

    return jsonify(all_tobs)

@app.route("/api/v1.0/<start>", defaults={'end': None})
@app.route("/api/v1.0/<start>/<end>")
def temp_by_date(start, end):
    try:
        dt.datetime.strptime(start, '%Y-%m-%d')
        if end is not None:
            dt.datetime.strptime(end, '%Y-%m-%d')
    except:
        return("Error! Date format should be like '2015-12-31' Please try again!")

    if end is None:
        results = session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).\
                    filter(Measurement.date >= start).all()
    else:
        results = session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).\
                    filter(Measurement.date >= start).\
                    filter(Measurement.date <= end).\
                    all()

    all_temps = list(np.ravel(results))
    return jsonify(all_temps)


if __name__ == '__main__':
    app.run(debug=True)
