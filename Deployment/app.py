from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd
app = Flask(__name__)
model = pickle.load(open("Turnover_freeze.pckl", "rb"))

@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")

@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Satisfaction level
        #date_dep = 
        satisfaction_level=float(request.form["SL"])
        

        # Last evaluation
        le = request.form["LE"]
        last_evaluation=float(le)

        # Number of project
        npr = request.form["NP"]
        no_of_projects=int(npr)

        # Average monthly hours
        a_m=request.form["AMH"]
        avg_monthly_hr=float(a_m)

        # time spend
        tim_sp=request.form["TSC"]
        time_spend=int(tim_sp)

        #work accident
        w_ac=request.form['WA']
        work_acc=int(w_ac)

        #promotion last 5 years
        pro=request.form['PL5']
        promo=int(pro)

        #Department
        dep=request.form['DEPT']
        department=int(dep)

        #salary
        sal=request.form['SALA']
        salary=int(sal)
        
        prediction=model.predict([[
           satisfaction_level,
           last_evaluation,
           no_of_projects,
           avg_monthly_hr,
           time_spend,
           work_acc,
           promo,
           department,
           salary
        ]])

        output=int(prediction)
        if output==0:
            return render_template('home.html',prediction_text="This employee is going to turnover the job ")
        else:
            return render_template('home.html',prediction_text="This employee is not going to turnover the job ")

    
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
