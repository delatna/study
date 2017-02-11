#filename : dec_to_bin.py
#date : 2017-02-02

import stack_listdatatype as ls

def dec_to_bin(dec):
    dtb=ls.stack()
    mok=int(dec) 
    sur=int()
    string=str()
    #print("mok = ", mok , "sur = ", sur)
    while mok != 0:
        # print("this is stack"+str(dtb))
        # print(type(dtb))
        sur = mok % 2
        mok = mok // 2
        print("mok = ", mok , "sur = ", sur)
        dtb.push(sur)
    while not dtb.is_empty():
        string=string+str(dtb.pop())
        
    return string
if __name__ == '__main__':
    print(dec_to_bin(19))
