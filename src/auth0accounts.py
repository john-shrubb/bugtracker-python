# Should not be executed as __main__
# Provides auth0 account management blueprint for index.py

if __name__ == '__main__':
	from sys import exit
	exit(0)

# Allows pulling variables from .env

from os import environ
from decouple import config

# Configure flask blueprint

from flask import Blueprint, session, url_for, redirect
auth0accounts = Blueprint('auth0accounts', __name__)

# Auth0 packages stuff

from urllib.parse import urlencode, quote_plus
from authlib.integrations.flask_client import OAuth

# Auth0 Configuration

from index import oauth

# Account management

@auth0accounts.route('/login')
def login():
	return oauth.auth0.authorize_redirect(
		redirect_uri=url_for('auth0accounts.callback', _external=True)
	)

@auth0accounts.route('/callback', methods=['GET', 'POST'])
def callback():
	token = oauth.auth0.authorize_access_token()
	session['user'] = token
	return redirect('/')

@auth0accounts.route('/logout')
def logout():
	session.clear()
	return redirect(f'''https://{config("AUTH_DOMAIN")}/v2/logout?{urlencode({
		'returnTo': url_for('home', _external=True),
		'client_id': config('AUTH_CLIENT_ID')
	}, quote_via=quote_plus)}''')
