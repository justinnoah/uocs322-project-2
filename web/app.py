"""
John Doe's Flask API.
"""

import config
from flask import Flask, render_template

def get_options():
    return config.configuration()

app = Flask(__name__, template_folder='pages')

@app.route("/")
def hello():
    return "UOCIS docker demo!\n"

if __name__ == "__main__":
    opts = get_options()
    app.run(debug=opts.DEBUG, host='0.0.0.0', port=opts.PORT)
