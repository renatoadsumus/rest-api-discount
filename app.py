from flask import Flask, jsonify, request, json
from discount import *


app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def total_amount():
    if request.method == 'POST':
        discount = Discount()

        ### RECEIVE PARAM BY POST FROM CLIENT ###
        total_purchase = request.form['post_total_purchase']

        ### CALCULATING DISCOUNT ###
        total_discount = discount.get_discount(total_purchase)

        #### BUILDING JSON TO SEND TO CLIENT ###
        discounts = [{'total_discount': total_discount }]
        print(json.dumps(request.json))
        return jsonify({'discount': discounts})
    return "IT IS NOT POST"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)






#param_total_purchase = request.args.get('total',type = int)
#param_total_purchase = request.args['total']