# INF601 - Advanced Programming in Python
# Braulio Mercado
# Mini Project 2

#(5/5 points) Initial comments with your name, class and project at the top of your .py file.


from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'