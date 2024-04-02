from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

def greet("/greet")
    return "<p>Hi..! Hope you are doing great.</p>


