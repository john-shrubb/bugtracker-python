# Should not be executed as __main__.
# Provides API blueprint to index.py

if __name__ == '__main__':
	from sys import exit
	exit(0)

from flask import Blueprint, session
import json

api = Blueprint('API', __name__)

@api.get('/api/loggedin')
def loggedin():
	if 'user' in session:
		return json.dumps({
			"status": 200,
			"loggedIn": True,
		})
	else:
		return json.dumps({
			"status": 200,
			"loggedIn": False,
		})

@api.get('/api/getuserinfo')
def getuserinfo():
	if 'user' not in session:
		return '3142425'
	

	print(session['user'])
	return json.dumps(session['user']['userinfo'])