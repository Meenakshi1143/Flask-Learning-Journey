from config import Config
import mysql.connector as sql
import random
import smtplib
from email.message import EmailMessage
from flask import Flask,render_template,redirect,url_for,request,session
import bcrypt


app = Flask(__name__)

app.secret_key = "Maggie"
DBConfig = Config()

from_email = DBConfig.from_email 
email_app_password = DBConfig.email_app_password
otp = 0

def generateHash(text):
    btext = text.encode('utf-8')
    cipher_text = bcrypt.hashpw(btext,bcrypt.gensalt(5))
    return cipher_text.decode('utf-8')
    #print(text[0],btext[0])
    #print(type(btext))
    #bcrypt.hashpw(btext)
generateHash("maggi")


#we will make connection with DB
def getConnectionWithDB():
    db_host = DBConfig.db_host
    db_port = DBConfig.db_port
    db_user = DBConfig.db_user
    db_password = DBConfig.db_password
    db_name = DBConfig.db_name
    try:
        connection = sql.connect(
            host = db_host,
            port = db_port,
            user = db_user,
            password = db_password,
            database = db_name
        )
        return connection
    except:
        return"Connection failed"
#Inserting data into tables
def insertRecords(user_data):
    """Inserting user records"""
    name = user_data['name']
    email = user_data['email']
    password_hash = user_data['password_hash']
    connection = getConnectionWithDB()
    if connection == "Connection failed":
        return False
    else:
        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO users(name,email,password_hash) values(%s,%s,%s)",(name,email,password_hash))
            connection.commit()
            cursor.close()
            connection.close()
            return True
        except:
            print("Data cannot be inserted")
    
#Function to define data

data = {
    'name': 'charan',
    'email': 'cherry@gmail.com',
    'password_hash': '12345'
}
print(insertRecords(data))

#Functions to create to access data
def ReadUsers():
    connection  = getConnectionWithDB()
    if connection == "Connection failed":
        return False
    else:
        cursor = connection.cursor()
        cursor.execute("select * from users")
        data = cursor.fetchall()
        records = []
        for record in data:
            temp = {}
            temp['id'] = record[0]
            temp['name'] = record[1]
            temp['email'] = record[2]
            temp['password_hash'] = record[3]
            temp['is_verified'] = record[4]
            temp['created_at'] = record[5]
            
            records.append(temp)
            cursor.close()
            connection.close()
        return records

all_users = ReadUsers()
if all_users:
    for u in all_users:
        print(u)
def ReadUserRecordByEmail(user_data):
    email = user_data['email']
    connection = getConnectionWithDB()
    if connection == "Connection failed":
        return False
    else:
        try:
            cursor = connection.cursor()
            cursor.execute("select * from users where email = %s",(email,))
            data = cursor.fetchone()
            #print(data)
            record = {
                        'id':data[0],
                        'name':data[1],
                        'email':data[2],
                        'password_hash': data[3],
                        'is_verified':data[4],
                        'created_at': data[5]
                    }
            return record
        except:
            cursor.close()
            connection.close()
            return "No Record"
        
def ReadUserRecordById(user_data):
    user_id = user_data['id']

    connection = getConnectionWithDB()

    if connection == "Connection failed":
        return False

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        data = cursor.fetchone()

        if data is None:
            return "No Record"

        record = {
            'id': data[0],
            'name': data[1],
            'email': data[2],
            'password_hash': data[3],
            'is_verified': data[4],
            'created_at': data[5]
        }

        return record

    except Exception as e:
        print(e)
        return "No Record"

    finally:
        cursor.close()
        connection.close()



def updateVerifiedByIdorEmail(user_data):
    try:
            id = user_data['id']
            query_filter = 'id'
    except:
            email = user_data['email'] 
            query_filter = "email" 
    new_IS_VERIFIED=user_data['new_IS_VERIFIED']
    connection = getConnectionWithDB()
    if connection == "Connection failed":
            return False   
    else:
            cursor = connection.cursor()
            if query_filter == "id":
               query = "UPDATE users SET IS_VERIFIED = %s WHERE id = %s"
               values = (new_IS_VERIFIED,id)
            elif query_filter =="email":
                query = "UPDATE users SET IS_VERIFIED = %s WHERE email = %s"
                values = (new_IS_VERIFIED,email)
            cursor.execute(query,values) 
            connection.commit()
            cursor.close()
            connection.close()
            return True   

def generateOTP():
    otp = random.randint(1000,9999)
    return otp

def sendOTPviaemail(to_email,otp):
    message = EmailMessage()
    message['Subject'] = "OTP Notification"
    message['From'] = from_email
    message['To'] = to_email
    message.set_content(
        f"Your OTP is {otp}"
    )
    with smtplib.SMTP("smtp.gmail.com",587) as server:
        server.starttls()
        server.login(from_email,email_app_password)
        server.send_message(message)
    return True


def validateData(user_data):

    errors = []

    name = user_data['name'].strip()
    email = user_data['email'].strip()
    password = user_data['password']
    confirm_password = user_data['confirm_password']

    if len(name) < 3:
        errors.append("Name must contain at least 3 characters")

    if not email or '@' not in email or '.' not in email:
        errors.append("Enter a valid email address")

    if len(password) < 8:
        errors.append("Password must contain at least 8 characters")

    if password != confirm_password:
        errors.append("Passwords do not match")

    return errors

def verifyDuplicateEmail(user_data):
    #email = user_data['email']
    is_duplicate = ReadUserRecordByEmail(user_data)
    if is_duplicate == False:    #No duplicate
                #if there is no account
                #convert password to hast value
                #otp = generateOTP()
                session['otp'] = generateOTP()
                password_hash = generateHash(user_data['password'])
                name = user_data['name']
                email = user_data['email']
                status = insertRecords(
                    {
                        'name':name,
                        'email':email,
                        'password_hash':password_hash
                    }
                )
                if status == True:
                    session['username'] = email
                    session['OTP'] = otp
                    sendOTPviaemail(email,otp)
                    return redirect('/verify')
                    #return render_template('register.html', res = "Registration Successfully COmpleted")
                else:
                    return render_template('register.html',err="Regestraton Failed")
    else:     #duplicate is present
        return render_template('register.html')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register',methods=['GET','POST'])
def register():
    global otp
    if (request.method =="GET"):
        return render_template('register.html')
    elif (request.method=="POST"):
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password  = request.form['confirm_password']
        user_data = {
            "name":name,
            "email":email,
            "password":password,
            "confirm_password":confirm_password
        }
        errors = validateData(user_data)
        if len(errors)>0:
            return render_template('register.html',errors=errors)
        else:
            is_duplicate = verifyDuplicateEmail(user_data)
            if is_duplicate == False:
                pass
            else:
                return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == "GET":
        return render_template('login.html')

    elif request.method == "POST":

        email = request.form['email']
        password = request.form['password']

        user_data = {
            'email': email
        }

        user = ReadUserRecordByEmail(user_data)

        if user == "No Record" or user is False:
            return render_template(
                'login.html',
                error="Invalid email or password"
            )

        if user['password_hash'] == password:
            return redirect(url_for('dashboard'))

        return render_template(
            'login.html',
            error="Invalid email or password"
        )

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/verify',methods = ['GET','POST'])
def verify():
    global otp
    if request.method == 'GET':
        return render_template('verify.html')
    elif request.method == "POST":
        OTP = request.form['OTP']
        OTP = int(OTP)
        if OTP == otp:
            is_verify = True
            updateVerifiedByIdorEmail

if (__name__ == "__main__"):
    app.run(host="0.0.0.0",
            port = 5003,
            debug=True)
'''
User-->register.html-->Registration form-->Post-->Python-->collecting Data-->Validating-->Verifying-->Password to password hash-->MySQL Table
html <=> python <=> MySql 
@app.route('register',methods =['GET','POST'])
def register():
    if request.method == "GET":
        renderHTMLPasgr()
    elif request.method == "POST":
        collectUsedata()
        validateUserData()
        dispalyErrors()
        status = verifyAccountExists()
        if status:
            insertRecords()
        else:
            displayErrorMessage()
'''