import os
import joblib
from flask import Flask, render_template, session, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import BooleanField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

# Load column names
column_names = joblib.load('./static/column_names.pkl')
# Load model
model = joblib.load('./static/final_model.pkl')


class InfoForm(FlaskForm):
    sqft = IntegerField("Please enter the square feet of the apartment", validators=[DataRequired()])
    beds = SelectField('Select the number of beds:',
                       choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    baths = SelectField('Select the number of bathrooms:',
                        choices=[('1', '1'), ('2', '2'), ('2.5', '2.5'), ('3', '3'), ('3.5', '3.5'),
                                 ('4', '4'), ('4.5', '4.5'), ('5', '5')])
    electric = BooleanField('Does the apartment have an electric vehicle charging station? (CHECK BOX IF YES)')
    furnished = BooleanField('Is the apartment furnished? (CHECK BOX IF YES)')
    # laundry will need to be broken up into two variables
    laundry = SelectField('Select laundry type:',
                          choices=[('w/d in unit', 'w/d in unit'), ('laundry on site', 'laundry on site'),
                                   ('no laundry options', 'no laundry options')])
    # Garage types will need to be broken up
    garage = SelectField('Select Parking option:',
                         choices=[('attached garage', 'attached garage'), ('detached garage', 'detached garage'),
                                  ('off-street parking', 'off-street parking'),
                                  ('no parking information', 'no parking information')])
    submit = SubmitField("Submit to get prediction")


def create_predictions(sqft, beds, baths, electric, furnished, laundry, garage):
    electric = int(electric)
    furnished = int(furnished)

    laundry_in_unit = 0
    laundry_on_site = 0

    attached_garage = 0
    detached_garage = 0
    off_street_parking = 0

    # Compare laundry and assign
    if laundry == 'w/d in unit':
        laundry_in_unit = 1
        laundry_on_site = 0
    elif laundry == 'laundry on site':
        laundry_in_unit = 0
        laundry_on_site = 1
    else:
        laundry_in_unit = 0
        laundry_on_site = 0

    # Check garage type
    if garage == 'attached garage':
        attached_garage = 1
        detached_garage = 0
        off_street_parking = 0
    elif garage == 'detached garage':
        attached_garage = 0
        detached_garage = 1
        off_street_parking = 0
    elif garage == 'off-street parking':
        attached_garage = 0
        detached_garage = 0
        off_street_parking = 1
    else:
        attached_garage = 0
        detached_garage = 0
        off_street_parking = 0

    prediction = model.predict([[sqft, beds, baths, electric, furnished, laundry_on_site, laundry_in_unit,
                                 attached_garage, detached_garage, off_street_parking]])
    return prediction[0]


@app.route('/', methods=['GET', 'POST'])
def index():
    form = InfoForm()

    if form.validate_on_submit():
        sqft = form.sqft.data
        beds = form.beds.data
        baths = form.baths.data
        electric = form.electric.data
        furnished = form.furnished.data
        laundry = form.laundry.data
        garage = form.garage.data

        predicted_value = create_predictions(sqft, beds, baths, electric, furnished, laundry, garage)
        print(f"The predicted value is {predicted_value}")
        session['sqft'] = sqft
        session['beds'] = beds
        session['baths'] = baths
        session['electric'] = electric
        session['furnished'] = furnished
        session['laundry'] = laundry
        session['garage'] = garage
        session['prediction'] = round(predicted_value, 2)
        return redirect(url_for('prediction'))
    if form.sqft.errors:
        flash('Please make sure to select every choice, square feet must be an integer value')

    return render_template('home.html', form=form)


@app.route('/prediction')
def prediction():
    return render_template('prediction.html')


if __name__ == '__main__':
    app.run(debug=True)
