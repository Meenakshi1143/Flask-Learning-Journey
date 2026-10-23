from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def students():

    student_list = [
        {'id': 1, 'name': 'Meena', 'percentage': 85.5},
        {'id': 2, 'name': 'Meghana', 'percentage': 72.0},
        {'id': 3, 'name': 'Priya', 'percentage': 91.0},
        {'id': 4, 'name': 'Dedeepya', 'percentage': 65.0},
        {'id': 5, 'name': 'Ankitha', 'percentage': 48.0},
        {'id': 6, 'name': 'Rahul', 'percentage': 35.0},
        {'id': 7, 'name': 'Anu', 'percentage': 80.5},
        {'id': 8, 'name': 'Sravanthi', 'percentage': 59.0},
        {'id': 9, 'name': 'Divya', 'percentage': 76.5},
        {'id': 10, 'name': 'Manoj', 'percentage': 40.0}
    ]

    for s in student_list:
        if s['percentage'] > 80:
            s['grade'] = 'A'
        elif s['percentage'] > 60:
            s['grade'] = 'B'
        elif s['percentage'] > 40:
            s['grade'] = 'C'
        else:
            s['grade'] = 'D'

    return render_template('students.html', students=student_list)


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port= 5001,debug=True)