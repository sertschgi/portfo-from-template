from flask import Flask, render_template, redirect, url_for, request
import csv
import os.path
app = Flask(__name__)


def write_to_csv(data):
    file_exists = os.path.isfile('./database.csv')
    with open('./database.csv', mode='a', newline='') as fobj:
        fieldnames = ['email','subject','message']

        csv_writer = csv.DictWriter(
            fobj, 
            fieldnames=fieldnames,
            delimiter=',', 
            quotechar='"', 
            quoting=csv.QUOTE_MINIMAL
        )

        if not file_exists:
            csv_writer.writeheader()

        csv_writer.writerow(data)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def make_route(page_name):
    if page_name == 'index.html':
        return redirect(url_for('home'))
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return 'form submitted'
        except:
            return 'jdkfjöllkdjfklöajd :('
    else:
        return 'something went wrong :('