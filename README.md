# Prefix and Infix Calculators

Written in python and tested using python 3.9.1

Both calculators have tests in test.py. Run with:
```
python tests.py
```

## Prefix Calculator

Run as follows:
```
python prefix_calc.py
Prefix calculator:
+ 1 2
3.0
+ * 1 2 3
5.0
```
Press ctrl-C to quit.

## Infix Calculator

Run as follows:
```
python infix_calc.py
Infix calculator:
( 1 + 2 )
3.0
( 1 * 2 )
2.0
```
Press ctrl-C to quit.

## RESTful interface

This requires Flask to be installed:
```
pip install flask
```
This code was tested using Flask 1.1.2

To run do:
```
python restful_api.py
```

Then use the tool curl, or your browser to visit:
```
http://127.0.0.1:5000/prefix_calc?expression=<your_URL_encoded_expression>
```
or
```
http://127.0.0.1:5000/infix_calc?expression=<your_URL_encoded_expression>
```

e.g: for + 1 2 and ( 1 + 2 ):
```
curl "http://127.0.0.1:5000/prefix_calc?expression=%2B%201%202"

curl "http://127.0.0.1:5000/infix_calc?expression=(%201%20%2B%202%20)"
```
