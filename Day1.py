#pip intsall flask
import flask
from flask import Flask

#We will initialize the flask application instance
app = Flask(__name__)

#Now we will define a route for the url
@app.route('/')
def home():
    return "I'm Meenakshiiiiiiii from batch PFS-VSP-004"
if __name__ == "__main__":
    #run the local development server
    app.run()
