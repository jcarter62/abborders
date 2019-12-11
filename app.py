from flask import Flask, current_app, jsonify, request, has_request_context
from db import DB
import logging
from logdir import LogFile


app = Flask(__name__)

logfile = LogFile(appname='abborders')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
log_file_handler = logging.FileHandler(filename=logfile.full_path)
logger.addHandler(log_file_handler)

app.logger = logger

@app.route('/')
def hello_world():
    log(request)
    return jsonify({})


@app.route('/orders_summary')
def route_orders_summary():
    log(request)
    data = DB()
    result = data.orders_summary()
    return jsonify({'data': result})


@app.route('/order_summary/<lateral>')
def route_order_summary(lateral):
    log(request)
    data = DB()
    result = data.order_summary(lateral)
    return jsonify({'data': result})


@app.route('/order_detail/<lateral>')
def route_order_detail(lateral):
    log(request)
    data = DB()
    result = data.order_detail(lateral)
    return jsonify({'data': result})


@app.route('/settings')
def route_settings():
    from settings import Settings
    log(request)
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
    log(request)
    return jsonify(result)


@app.route('/settings/db/<db>')
def route_set_db(db):
    from settings import Settings
    config = Settings()
    configvalues = config.settings()
    configvalues['database'] = db
    config.save_config(configvalues)
    log(request)
    return jsonify({'result': 'ok'})


@app.route('/settings/sqlserver/<server>')
def route_set_server(server):
    from settings import Settings
    config = Settings()
    configvalues = config.settings()
    configvalues['sqlserver'] = server
    config.save_config(configvalues)
    log(request)
    return jsonify({'result': 'ok'})


def log(req):
    import arrow
    now_string = arrow.now().format("YYYY/MM/DD-HH:mm:ss")
    obj = {
        'stamp': now_string,
        'url': req.path,
        'ip': req.remote_addr,
        'agent': req.user_agent,
    }

    new_file = LogFile(appname='abborders').full_path
    current_file = app.logger.handlers[0].baseFilename
    if current_file != new_file:
        handler = app.logger.handlers[0]
        app.logger.removeHandler(hdlr=handler)
        handler = logging.FileHandler(filename=new_file)
        app.logger.addHandler(handler)

    logger.info('%(ip)s %(stamp)s %(url)s %(agent)s' % obj)

    return

# @app.after_request
# def app_after_request():
#     print('After Response')
#
#     context = {}
#     if has_request_context():
#         context.url = request.url
#         context.remote_addr = request.remote_addr
#     else:
#         context.url = None
#         context.remote_addr = None
#     logger.info("%(remote_addr)s: %(url)s" % context)
#

if __name__ == '__main__':
    app.run()
