"""
Flask web server to keep the bot alive on Replit.
"""
import logging
import os
from flask import Flask, render_template

from config import FLASK_HOST, FLASK_PORT, BOT_CONFIGURED

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "default_secret_key")

logger = logging.getLogger(__name__)

@app.route('/')
def home():
    """
    Home route that displays basic information about the bot.
    """
    return render_template('index.html', bot_configured=BOT_CONFIGURED)

def keep_alive():
    """
    Start the Flask server to keep the bot alive.
    """
    logger.info(f"Starting Flask server on {FLASK_HOST}:{FLASK_PORT}")
    app.run(host=FLASK_HOST, port=FLASK_PORT)
