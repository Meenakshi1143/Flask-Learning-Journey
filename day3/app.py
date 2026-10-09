from flask import Flask
app = Flask(__name__)
#Multiple routes to view one function
@app.route('/')
@app.route('/home/')
def home():
    return f'Welcome to Day-3 Learning about Static and Dynamic routes'
@app.route('/profile/')
def details():
    return f'Batch: PFS-VSP-004'
#Static route - /name/meena
#Dynamic routing - /name/<name>
@app.route('/name/meena')
def data():
    return f'Welcome Meenaa..'
@app.route('/name/<name>')
def std_data(name):
    return f'Hello {name}'
#now we want to create related too course names 
@app.route('/courses/<course_name>')
def courses(course_name):
    return f'This Course is <b>{course_name}</b>'
#Converts - int, str, float, path, uuid
#Integer Converters
@app.route('/student/<string:student_id>')
def studentid(student_id):
    return f'<u><h1>Student id:</h1></u> {student_id}'
@app.route('/students/<float:student_marks>')
def studentMarks(student_marks):
    return f'<b>Student marks:</b> {student_marks}'
#Path converters
@app.route('/path/<path:file_name>')
def filepath(file_name):
    return f'The file path {file_name}'
#UUID Converter
@app.route('/student_id/<uuid:std_id>')
def student_id(std_id):
    return f'UUID: {std_id}'
    
if __name__ == "__main__":
    app.run(host = '0.0.0.0',
            port = 5001, debug = True
        )