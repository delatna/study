num = input("학생 수 : ")
kor = []
eng = []
mat = []

for sub in range(0, int(num)):
    kor.append(int(input("국어 점수: ")))
    eng.append(int(input("영어 점수: ")))
    mat.append(int(input("수학 점수: ")))

print(kor)
print(eng)
print(mat)

what_num = input("몇번 학생의 평균을 보고싶은가?")

for avg in range(0, int(num)):
    if int(avg) == int(what_num):
        print((kor[avg] + eng[avg] + mat[avg])/3)

