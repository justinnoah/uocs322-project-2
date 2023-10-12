"""
John Doe's Flask API.
"""

from flask import Flask
import config

app = Flask(__name__)
def get_options():
    return config.configuration()

@app.route("/")
def hello():
    return "UOCIS docker demo!\n"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
    opts = get_options()
