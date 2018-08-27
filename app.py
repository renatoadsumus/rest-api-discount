from flask import Flask, jsonify, request
from discount import *


app = Flask(__name__)

@app.route('/',methods=['GET'])
def total_amount():
    discount = Discount()
    #param_total_purchase = request.args.get('total',type = int)
    param_total_purchase = request.args['total']
    #print("VVVVVVVVVVVVV" + param_total_purchase)
    #total_purchase = discount.total_amount(30)
    #amount = [{'total_amount': total_purchase }]
    #return jsonify(amount)
    return param_total_purchase


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)