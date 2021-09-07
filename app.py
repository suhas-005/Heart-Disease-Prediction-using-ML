from flask import Flask, request, url_for, redirect, render_template
import joblib
import numpy as np

app = Flask(__name__)

app.config["SECRET_KEY"] = 'abd3e6fb8a9854dd92a30cfc6dab510d'
clf = joblib.load(r'C:\Users\User\Desktop\ML Web\heart_rf_model.sav')


@app.route('/')
def hello_world():
    return render_template("Home.html")


@app.route('/about')
def about():
    return render_template("aboutus.html", title='About Us')


@app.route('/project')
def project():
    return render_template("Project.html", title='Check Heart health')


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    final = [np.array(int_features)]
    print(int_features)
    print(final)
    prediction = clf.predict_proba(final)
    print(prediction)
    output = '{0:.{1}f}'.format(prediction[0][1], 2)

    if output > str(0.5):
        return render_template('Project.html', pred='Your Heart is in Danger.\nProbability of heart disease is {}'.format(output), res="Do consult a doctor!!")
    else:
        return render_template('Project.html', pred='Your Heart is safe.\n Probability of heart disease is {}'.format(output), res="Eat safe and be healthy..")


if __name__ == '__main__':
    app.run(debug=True)
