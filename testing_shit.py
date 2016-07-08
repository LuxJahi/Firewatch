import img_loc_saver
import os
from flask import Flask, request, render_template

app = Flask(__name__)


APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def p1():
    x = img_loc_saver.index()
    return x

@app.route("/upload", methods=['POST'])
def upload():
    x = img_loc_saver.upload()
    return x



if __name__ == "__main__":
    app.run(port=4555, debug=True)