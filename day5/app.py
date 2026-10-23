from flask import Flask,redirect,render_template,url_for,request
app = Flask(__name__)
#GET => Fetching data from db
#pOST => Store data in db,forms
#PUT => Upadate data 
#DELETE => Delets data (a row)
#PATCH => Update a specific row in column
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/getData',methods=['GET'])
def getData():
    name = request.args.get('name')
    mail = request.args.get('mail')
    return f'Name is {name} mail is {mail}'
@app.route('/getpostData',methods=['POST'])
def getpostData():
    data = request.get_json()
    name = data['name']
    mail = data['mail']
    return f'Name is {name} mail is {mail}'
@app.route('/postData',methods =['POST'])
def postData():
    #data = request.get_json()
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    if name is None or len(name)<4:
        return render_template('index.html',err="Invalid Name")
    if email is None:
        return render_template('index.html',err="enter email")
    if password is None or len(password)<4:
        return render_template('index.html',err="Password mush have atleast 4 chars")
    return render_template('index.html',msg="Sucessful")
@app.route('/updateData/<mail>',methods = ['PUT'])
def updateData(mail):
    data = request.get_json()
    mail1 = data['mail']
    print(mail1)
    #database logic for put 
    return f"Data is updated sucessfully for {mail}"
@app.route('/deleteData/<mail>',methods = ['DELETE'])
def deleteData(mail):
    #database logic for delete data
    return f'Data is deleted sucessfully for {mail}'
if __name__ =="__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)