
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def signup():
    return render_template('signup.html')


@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    email = request.form.get('email')
    address = request.form.get('address')
    password = request.form.get('password')

    return render_template(
        'success.html',
        username=username,
        email=email,
        address=address
    )


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port= 5001,debug=True)
