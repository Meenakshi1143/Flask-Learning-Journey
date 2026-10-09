#Build a Student routing app
#Student default page
#Student id
#Student attendance
#File path
#Student uuid

from flask import Flask
import uuid
app = Flask(__name__)
#We will generate UUID  using python module
@app.route('/')
def student():
    return f'Student Routing Application'
@app.route('/stud_id/<int:id>')
def std_id(id):
    return f'Student Id: {id}'
@app.route('/skills/<s1>/<s2>')
def skills(s1, s2):
    return f'Student Skills: {s1}, {s2}'
@app.route('/attendance/<float:attendance>')

def std_attendance(attendance):
    return f'Attendance Details of Student: {attendance}'
@app.route('/path/<path:File_name>')
def file_path(File_name):
    return f'Student file path: {File_name}'
@app.route('/std_uuid')
def stud_uuid(std_uuid):
    id = uuid.uuid4().hex
    return f'UUID of Student: {std_uuid}'

if __name__ == "__main__":
    app.run(host = '0.0.0.0',
            port = 5000, debug = True)
    

