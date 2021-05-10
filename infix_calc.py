"""
Infix calculator

Run as below:
python infix_calc.py
>> ( 1 + 2 )
3
>> ( 1 + ( 2 * 3 ) )
7
etc
"""

from utils import is_operator, do_calc


def icalculator(items):
    var1 = ''
    var2 = ''
    op = ''

    while len(items) > 1:
        if var1 == '':
            while items[0] == '(':
                items.pop(0)
            var1 = items.pop(0)
        elif op == '':
            op = items.pop(0)
        else:
            # Check if we need to call recursively
            if items[0] == '(':
                var2 = icalculator(items)
            else:
                var2 = items.pop(0)

            result = do_calc(var2, var1, op)
            # pop the closing brace
            items.pop(0)
            # Now check if we should return the result or save to var1
            if len(items) > 0 and is_operator(items[0]):
                var1 = result
                op = ''
            else:
                return result


def infix_calc(eq):
    items = eq.split(' ')
    if len(items) == 1:
        return items[0]
    elif len(items) == 3:
        return items[1]
    else:
        return icalculator(items)


if __name__ == '__main__':
    print('Infix calculator:')

    while True:
        equ = input()
        print(infix_calc(equ))

