#file name : format.py

name = "Hong Kil Dong"
age = 13

#My name is Hong Kil Dong. I am 13 years old

print("My name is ", name, ", I am ", age, "years old")

print("My name is {}, I am {} years old".format(name,age))

print("{:^50}".format("center"))

for n in range(1, 11):
    print("{:^50}".format("*"*n))

import math

print("pi = ", 22/7)
print("pi = ", math.pi)

print("pi = {:.2f}".format(math.pi))

#숫자 1234567 => 1,234,567
money = 1234567

print("money = {:,}".format(money))

### 100만 ~ 1000100 까지의 수를 11로 나눈 값을 123,456.12 형식으로 출력

for n in range(10**6, 10**6+101):
    print(n,"/ 11 = {:,.2f}".format(n/11))
