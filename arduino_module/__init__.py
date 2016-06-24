from flask import Flask
app = Flask(__name__)
from arduino_module import views

