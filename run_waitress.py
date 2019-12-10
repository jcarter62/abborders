import os
import logging
from logging.handlers import RotatingFileHandler
from waitress import serve
import app

if not os.path.exists('logs'):
    os.mkdir('logs')
file_handler = RotatingFileHandler('logs/application.log', maxBytes=10240, backupCount=5)
file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]"))
# app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)
app.logger.info('Application Startup')

serve(app.app, host='0.0.0.0', port=5200)

# Reference:
# https://stackoverflow.com/a/52093761


