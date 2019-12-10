from flask import Flask, current_app, jsonify, request
from flask_logs import LogSetup
from datetime import datetime as dt
import logging
from logdir import LogDir
from db import DB
import os
from mylogger import MyLogger


app = Flask(__name__)

logger = MyLogger(filename='abborders.txt').logger
app.logger = logger


@app.route('/')
def hello_world():
    return jsonify({})


@app.route('/orders_summary')
def route_orders_summary():
    data = DB()
    result = data.orders_summary()
    return jsonify({'data': result})


@app.route('/order_summary/<lateral>')
def route_order_summary(lateral):
    data = DB()
    result = data.order_summary(lateral)
    return jsonify({'data': result})


@app.route('/order_detail/<lateral>')
def route_order_detail(lateral):
    data = DB()
    result = data.order_detail(lateral)
    return jsonify({'data': result})


@app.route('/settings')
def route_settings():
    from settings import Settings
    return jsonify(Settings().settings())


@app.route('/api')
def route_api():
    result = [
        {'api': '/orders_summary', 'description': 'List all available laterals, and an agrigate CFS for each lateral'},
        {'api': '/order_summary/<lateral>', 'description': 'List one lateral and associated CFS'},
        {'api': '/order_detail/<lateral>', 'description': 'List orders for a lateral'},
        {'api': '/settings', 'description': 'Database information for this api'},
        {'api': '/settings/db/<db>', 'description': 'Change settings to use <db> database'},
        {'api': '/settings/sqlserver/<server>', 'description': 'Change settings to use <server> sql server address'}
    ]
    return jsonify(result)


@app.route('/settings/db/<db>')
def route_set_db(db):
    from settings import Settings
    config = Settings()
    configvalues = config.settings()
    configvalues['database'] = db
    config.save_config(configvalues)
    return jsonify({'result': 'ok'})


@app.route('/settings/sqlserver/<server>')
def route_set_server(server):
    from settings import Settings
    config = Settings()
    configvalues = config.settings()
    configvalues['sqlserver'] = server
    config.save_config(configvalues)
    return jsonify({'result': 'ok'})


if __name__ == '__main__':
    app.run()
