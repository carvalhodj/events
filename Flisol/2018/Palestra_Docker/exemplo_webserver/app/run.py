# run.py

import os

from flask import Flask
from flask import jsonify, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/env")
def api():
    response = {
        'env_value': os.getenv('ENV'),
        'debug_value': os.getenv('DEBUG')
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=os.getenv('DEBUG'), host='0.0.0.0')
