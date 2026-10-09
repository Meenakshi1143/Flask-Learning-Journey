from flask import Flask
#Create a Flask applictaion instance 
app = Flask(__name__)
#__name__ is saying it is a flask object

#Now we will start defining the routes
@app.route('/')
def home():
    """Default home page"""
    return "Hello, Good Morning"
@app.route('/meee')
def details():
    """Details about Meee"""
    return "I'm are from........."
@app.route('/location')
def loc():
    """Loaction of mee"""
    return "Visakhapatnam"
@app.route('/edu')
def edu():
    """Education Details"""
    return "Trainee at codegnan "
if __name__ ==  "__main__":
    #app.run()
    app.run(host='0.0.0.0',
            port=5000, debug = True)