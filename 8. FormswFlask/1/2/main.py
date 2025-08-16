from flask import Flask, render_template,session,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import (StringField,BooleanField,DateTimeField,
                    RadioField, SelectField,TextAreaField,
                    SubmitField)

from wtforms.validators import DataRequired

app = Flask(__name__, template_folder=r"C:\Users\Asus\VSCode\Flask\8. FormsWFlask\2")

app.config['SECRET_KEY'] = 'mysectretkey'

class InfoForm(FlaskForm):
    breed = StringField('What breed are you?', validators=[DataRequired()])
    neutered = BooleanField("Have you been neutered?")
    mood = RadioField('Please choose your mood: ',
                        choices=[('mood1','Happy'),('mood2','Excited'),('mood3','Sad')])
    
    food_choice = SelectField('Pick your favorite food: ', 
                              choices=[('chi','Chicken'),('bo','Bone'),('Pe','Pedigree')])
    feedback = TextAreaField('Enter your feedback here...')
    submit = SubmitField('Submit')
    
@app.route('/',methods=['GET','POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food_choice.data
        session['feedback'] = form.feedback.data
        
        return redirect(url_for('thankyou'))
    return render_template('home.html',form = form)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)