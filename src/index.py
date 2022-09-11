#!/usr/bin/env python3

# Import modules

from flask import Flask

# Initialise Flask

app = Flask(__name__)

# Basic config

app.static_folder = '../static/'

# Basic Routing

@app.route('/')
def index():
	return 'Hello world'
