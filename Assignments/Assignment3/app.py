
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/getdata', methods=['GET'])
def getdata():
    name = request.args.get('name')
    batchno = request.args.get('batchno')

    return jsonify({
        'name': name,
        'batchno': batchno
    })

@app.route('/postdata', methods=['POST'])
def postdata():
    data = request.get_json()

    if not isinstance(data, dict):
        return jsonify({'error': 'Please send a JSON object'}), 400

    name = data.get('name')
    skills = data.get('skills')

    return jsonify({
        'name': name,
        'skills': skills
    })


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port= 5001,debug=True)
