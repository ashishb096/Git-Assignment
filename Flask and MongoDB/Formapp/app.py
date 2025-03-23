from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired
from dotenv import load_dotenv
import os
from pymongo import MongoClient

#Load environment variables from .env file

load_dotenv()

app = Flask(__name__)

#Configuring secret key for flash messages

app.config['SECRET_KEY'] = 'mysecretkey'

#Configuring MongoDB URI

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client.get_database('db')
users_collection = db.get_collection('users')

#Define a Flask-WTF form
class DataForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])

#Route to display the form
@app.route('/', methods=['GET', 'POST'])
def index():
    form = DataForm()

    if form.validate_on_submit():
        try:
            #Inserting data into MongoDB
            users_collection.insert_one({
                'name': form.name.data,
                'age': form.age.data
            })
            #If successful, redirect tp success page
            return redirect(url_for('success'))

        except Exception as e:
            #If there's an error, display error on the same page
            flash(f"An error occurred: {str(e)}", 'error')
            return redirect(url_for('index'))

    return render_template('index.html', form=form)


#Route to display the success message
@app.route('/success', methods=['GET', 'POST'])
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)
