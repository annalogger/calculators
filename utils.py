"""
Utility functions
"""


def mult(a, b):
    return a * b


def div(a, b):
    return b / a


def add(a, b):
    return a + b


def sub(a, b):
    return b - a


operators = {
    '*': mult,
    '/': div,
    '+': add,
    '-': sub
}


def is_operator(opchar):
    if opchar in list(operators.keys()):
        return True
    else:
        return False


def do_calc(val1, val2, operator):
    #print(val1, val2, operator)
    return operators[operator](float(val1), float(val2))
