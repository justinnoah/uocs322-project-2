"""
John Doe's Flask API.
"""

import config
from flask import Flask, render_template

def get_options():
    return config.configuration()

# Flask(...) needs to have get_options defined before it in the module
app = Flask(__name__, template_folder='pages')

@app.route("/")
def hello():
    return "UOCIS docker demo!\n"

# Not Implemented Error Handler
@app.errorhandler(401)
def error401_not_implemented(path):
    return render_template('401.html', path=path), 401

# Forbidden Error Handler
@app.errorhandler(403)
def error403_forbidden(path):
    return render_template('403.html', path=path), 403

# Not Found Error Handler
@app.errorhandler(404)
def error404_not_found(path):
    return render_template('404.html', path=path), 404


if __name__ == "__main__":
    # Using config.py from project 1, get the config options
    opts = get_options()
    # run the app with config options
    app.run(debug=opts.DEBUG, host='0.0.0.0', port=opts.PORT)
