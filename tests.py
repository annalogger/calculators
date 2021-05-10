"""
Tests

Run as below:
python tests.py
"""

from utils import is_operator
from prefix_calc import prefix_calc
from infix_calc import infix_calc


def test_is_operator():
    print(is_operator('+'))
    print(is_operator('-'))
    print(is_operator('*'))
    print(is_operator('/'))
    print(is_operator('x'))


def test_value(in_expr, result, expected):
    if abs(float(result) - float(expected)) > 0.001: # Sufficient for these tests
        print(f"Test failed: {in_expr} is {expected}, found {result}.")
        return False
    else:
        print(f"Test passed: {in_expr}")
        return True


def test_prefix():
    test_cases = [["3", 3], ["+ 1 2", 3], ["+ 1 * 2 3", 7], ["+ * 1 2 3", 5],
                  ["- / 10 + 1 1 * 1 2", 3], ["- 0 3", -3], ["/ 3 2", 1.5],
                  ["- / 10 2 2", 3], ["+ + + + 1 2 3 4 5", 15]]
    result = True
    for test in test_cases:
        result = test_value(test[0], prefix_calc(test[0]), test[1]) and result
    if result:
        print("test_prefix tests all completed successfully.")


def test_infix():
    test_cases = [["( 1 + 2 )", 3], ["( 1 * 2 )", 2], ["( 1 + ( 2 * 3 ) )", 7],
                  ["( ( 1 * 2 ) + 3 )", 5], ["( ( ( 1 + 1 ) / 10 ) - ( 1 * 2 ) )", -1.8],
                  ["( ( ( 1 + ( 3 * 4 ) ) + 2 ) / 5 )", 3], ["( ( ( ( 1 + 2 ) + 3 ) + 4 ) + 5 )", 15],
                  ["( 1 + ( 2 + ( 3 + ( 4 + 5 ) ) ) )", 15], ["( 3 * ( ( ( 1 + 1 ) / 10 ) - ( 1 * 2 ) ) )", -5.4]]
    result = True
    for test in test_cases:
        result = test_value(test[0], infix_calc(test[0]), test[1]) and result
    if result:
        print("test_infix tests all completed successfully.")


if __name__ == '__main__':
    test_is_operator()
    test_prefix()
    test_infix()


"""
Restful API tests:

python restful_api.py

curl "http://127.0.0.1:5000/prefix_calc?expression=3"
curl "http://127.0.0.1:5000/prefix_calc?expression=%2B%201%202"
curl "http://127.0.0.1:5000/prefix_calc?expression=%2B%201%20*%202%203"
curl "http://127.0.0.1:5000/prefix_calc?expression=%2B%20*%201%202%203"
curl "http://127.0.0.1:5000/prefix_calc?expression=-%20%2F%2010%20%2B%201%201%20*%201%202"
curl "http://127.0.0.1:5000/prefix_calc?expression=-%200%203"
curl "http://127.0.0.1:5000/prefix_calc?expression=%2F%203%202"

curl "http://127.0.0.1:5000/infix_calc?expression=(%201%20%2B%202%20)"
curl "http://127.0.0.1:5000/infix_calc?expression=(%201%20%2B%20(%202%20*%203%20)%20)"
curl "http://127.0.0.1:5000/infix_calc?expression=(%20(%201%20*%202%20)%20%2B%203%20)"
curl "http://127.0.0.1:5000/infix_calc?expression=(%20(%20(%201%20%2B%201%20)%20%2F%2010%20)%20-%20(%201%20*%202%20)%20)"

"""