import re

def check_mobile(mobile):       #validate mobile number
    #result = re.findall("^01[016789]-\d{4}=\d{4}$", mobile)
    
    #일반적으로 파이썬에서는 r = raw(날것)
    #특수기호들이 파이썬 문자열의 특수기호를 인식하지 않고 정규식이라고 생각함
    result = re.findall(r"^01[016789]-\d{4}-\d{4}$", mobile)

    if len(result) == 0:
        print(mobile, "은 잘못된 형식")
        return False

    print(mobile, "은 정상적인 형식")
    return True

#if check_mobile("010-1234-1234") == Ture:
#    print("정상")
#else:
#    print("정상아니")

if __name__ == "__main__":

    check_mobile("1234")
    check_mobile("010-1234-5678")
    check_mobile("010-123a-5678")

