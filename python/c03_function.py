#-*- coding: utf-8 -*-

#함수를 사용자가 직접 정의해서 사용하기
#사용하는 키워드 : def

def my_func():
    name = str(input("insert Name : "))
    print(type(name))
    print(name, " welcome")


    age = int(input("insert Age : "))
    print(name, " next year you are ", age+1, "years old")


print("call created function")


print("3 times call")

for n in range(3):
    my_func()


