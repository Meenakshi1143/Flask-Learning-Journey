from flask import Flask, render_template, url_for
import uuid

app = Flask(__name__)


# Default root route
@app.route('/')
def home():
    return render_template('index.html')


# /home route
@app.route('/home')
def home_page():
    return render_template('index.html')


# Subject and Marks
@app.route('/subject/<subject>/<float:marks>')
def subject_marks(subject, marks):
    return f"Subject: {subject}<br>Marks: {marks}"


# Generating UUID
@app.route('/subject/<subject>/uuid')
def subject_uuid(subject):
    unique_id = uuid.uuid4()
    return f"Subject: {subject}<br>UUID: {unique_id}"

@app.route('/uuid')
def subject_iuuid():
    unique_id = uuid.uuid4()
    return f"UUID: {unique_id}"


#About page
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port= 5001, debug=True)