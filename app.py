from flask import Flask, jsonify
from db import DB

app = Flask(__name__)


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

if __name__ == '__main__':
    app.run()
