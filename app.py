from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("skill_model.pkl","rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def predict():

    p = int(request.form['python'])
    ps = int(request.form['problem'])
    ce = int(request.form['coding'])

    result = model.predict([[p,ps,ce]])

    if result[0]==0:
        level="Beginner"
    elif result[0]==1:
        level="Intermediate"
    else:
        level="Advanced"

    return render_template("index.html",prediction=level)

if __name__ == "__main__":
    app.run(debug=True)