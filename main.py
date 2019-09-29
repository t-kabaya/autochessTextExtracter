from flask import Flask
from flask import jsonify
from index import create_synergy_text

app = Flask(__name__)

@app.route("/")
def hello():
    json = {
      'foo': 'foo'
    }
    return jsonify(json)