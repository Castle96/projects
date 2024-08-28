from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import csv
import subprocess

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('orders.db')
    conn.row_factory = sqlite3.Row

    # Create the "orders" table if it doesn't exist
    conn.execute('''CREATE TABLE IF NOT EXISTS orders (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      coffee_type TEXT,
                      size TEXT,
                      extra_shots INTEGER,
                      syrup_flavor TEXT,
                      timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                  )''')

    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pong')
def pong():
    subprocess.Popen(["python", "pong.py"])
    return render_template('pong.html')

@app.route('/coffee')
def coffee():
    return render_template('coffee.html')

@app.route('/confirm', methods=['POST'])
def confirm_order():
    try:
        coffee_type = request.form['type']
        size = request.form['size']
        extra_shots = int(request.form['extra_shots'])
        syrup_flavor = request.form['syrup_flavor']

        conn = get_db_connection()
        conn.execute('INSERT INTO orders (coffee_type, size, extra_shots, syrup_flavor) VALUES (?, ?, ?, ?)',
                     (coffee_type, size, extra_shots, syrup_flavor))
        conn.commit()
        conn.close()

        return render_template('confirm.html', coffee_type=coffee_type, size=size, extra_shots=extra_shots, syrup_flavor=syrup_flavor)
    except Exception as e:
        print(f"Error: {e}")
        return f"An error occurred: {e}"

@app.route('/export')
def export_orders():
    try:
        conn = get_db_connection()
        orders = conn.execute('SELECT * FROM orders').fetchall()
        conn.close()

        with open('orders.csv', 'w', newline='') as csvfile:
            fieldnames = ['id', 'coffee_type', 'size', 'extra_shots', 'syrup_flavor', 'timestamp']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for order in orders:
                writer.writerow(order)

        return render_template('export.html')
    except Exception as e:
        print(f"Error: {e}")
        return f"An error occurred: {e}"

if __name__ == "__main__":
    app.run(debug=True)
