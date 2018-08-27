from flask import Flask, jsonify, request
from discount import *


app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def total_amount():
    if request.method == 'POST':
        discount = Discount()
        total_purchase = request.form['post_total_purchase']
        total_purchase = discount.get_discount(total_purchase)
        amount = [{'total_amount': total_purchase }]
        return jsonify(amount)
    return "IT IS NOT POST"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


#param_total_purchase = request.args.get('total',type = int)
#param_total_purchase = request.args['total']