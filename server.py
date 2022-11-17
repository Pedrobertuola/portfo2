from flask import Flask, render_template, redirect, request
import os
import csv

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')



def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',',  quotechar=';', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/')
    else:
        return 'Somethinbg went wrong. Try again!'




""" @app.route("/favicon.png")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
    'coffee.ico', mimetype="image/coffee.ico")
 """