import random
import time 

while(1):
    time.sleep(3)
    x=random.random()   #0~1사이의 실수생성
    if(x<0.1):
        print(x)
