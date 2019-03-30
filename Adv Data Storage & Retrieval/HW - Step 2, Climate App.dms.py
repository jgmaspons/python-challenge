
#################################################
# 1 Import Flask
#################################################

import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# 2 Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the measurement table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)


#################################################
# 3 Flask Setup
#################################################

app = Flask(__name__)


#################################################
# 4 Flask Routes
#################################################

@app.route("/")
def home():
    return (
        f"Welcome to the API Home Page for Climate App. The routes available are:<br/><br/>" 
        f"/api/v1.0/precipitation<br/>"  
        f"/api/v1.0/stations<br/>"     
        f"/api/v1.0/tobs<br/>"  
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end"
    )


#############################################################
# 5 Return JSON representation of precipitation dictionary
#############################################################


@app.route("/api/v1.0/precipitation")
def precipitation():
    
    # Query all precipitation results
    precipitation_results = session.query(Measurement, Measurement.station, Measurement.date, Measurement.prcp).order_by(Measurement.date).all()
    
   # Create a dictionary from the row data and append to a list of precipitation results
    all_precipitation = []
    for precipitation in precipitation_results:
        measurement_dict = {}
        measurement_dict["station"] = precipitation[1]
        measurement_dict["date"] = precipitation[2]
        measurement_dict["precipitation"] = precipitation[3]
        all_precipitation.append(measurement_dict)

    return jsonify(all_precipitation)


#################################################
# 6 Return JSON list of stations
#################################################

all_stations = [
    
    {"USC00519397": "WAIKIKI 717.2, HI US"},
    {"USC00513117": "KANEOHE 838.1, HI US"},
    {"USC00514830": "KUALOA RANCH HEADQUARTERS 886.9, HI US"},
    {"USC00517948": "PEARL CITY, HI US"},
    {"USC00518838": "UPPER WAHIAWA 874.3, HI US"},
    {"USC00519523": "WAIMANALO EXPERIMENTAL FARM, HI US"}, 
    {"USC00519281": "WAIHEE 837.5, HI US"},
    {"USC00511918": "HONOLULU OBSERVATORY 702.2, HI US"},
    {"USC00516128": "MANOA LYON ARBO 785.2, HI US"}

 ]

@app.route("/api/v1.0/stations")
def stations():
   #return jsonify(stations)
    return jsonify(all_stations)
    
   # Query all weather stations
   #weather_stations = session.query(Station, Station.station, Station.name).all()
    
   # Create a dictionary from the row data and append to a list of station results
   #stations = []
   #for station in weather_stations:
        #station_dict = {}
        #station_dict["station"] = station[1]
        #station_dict["name"] = station[2]
        #stations.append(station_dict)
    
   #return jsonify(stations)


##############################################################
# 7 Return JSON representation of temperature dictionary
##############################################################

@app.route("/api/v1.0/tobs")
def tobs():


# Query temperature results from previous year
    date = dt.datetime(2016, 8, 22)
     
    temp_last_yr = session.query(Measurement, Measurement.station, Measurement.date, Measurement.tobs).filter(Measurement.date > '2016-08-22').order_by(Measurement.date).all()


# Create a dictionary from the row data and append to a list of temperature results
    temp_results_list = []
    for temperature in temp_last_yr:
        temperature_dict = {}
        temperature_dict["station"] = temperature[1]
        temperature_dict["date"] = temperature[2]
        temperature_dict["temperature"] = temperature[3]
        temp_results_list.append(temperature_dict)

    return jsonify(temp_results_list)
    
      
##############################################################
# 8 Process JSON list output based on start date
##############################################################

@app.route("/api/v1.0/<start_date>")
def startdate(start_date):
    session = Session(engine)

    temp_inquiry_results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start_date).all()
                                                                                                                                  
    (temp_min, temp_avg, temp_max) = temp_inquiry_results[0]
                                                                                                                                  
    temp_start_output = {}
    temp_start_output["Initial date selected"] = start_date                                     
    temp_start_output["Minimum temperature"] = temp_min
    temp_start_output["Average temperature"] = temp_avg
    temp_start_output["Maximum temperature"] = temp_max
  
    return jsonify(temp_start_output)                                     
                  
    
##############################################################
# 9. Process JSON list output based on start and end date
##############################################################

@app.route("/api/v1.0/<start_date>/<end_date>")
def data_range(start_date, end_date):
    session = Session(engine)

    temp_inquiry_results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

    (temp_min, temp_avg, temp_max) = temp_inquiry_results[0]
                                                                                                                                  
    temp_range_output = {}
    temp_range_output["Initial date selected"] = start_date   
    temp_range_output["End date selected"] = end_date
    temp_range_output["Minimum temperature"] = temp_min
    temp_range_output["Average temperature"] = temp_avg
    temp_range_output["Maximum temperature"] = temp_max
  
    return jsonify(temp_range_output)


if __name__ == "__main__":
    app.run(debug=True)


