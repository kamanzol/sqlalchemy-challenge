#Dependencies import section

import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import create_engine, inspect
from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)


# Flask setup Section Starts Here


app = Flask(__name__)

@app.route("/")
def welcome():
    return (
        f"Welcome to Katie's Flask HW for SQL Alchemy Week 10.<br/>"
        f"<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/startend<br/>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    results = session.query(Measurement.date, Measurement.prcp).all()
    session.close()

    all_results = []
    for date, prcp in results:
        result_dict = {}
        result_dict["date"] = date
        result_dict["prcp"] = prcp
        all_results.append(result_dict)

    return jsonify(all_results)
#confused why the keys date and prcp won't show up on my site?  But it does for stations.
#because date is an index and not it's own column?

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    results = session.query(Station.id, Station.station).all()
    session.close()

    all_results = []
    for id, station in results:
        result_dict = {}
        result_dict["id"] = id
        result_dict["station"] = station
        all_results.append(result_dict)

    return jsonify(all_results)



@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    results = session.query(Measurement.date, Measurement.tobs).\
        group_by(Measurement.date).\
        filter(Measurement.date <= '2017-08-23').\
        filter(Measurement.date >= '2016-08-24').all()
    session.close()

    tobs_list = list(results)
    return jsonify(tobs_list)


@app.route("/api/v1.0/start")
def start():
    f"text 2"


@app.route("/api/v1.0/startend")
def startend():
    f"text 3"





if __name__ == "__main__":
    app.run(debug=True)