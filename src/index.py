from flask import Flask

app = Flask(__name__)

@app.route('/review/<text>')
def index(text):
  return text