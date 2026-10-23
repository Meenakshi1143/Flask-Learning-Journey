from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def home():
    data = 28
    #creating sudent details
    student_details = [
        {
        "id":1,
        "name":"Meenakshi"
        },
        {
            "id":2,
            "name":"Meghana"
        }
    ]
    return render_template('index.html',d=data,m = student_details)

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)