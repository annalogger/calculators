"""
Prefix calculator

Run as below:
python prefix_calc.py
>> + * 1 2 3
5
>> - / 10 + 1 1 * 1 2
3
etc
"""

from utils import is_operator, do_calc


def pcalculator(items):

    val1 = ''
    val2 = ''

    while len(items) > 1:
        if val1 == '':
            val1 = items.pop()

        # Check whether item after next is an operator.
        # If it is, pop the next value and do the calc.
        # If not, call recursively.
        if len(items) > 1 and is_operator(items[-2]) is True:
            val2 = items.pop()
        else:
            val2 = pcalculator(items)

        op = items.pop()
        val1 = do_calc(val1, val2, op)
        # Check whether to return the value here or continue looping.
        # If the next item is an operator, this indicates we are in a recursive call.
        if len(items) > 0 and is_operator(items[-1]) is True:
            return val1

    return val1


def prefix_calc(eq):
    items = eq.split(' ')
    if len(items) == 1:
        return items.pop()
    else:
        return pcalculator(items)


if __name__ == '__main__':
    print('Prefix calculator:')

    while True:
        equ = input()
        print(prefix_calc(equ))
