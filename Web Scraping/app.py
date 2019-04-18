# Import Dependencies 
from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
import pymongo
import scrape_mars
import os


# Hidden authetication file
#import config 

# Create an instance of Flask app
app = Flask(__name__)

# Create connection variable
conn = "mongodb://localhost:27017"

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)


# Create route that renders index.html template and finds documents from mongo
@app.route("/")
def home(): 

    # Find data
    mars_db = db.produce.find_one()

    # Return template and data
    return render_template("index.html", mars_db=mars_db)


