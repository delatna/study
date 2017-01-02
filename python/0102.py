str_count = input("학생 수 : ")
kor = []
eng = []
mat = []
scores = []
kor_avg = 0
eng_avg = 0
mat_avg = 0
avg_sum = 0
for sub in range(0, int(str_count)):
    kor.append(int(input("국어 점수: ")))
    eng.append(int(input("영어 점수: ")))
    mat.append(int(input("수학 점수: ")))
    scores.append([kor[sub], eng[sub], mat[sub]])

what_num = int(input("몇번 학생의 평균을 보고싶은가?"))

'''for avg in range(0, int(num)):
    if int(avg) == int(what_num):
        print((kor[avg] + eng[avg] + mat[avg])/3)
'''
for avg in range(0, int(str_count)):
    avg_sum = avg_sum + scores[what_num-1][avg]
    if avg == int(str_count)-1:
        print("평균은 : ", avg_sum/3) 

for sub_avg in range(0, int(str_count)):
    kor_avg = kor_avg + kor[sub_avg]
    eng_avg = eng_avg + eng[sub_avg]
    mat_avg = mat_avg + mat[sub_avg]
    if sub_avg == int(str_count) - 1:
        print("국어 평균은 : ", kor_avg / int(str_count))
        print("영어 평균은 : ", eng_avg / int(str_count))
        print("수학 평균은 : ", mat_avg / int(str_count))
