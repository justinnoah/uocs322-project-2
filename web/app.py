"""
John Doe's Flask API.
"""

import config
from flask import Flask, render_template
import os

def get_options():
    return config.configuration()

# Flask(...) needs to have get_options defined before it in the module
app = Flask(__name__, template_folder='pages')

@app.route("/")
def hello():
    return "UOCIS docker demo!\n"

# Given a path, check whether it exists, it's forbidden, or unhandled
@app.route("/<path:path>", methods=['GET'])
def serve_path(path):
    # Handle forbidden paths, return 403
    if '..' in path:
        return error403_forbidden(path)
    elif '~' in path:
        return error403_forbidden(path)

    # Make sure endpoints end with html or css
    # Return an unimplemented error if not
    if not path.endswith(('html', 'css')):
        return error401_not_implemented(path)

    # Check if the path actually exists
    # Return path if it does, else handle error 404
    pages = os.path.join(os.getcwd(), 'pages')
    req_path = os.path.join(pages, path)
    if os.path.exists(req_path):
        return render_template(path, path=path)
    else:
        return error404_not_found(path)

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
