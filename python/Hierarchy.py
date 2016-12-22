var = "Hello Python world"
print(id(var))

print(type(var))

print(str)

print(type(str))

print(int)

var.__class__       #var 클래스 확인

print(var.__class__)

class Car:
    color = str()
    def print_car(self):     #파라미터가 없으면 안된다
       print("color =",self.color)

taxi = Car()
print("type(taxi) = ",type(taxi))
taxi.color = "RED"

taxi.print_car()
