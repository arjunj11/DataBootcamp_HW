from flask import Flask,render_template,redirect
from flask_pymongo import PyMongo 


app=Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route('/')
def home(): 

    import missionstomars
    scraped_dict=missionstomars.scrape()


    # Find one record of data from the mongo database
    #mars_data = mongo.db.mars.find()

    # Return template and data
    return render_template("index.html", mrs=scraped_dict)
    


@app.route('/scrape')
def scrapes():     
    # import missionstomars
    # scraped_dict=missionstomars.scrape()

    # Update the Mongo database using update and upsert=True
    #mongo.db.mars.update({}, scraped_dict, upsert=True)

    # Redirect back to home page
    return redirect("/")
    

if __name__ == "__main__":
    app.run(debug=True)