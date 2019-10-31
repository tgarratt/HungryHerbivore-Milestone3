import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'hungryHerbivore'
app.config['MONGO_URI'] = os.environ.get('MONGO_URL')

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())
    
    
@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html')
    
@app.route('/submit_recipe', methods=['POST'])
def submit_recipe():
    recipes=mongo.db.recipes
    recipes.insert_one(request.form.to.dict())
    return redirect(url_for('get_recipes'))
    
    
if __name__ ==  '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
    
