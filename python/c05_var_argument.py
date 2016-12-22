#-*- coding: utf-8 -*-

#직전의 예제 add(a, b)
#파라미터가 리스트인지, 튜플인지, 이런것들을 구분해 줘야함

#*tuple
#**dict

def family_info(name, *family_name, **info):
    print("my name is ", name)
    print("my family consist ..")
    print(family_name)
    
    for name in family_name:
        print(name)

    print("="*20)

    for key in info_key():
        print(key, ":", info[key])

my_fam = ("아버지", "엄마", "형", "동생")
my_dict = {"가훈":"잘먹고 잘살자", "지역":"부산"}
family_info("홍길동", "아버지", "엄마", "아들", 가훈="우리집 가훈", 집="부산")

def my_string(*args, seperator = "/"):
    return seperator, join(args)

my_string("빨","주","노","초","파","남","보")
