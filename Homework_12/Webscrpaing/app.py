from flask import Flask,render_template,redirect
from flask_pymongo import PyMongo 
app=Flask(__name__)
import pymongo

# Use PyMongo to establish Mongo connection
conn='mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db= client.mars_db
collection = db.mars

@app.route('/')
def home(): 
    #Find one record of data from the mongo database
    
    result=db.mars.find()
    for row in result:
        mars_dict=row
    return render_template("index.html", mars=mars_dict)
    
@app.route('/scrape')
def scrapes():     
    import missionstomars
    scraped_dict=missionstomars.scrape()

    # Update the Mongo database using update and upsert=True
    collection.update({},scraped_dict, upsert=True)

    # Redirect back to home page
    return redirect("/")
    

if __name__ == "__main__":
    app.run(debug=True)