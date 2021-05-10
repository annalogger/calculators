"""
RESTful interface to the prefix and infix calculators.

Run as below:
python restful_api.py

Then use either curl or your browser to visit:
http://127.0.0.1:5000/prefix_calc?expression=<your_URL_encoded_expression>
or
http://127.0.0.1:5000/inffix_calc?expression=<your_URL_encoded_expression>

e.g: for + 1 2 and ( 1 + 2 ):
curl "http://127.0.0.1:5000/prefix_calc?expression=%2B%201%202"

curl "http://127.0.0.1:5000/infix_calc?expression=(%201%20%2B%202%20)"
"""

from flask import Flask, request
from prefix_calc import prefix_calc
from infix_calc import infix_calc

# Initialise flask
api = Flask(__name__)


# Landing pages
@api.route('/')
def welcome():
    return "Welcome to the calculator."


# Create routes for endpoint
# Use GET requests as operations are idempotent
@api.route('/prefix_calc', methods=['GET'])
def get_prefix_calc():
    expression = request.args.get('expression')
    try:
        result = str(prefix_calc(expression))
    except (KeyError, ValueError):
        return "Error calculating the expression."
    else:
        return result


@api.route('/infix_calc', methods=['GET'])
def get_infix_calc():
    expression = request.args.get('expression')
    try:
        result = str(infix_calc(expression))
    except (KeyError, ValueError):
        return "Error calculating the expression."
    else:
        return result


if __name__ == '__main__':
    api.run()
    # If you want this to be exposed to other machines on the network, comment
    # out the above and use the below instead. You can then access the calculators
    # using the IP address of your machine instead of 127.0.0.1, e.g:
    # http://192.168.0.18:5000/prefix_calc?expression=3
    #api.run(host='0.0.0.0')
