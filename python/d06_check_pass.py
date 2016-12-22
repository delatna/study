import re

mobile = input("insert Phone Number : ")
result = re.findall("^01[016789]-\d{4}-\d{4}$", mobile)

if len(result) == 0:
    print("전화번호는 010-1234-5678 형식 입니다. ")
    print("확인하세요")
else:
    print("정상적인 전화번호입니다.")


