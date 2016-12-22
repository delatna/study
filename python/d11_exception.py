import traceback

#예외 처리

#print(1/0)

my_var = "Hello"

#print(myvar)

#age = input("Insert Age : ")

#print("내년에는 ", age + 1)

#문제 해결하기
##try ~

def exception_test():
    print("[1] 2 + '3' = ?")

    try:
        print("[2] Try ", 2 + '3') #exception

    except TypeError as err:
        print("[2] 예외 발생 !!! {}".format(err))
        traceback.print_exc()
    print("[3] Last")

exception_test()


def file_exception(file_path):
    try:
        f = open(file_path, "r")
    except IOError:
        print("Cannot Open File : ", file_path)
    else:
        print("file open")
        f.closed()
    finally:
        print("final")
