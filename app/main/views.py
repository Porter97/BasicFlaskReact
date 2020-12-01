from flask import render_template, request, current_app
from . import main
import requests


@main.route('/')
def index():
    return render_template("templates/index.html")

