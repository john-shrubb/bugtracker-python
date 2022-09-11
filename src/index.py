#!/usr/bin/env python3

# Import modules

from flask import Flask, render_template, url_for, session ,redirect
from os import environ
from decouple import config
from authlib.integrations.flask_client import OAuth
from urllib.parse import urlencode, quote_plus

app = Flask(__name__)

# Basic config

app.secret_key = config('FLASK_SECRET_KEY')
app.static_folder = '../static/'
app.template_folder = '../pages'

# Auth0 Configuration

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

from api import api

app.register_blueprint(api)

# Basic Routing

@app.route('/')
def root():
	return redirect('/home', 302)

@app.get('/home')
def home():
	return render_template('index.html')

# ACCOUNTS

@app.route('/login')
def login():
	return oauth.auth0.authorize_redirect(
		redirect_uri=url_for('callback', _external=True)
	)

@app.route('/callback', methods=['GET', 'POST'])
def callback():
	token = oauth.auth0.authorize_access_token()
	session['user'] = token
	return redirect('/')

@app.route('/logout')
def logout():
	session.clear()
	return redirect(f'''https://{config("AUTH_DOMAIN")}/v2/logout?{urlencode({
		'returnTo': url_for('home', _external=True),
		'client_id': config('AUTH_CLIENT_ID')
	}, quote_via=quote_plus)}''')
