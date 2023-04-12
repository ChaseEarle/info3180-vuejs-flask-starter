from flask import Flask
from .config import Config
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_object(Config)

from app import views

csrf = CSRFProtect(app)
