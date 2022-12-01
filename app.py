# Import Flask Dependencies
from flask import Flask

# Create a New Flask App Instance
app = Flask(__name__)

# Create Flask Routes

@app.route('/')
def add_number():
    x = 5
    y = 2
    return str(x + y)
    

@app.route('/')
def hello_world():
    return 'Hello world'

