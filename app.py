/*--------------------------------------------------------------------------------- IMPORTS START */

import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from bson.objectid import ObjectId

/*--------------------------------------------------------------------------------- IMPORTS END */
/*--------------------------------------------------------------------------------- CONNECTIONS START */

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'hungryHerbivore'
app.config['MONGO_URI'] = os.environ.get('MONGO_URL')

mongo = PyMongo(app)

/*--------------------------------------------------------------------------------- CONNECTIONS END */
/*--------------------------------------------------------------------------------- @ROUTE START */

@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())
    
    
@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html', categories=mongo.db.categories.find())
    
@app.route('/submit_recipe', methods=['POST'])
def submit_recipe():
    recipes=mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))
    
@app.route('/modify_recipe/<recipe_id>')
def modify_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template('modifyrecipe.html', recipe=the_recipe)
    
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))
    
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
     'meal_name':request.form.get('meal_name'),
     'difficulty':request.form.get('difficulty'),
     'meal_time':request.form.get('meal_time'),
     'meal_ingredients':request.form.get('meal_ingredients'),
     'meal_requirements':request.form.get('meal_requirements'),
     'meal_method':request.form.get('meal_method'),
     'meal_comment':request.form.get('meal_comment'),
    })
    return redirect(url_for('get_recipes'))
    
@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
  the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
  all_categories = mongo.db.categories.find()
  return render_template('viewrecipe.html', recipe=the_recipe)
  
@app.route('/filter', methods=["POST"])
def filter():
    difficulty = request.form['difficulty-filter']
    result_cursor = mongo.db.recipes.find({"difficulty" : difficulty})
    my_res = ""
    for doc in result_cursor:
        my_res += str(doc)
    return my_res
     

/*--------------------------------------------------------------------------------- @ROUTE END */
/*--------------------------------------------------------------------------------- DEBUG + HEROKU START */
    
if __name__ ==  '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
    
/*--------------------------------------------------------------------------------- DEBUG + HEROKU START */