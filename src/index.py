#!/usr/bin/env python3

# Import modules

from flask import Flask, render_template, url_for, session ,redirect
from os import environ
from decouple import config
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)

# Basic config

app.secret_key = config('FLASK_SECRET_KEY')
app.static_folder = '../static/'
app.template_folder = '../pages'

oauth = OAuth(app)

oauth.register(
	"auth0",
	client_id=config('AUTH_CLIENT_ID'),
	client_secret=config('AUTH_CLIENT_SECRET'),
	client_kwargs={
		'scope': 'openid profile email'
	},
	server_metadata_url=f'https://{config("AUTH_DOMAIN")}/.well-known/openid-configuration'
)

# Pull blueprints

from api import api
app.register_blueprint(api)

from auth0accounts import auth0accounts
app.register_blueprint(auth0accounts)

# Basic Routing

@app.route('/')
def root():
	return redirect('/home', 302)

@app.get('/home')
def home():
	return render_template('index.html')
