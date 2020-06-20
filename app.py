import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from os import path
from bson.objectid import ObjectId
from bson.json_util import dumps

if path.exists("env.py"):
  import env 


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'solo_traveller_handbook'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

@app.route('/')
@app.route('/home')
def index():


    return render_template("pages/index.html", tasks=mongo.db.things_to_do.find())

@app.route('/find')

def find():

    return render_template("pages/find.html", categories=mongo.db.things_to_do.find())
    



@app.route('/find_activity', methods=['POST'])

def find_activity():

    #category_to_search = request.form.get('category')
    #city_to_search = request.form.get('city')
    #name_to_search = request.form.get('name')
    #matching_activities = mongo.db.things_to_do.find({'category': category_to_search, 'name': name_to_search, 'city': city_to_search})
    #print (matching_activities)
    my_name= "Nafeesah2"

    #search_dict = { 'city': request.form.get('city'), 'category': request.form.get('category') }

    #if request.form.get('name') != "":
    #    search_dict['name'] = request.form.get('name')
    #matching_activities = mongo.db.things_to_do.find()
    one_activity = list(mongo.db.things_to_do.find({'city': request.form.get('city'), 'category': request.form.get('category')}))

    
    print(my_name)
    print(one_activity)
    
    return render_template("pages/findactivity.html", activity=one_activity)










    
@app.route('/addactivity')

def add():
    return render_template("pages/addactivity.html", categories=mongo.db.things_to_do.find())

@app.route('/insert_activity', methods=['POST'])

def insert_activity():

    things_to_do = mongo.db.things_to_do
    things_to_do.insert_one(request.form.to_dict())
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)