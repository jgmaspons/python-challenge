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

db = client.mars_db

# Create route that renders index.html template and finds documents from mongo
@app.route("/")
def home(): 

    # Find data
    #mars_db = client.db.produce.find_one()

    # Grall all data
    mars_all_data = db.collection.find_one()

    # Return template and data
    return render_template("index.html", mars_all_data=mars_all_data)

#def main()

    

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    mars_data = scrape_mars.scrape_mars_data_news()
    mars_images = scrape_mars.scrape_mars_images()
    mars_weather = scrape_mars.scrape_mars_weather()
    mars_facts = scrape_mars.scrape_mars_facts()
    #mars_hemispheres = scrape_mars.scrape_mars_hemispheres()

   

    mars_all_data = {}
    mars_all_data['news_title'] = mars_data['news_title']
    mars_all_data['results_paragraph'] = mars_data['results_paragraph']
    mars_all_data['feature_image_url'] = mars_images['feature_image_url']
    mars_all_data['mars_weather_result'] = mars_weather['mars_weather_result']
    mars_all_data['mars_facts_table'] = mars_facts['mars_facts_table']
    mars_all_data['mars_hemispheres'] = scrape_mars.scrape_mars_hemispheres()


    db.collection.update({}, mars_all_data, upsert=True)

    print(mars_data)
    print(mars_images)
    print(mars_weather)
    print(mars_facts)
    #print(mars_hemispheres)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, port = 8080)
#    print("blah")
