from flask import Flask, render_template, redirect, url_for, request
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yoursecretkey'

# Setup SQLite database
def get_db_connection():
    conn = sqlite3.connect('extranet.db')
    conn.row_factory = sqlite3.Row
    return conn

def setup_database():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

setup_database()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/werking')
def werking():
    return render_template('werking.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

