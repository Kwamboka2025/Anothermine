from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate_age():
    if request.method == 'POST':
        dob_str = request.form['dob']
        dob = datetime.strptime(dob_str, '%Y-%m-%d')
        age = (datetime.today() - dob).days // 365
        return f'Your age is: {age} years'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
