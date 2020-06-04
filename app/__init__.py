from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app = Bootstrap(app)

from app import routes