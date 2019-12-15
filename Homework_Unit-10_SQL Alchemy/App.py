<<<<<<< HEAD
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt
# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
conn=engine.connect()
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)
inspector=inspect(engine)
m=inspector.get_columns('measurement')
s= inspector.get_columns('station')
from flask import Flask,jsonify

app = Flask(__name__)
@app.route("/")
def home():
    session = Session(engine)
    return ("You are amazing - and you can select any route from the below /n precipitation /n stations /n temperature /n start and end date ")

@app.route("/api/v1.0/precipitation")
def prec():
    session = Session(engine)
    dates=[]
    precp=[]
    outputs=session.query(Measurement.date,Measurement.prcp)
    for row in outputs:
        (a,b)=row
        dates.append(a)
        precp.append(b)
    dateprec=dict(zip(dates,precp))
    return jsonify(dateprec)

@app.route("/api/v1.0/stations")
def stn():
    session = Session(engine)
    sttn=[]
    outputa=session.query(Measurement.station).group_by(Measurement.station)
    for row in outputa:
        sttn.append(row)
    return jsonify(sttn)

@app.route("/api/v1.0/tobs")
def temps():
    session = Session(engine)
    temp1=[]
    outputb=session.query(Measurement.tobs).filter(Measurement.date>='2016-08-23')
    for row in outputb:
        temp1.append(row)
    return jsonify(temp1)

@app.route("/api/v1.0/<start>")
def strt(start):
    session = Session(engine)
    return jsonify(session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).all())
            
@app.route("/api/v1.0/<start>/<end>")
def strtend(start,end):
    session = Session(engine)
    return jsonify(session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).all())         
            
if __name__ == "__main__":
=======
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt
# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
conn=engine.connect()
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)
inspector=inspect(engine)
m=inspector.get_columns('measurement')
s= inspector.get_columns('station')
from flask import Flask,jsonify

app = Flask(__name__)
@app.route("/")
def home():
    session = Session(engine)
    return ("You are amazing - and you can select any route from the below /n precipitation /n stations /n temperature /n start and end date ")

@app.route("/api/v1.0/precipitation")
def prec():
    session = Session(engine)
    dates=[]
    precp=[]
    outputs=session.query(Measurement.date,Measurement.prcp)
    for row in outputs:
        (a,b)=row
        dates.append(a)
        precp.append(b)
    dateprec=dict(zip(dates,precp))
    return jsonify(dateprec)

@app.route("/api/v1.0/stations")
def stn():
    session = Session(engine)
    sttn=[]
    outputa=session.query(Measurement.station).group_by(Measurement.station)
    for row in outputa:
        sttn.append(row)
    return jsonify(sttn)

@app.route("/api/v1.0/tobs")
def temps():
    session = Session(engine)
    temp1=[]
    outputb=session.query(Measurement.tobs).filter(Measurement.date>='2016-08-23')
    for row in outputb:
        temp1.append(row)
    return jsonify(temp1)

@app.route("/api/v1.0/<start>")
def strt(start):
    session = Session(engine)
    return jsonify(session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).all())
            
@app.route("/api/v1.0/<start>/<end>")
def strtend(start,end):
    session = Session(engine)
    return jsonify(session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).all())         
            
if __name__ == "__main__":
>>>>>>> 2d40831c094b16f1c4e967bcd66cb0070acf77d0
    app.run(debug=True)