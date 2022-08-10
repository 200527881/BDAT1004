from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://ykm2478:YadhuKM1@ykm2478.mysql.pythonanywhere-services.com/ykm2478$DataXYZ'
db = SQLAlchemy(app)

class Salaries(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    work_year = db.Column(db.Integer, nullable=False)
    experience_level = db.Column(db.String(2), nullable=False)
    employment_type = db.Column(db.String(2), nullable=False)
    job_title = db.Column(db.String(200), nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    salary_currency = db.Column(db.String(3), nullable=False)
    salary_in_usd = db.Column(db.Integer, nullable=False)
    employee_residence = db.Column(db.String(2), nullable=False)
    remote_ratio = db.Column(db.Integer, nullable=False)
    company_location = db.Column(db.String(2), nullable=False)
    company_size = db.Column(db.String(1), nullable=False)

    #age = db.Column(db.Integer)

    def __repr__(self):
        return '<Task %r>' % self.id
@app.route('/')
def index():
    salaries = Salaries.query.order_by(Salaries.id).all()
    return render_template('index.html', salaries = salaries)
if __name__ == "__main__":
    app.run(debug=True)

