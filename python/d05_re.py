#정규식 : Regular Expression
#패턴 매칭을 이용하는 가장 성능이 우수한 식

import re

text ="Hello Python World 010-1234-567a $ @ * 010-1234-5678 xyz"

# 3 이라는 문자를 찾기

result = re.findall("3", text)
print("result = ", result)

len = len(result)
print("len = ",len)
#len = 0 이면 못찾음, 아니면 찾음

#모든 소문자 찾기

result = re.findall("[a-z]", text)
print("소문자 = ", result)


#모든 대문자 찾기

result = re.findall("[A-Z]", text)
print("대문자 = ", result)

#휴대 전화 찾기

result = re.findall("01[0,1,6,7,8,9]-\d{4}-\d{4}", text)
print("휴대폰 = ", result)
