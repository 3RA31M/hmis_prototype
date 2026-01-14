from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(
    __name__,
    template_folder='../templates',  # go up one level, then into templates
    static_folder='../static'        # same for static
)
# Create the database if it doesn't exist
def init_db():
    conn = sqlite3.connect('pat_info.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS patients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    prefix TEXT,
                    name TEXT,
                    phone TEXT,
                    email TEXT,
                    gender TEXT,
                    age INTEGER,
                    dob TEXT,
                    address TEXT,
                    marital_status TEXT,
                    spouse TEXT,
                    doctor TEXT
                    appointment_time TEXT
                )''')
    conn.commit()
    conn.close()

init_db()  # make sure the table exists

@app.route('/', methods=['GET'])
def form():
    return render_template('appointment.html')

@app.route('/submit', methods=['POST'])
def submit():
    prefix = request.form.get('prefiix')
    name = request.form.get('name')
    phone = request.form.get('Phone NO')
    email = request.form.get('Email')
    gender = request.form.get('gender')
    age = request.form.get('age')
    dob = request.form.get('date')
    address = request.form.get('address')
    marital_status = request.form.get('maritial-status')
    spouse = request.form.get('spouse')
    doctor = request.form.get('doctor')
    appointment_time = request.form.get('appointmentTime')

    conn = sqlite3.connect('pat_info.db')
    c = conn.cursor()
    c.execute('''INSERT INTO patients 
                 (prefix, name, phone, email, gender, age, dob, address, marital_status, spouse, doctor, appointment_time)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
              (prefix, name, phone, email, gender, age, dob, address, marital_status, spouse, doctor, appointment_time))
    conn.commit()
    conn.close()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
