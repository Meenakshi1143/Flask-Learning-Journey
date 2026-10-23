from flask import Flask, render_template, url_for, request

app = Flask(__name__)


# 1. Home page
@app.route('/')
def home():
    return render_template('index.html')


# 2. About page
@app.route('/about')
def about():
    return render_template('about.html')


# 3. GET request to get name and batchno
@app.route('/getData', methods=['GET'])
def getData():
    name = request.args.get('name')
    batchno = request.args.get('batchno')

    return f"Name: {name}, Batch No: {batchno}"


# 4. POST request to fetch name and skills using JSON
@app.route('/postData', methods=['POST'])
def postData():
    data = request.get_json()

    name = data['name']
    skills = data['skills']

    return {
        'name': name,
        'skills': skills
    }


if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True, port=5001)