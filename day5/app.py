from flask import Flask, render_template, url_for, request
import uuid
#create a flask application instance
app = Flask(__name__)
@app.route('/')
def home():
    #return f'Day5 - Journey of Learning Flask'
    return render_template('index.html')
#Name = ****, Email = *****
#GET - Fetching the data from db
#POST - Store the data in db, form
#PUT - Update the data (Entire row)
#DELETE - Delete the data(Entire row)
#PATCH - Update a specific column in a row

@app.route('/getData', methods = ['GET'])
def getData():
    name = request.args.get('name')
    email = request.args.get('email')
    return f'Name: {name} Email id: {email}'

@app.route('/getDataFromPOST', methods = ['POST'])
def getDataFromPOST():
    data = request.get_json()
    name = data['name']
    email = data['email']
    return f'Name: {name}, Email id: {email}'
    
@app.route('/postData', methods = ['POST'])
def postData():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    if name is None or len(name) < 5:
        return render_template('index.html',err = "Invalid name")
    if email is None :
            return render_template('index.html',err = "Invalid email")
    if password is None or len(password) < 4:
            return render_template('index.html',err = "Invalid Password")
    return render_template('index.html', msg = "Successful")
        
@app.route("/updateData/<email>", methods = ['PUT'])
def updateData(email):
    data = request.get_json()
    email1 = data['email']
    print(email1)
    #DATABASE LOGIC for PUT
    return f"Data is Updated Successfully for {email}"

@app.route('/deleteData/<email>', methods = ['DELETE'])
def deleteData(email):
    #Database logic for DELETE
    return f'Data is deleted successfully for {email}'

@app.route('/register', methods = ['GET', 'POST'])
def register():
    #here we will mention our condition it can be
    #Either GET or POST
    if request.method == "GET":
        name = request.args.get('name')
        email = request.args.get('email')
        phn = request.args.get('phn')
    if request.method == "POST":
        data = request.get_json()
        #In POST method we will store the data in JSON
        name = data['name']
        email = data['email']
        phn = data['phn']
    return f'The name is {name}, Email: {email}, Phn No. {phn}'
if __name__ == '__main__':
    app.run(host = '0.0.0.0',
            port = 5001,
            debug = True)