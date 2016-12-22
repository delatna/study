import math
#정렬

print("{}".format("왼쪽정렬")) #기본
print("{:<50}".format("왼쪽"))
print("{:>50}".format("오른쪽"))
print("{:^50}".format("가운데"))


print("{:^.50}".format("가운데"))

print("{:%^50}".format("가운데"))
print("{:#^50}".format("가운데"))

#수학관련 함수를 포멧에 맞추기

pi = math.pi
print("pi = ", pi)
print("pi = {:f}".format(pi))

print("pi = {:2f}".format(pi))

print("pi = {:f} vs {:+f} vs {:+f}".format(pi, pi, -pi))

print("{}".format(1234567890))
print("{:,}".format(1234567890))

#백분율 표기
print("{:%}".format(1/3))
print("{:.2%}".format(1/3))

##C언어 스타일의 포멧도 지원하지만 ,추천하지는 않음

print("pi is %.2f" % math.pi)
