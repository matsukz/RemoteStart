from flask import Flask
import os
from ping3 import ping

app = Flask(__name__)

@app.route("/")
def root():
    return "OK!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")