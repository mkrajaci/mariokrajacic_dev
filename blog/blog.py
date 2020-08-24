from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route('/<username>')
def hello_world(username):
    return 'Hello, %s' % escape(username)
