#filename : par_checker_general.py
#date : 2017-02-02

import stack_listdatatype as ls

def par_checker(symbol_string):
    s=ls.stack()
    balanced=True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in "{[(":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced=False
            else:
                top=s.pop()
            if not matches(top, symbol):
                balanced=False

        index = index + 1
    if balanced and s.is_empty():
        return True
    else:
        return False
def matches (open, close):
    opens="({["
    closes=")}]"
    return opens.index(open)==closes.index(close)

if __name__ == '__main__':
    print(par_checker('{[({})]()}'))
    print(par_checker('{{[{{[}}]}}'))
