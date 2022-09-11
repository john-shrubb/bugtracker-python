from flask import Blueprint, render_template, session

api = Blueprint('API', __name__, static_folder='../static')

@api.get('/api/loggedin')
def abcd():
	if 'user' in session:
		return 'logged in'
	else:
		return 'logged out'