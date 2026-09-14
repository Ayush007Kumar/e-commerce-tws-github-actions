from flask import Flask, render_template

app = Flask(__name__)

DB_USER = 'root'
DB_PASSWORD = 'root12234'    

def connect_db():
    # Logic to connect to the database using DB_USER and DB_PASSWORD
    print(f"Connecting to database with user: {DB_USER} and password: {DB_PASSWORD}")

@app.route('/')
def home():
    return render_template('index.html')

