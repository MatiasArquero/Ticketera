from flask import Flask, render_template
from flask import Blueprint

home_bp = Blueprint('home',__name__,template_folder='templates')

@home_bp.route('/')
def home():
    return render_template("home/home.html")