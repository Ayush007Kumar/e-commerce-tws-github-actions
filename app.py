from flask import Flask, render_template

app = Flask(__name__)

DB_USER = 'root'
DB_PASSWORD = 'root'        

@app.route('/')
def home():
    return render_template('index.html')
def connect_db():
    # Logic to connect to the database using DB_USER and DB_PASSWORD
    print(f"Connecting to database with user: {DB_USER} and password: {DB_PASSWORD}")
def login(app_secret_key):
    app.secret_key = app_secret_key
    print(f"App secret key set to: {app_secret_key}")