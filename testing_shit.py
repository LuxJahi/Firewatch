import img_loc_saver
import os
from flask import Flask, request, render_template

app = Flask(__name__)

if __name__ == "__main__":
    app.run(port=4555, debug=True)



x = img_loc_saver.index()


y = img_loc_saver.upload()

print x
print y