class Car:
    def __init__(self, name, color, speed):      #초기화 함수 재정의
        self.name = name        #instance variable
        self.color = color      #instance variable
        self.speed = speed      #instance variable

    def print_car(self):
        print("(name, color, speed) = (", self.name, ",", self.color, ",", self.speed,")")

taxi=Car('bmw','RED',77)
taxi.print_car()

print(taxi)

