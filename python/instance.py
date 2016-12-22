class Car:
    nation = "KOREA"            #클래스 변수 nation 선언
    def __init__(self, name, color, door):      #초기화 함수 재정의
        self.name = name                        #인스턴스 변수 name 선언
        self.color = color
        self.door = door

    def print_car(self):
        print("(name, color, door, nation) = (", self.name, ",", self.color, ",", self.door,",",self.nation,")")

taxi = Car('bmw', "RED", 4)
bus = Car(77,77,77)

taxi.nation

taxi.print_car()

taxi.nation = "JAPAN"
taxi.print_car()
bus.print_car()
