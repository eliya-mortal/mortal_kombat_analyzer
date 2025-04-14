"""
Exports the Flask application for Gunicorn to use.
"""
# This file is specifically for the Gunicorn server to find our app
from keep_alive import app

# This is for compatibility with the main:app format
application = app