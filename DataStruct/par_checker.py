#file name : par_checker.py
#date  : 2017.02.02

import stack_listdatatype as sl

def parChecker(symbolString):
    s=sl.stack()
    balanced=True
    index = 0
    while index < len(symbolString):
        symbol=symbolString[index]
        if symbol=="(":
            s.push(symbol)
        else:
            if s.is_empty():
                balance=false
            else:
                print(s.pop())
        index=index+1

    if balanced and s.is_empty():
        return True
    else:
        return False
if __name__ == '__main__':
    print(parChecker('((()))'))
    print(parChecker('((())'))


