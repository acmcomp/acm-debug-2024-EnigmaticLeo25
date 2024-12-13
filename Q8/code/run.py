from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_SECRET = os.getenv('API_KEY')

app = Flask(
    __name__,
    static_folder='static',
    template_folder='templates'
)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    job_title = db.Column(db.String(120))
    feedback_text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Feedback {self.username}>"


with app.app_context():
    db.create_all()
@app.route('/')
def home():
    category = 'inspirational' # Choose one of the categories from the API docs
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': API_SECRET})
    if response.status_code == requests.codes.ok:
        resp = response.json()
        quote_of_the_day = resp[0]['quote']
    else:
        print("Error:", response.status_code, response.text)
        quote_of_the_day = "Loading.."

    with app.app_context():
        feedbacks = Feedback.query.all()

    return render_template(
        'home.html',
        feedbacks=[{'USERNAME': f.username, 'JOB_TITLE': f.job_title, 'FEEDBACK': f.feedback_text} for f in feedbacks],
        daily_quote=quote_of_the_day
    )

@app.route('/submit_feedback', methods=['GET','POST'])
def submit_feedback():
    if request.method == 'POST':
        username = request.form.get('username')
        job_title = request.form.get('job_title')
        feedback_text = request.form.get('feedback')
        
        new_feedback = Feedback(username=username, job_title=job_title, feedback_text=feedback_text)
        db.session.add(new_feedback)
        db.session.commit()
        with app.app_context():
            feedbacks = Feedback.query.all()
        return render_template('home.html',feedbacks=[{'USERNAME': f.username, 'JOB_TITLE': f.job_title, 'FEEDBACK': f.feedback_text} for f in feedbacks])

if __name__ == '__main__':
    app.run(debug=True, port=5001)