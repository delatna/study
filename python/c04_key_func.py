#-*- coding: utf-8 -*-

#인자를 여러개 사용하거나, 기본값 정하기

def car_info(maker, door, type):
    print("차 정보 : ", maker, "사의 ", door, "개의 문이 달린 ", type)

def car_info2(maker, door=4, type="SEDAN"):
    print("차 정보 : ", maker, "사의 ", door, "개의 문이 달린 ", type)
car_info("KIA", 4, "SUB")
car_info("BMW", 2, "COUPE")

# 이렇게 호출하고 싶다.
#car_info("KIA")

car_info2("BENZ")
car_info2("AUDI", 2)
car_info2("PORCHEZ", 2, "SPORTSCAR")

#car_info2() 의 maker 는 default(기본값)이 없다
#이것을 필수값이라고 하는데
#이 값이 없으면 에러

#car_info2()

#동일 인자(매개변수)에 중복 사용하는 경우
#car_info2("현대", maker="HYUNDAI") #maker를 두번 썼기때문에 에러

#알지 못하는 키워드는 에러
car_info2("현대", type="몰라")
#car_info2("현대", color="RED")

