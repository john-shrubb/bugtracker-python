# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                         #
#    database.py                                          #
#    Connects to the postgresql database and provides     #
#    a user manager class for index.js                    #
#                                                         #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# File should not be executed as __main__. It simply provides a class to index.py to manage users.

if __name__ == '__main__':
	from sys import exit
	exit(0)


import psycopg2 as postgres

# .env variables

from os import environ
from decouple import config

# Establish a basic connection

_connection = postgres.connect(
	database=config('PSQL_DB'),
	user=config('PSQL_USERNAME'),
	password=config('PSQL_PASSWORD'),
	port=config('PSQL_PORT'),
	host=config('PSQL_HOST')
)
