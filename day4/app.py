from flask import Flask,render_template, url_for,request, redirect
import uuid
app = Flask(__name__)
#We will generate UUID  using python module
@app.route('/')
def home():
    #return "Welcome to Day-4 learning Class"
    return redirect(url_for('aboutPage'))
@app.route('/generate')
def generate():
    id = uuid.uuid4().hex
    print(id)
    return f'The generated id is: {id}'
@app.route('/index')
def indexPage():
    return render_template('index.html')
@app.route('/about')
def aboutPage():
    return render_template('about.html')
if __name__ == "__main__":
    app.run(host = '0.0.0.0',
            port = 5000, debug = True)
