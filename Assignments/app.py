from flask import Flask, render_template, url_for
import uuid

app = Flask(__name__)


# 1. Default root route
@app.route('/')
def home():
    return render_template('index.html')


# 2. /home route
@app.route('/home')
def home_page():
    return render_template('index.html')


# 3. Dynamic route for subject and marks
@app.route('/subject/<subject>/<float:marks>')
def subject_marks(subject, marks):
    return f"Subject: {subject}<br>Marks: {marks}"


# 4. Dynamic route for generating UUID
@app.route('/subject/<subject>/uuid')
def subject_uuid(subject):
    unique_id = uuid.uuid4()
    return f"Subject: {subject}<br>UUID: {unique_id}"


# 5. About page
@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(host = '0.0.0.0',
            port= 5001,
            debug=True)