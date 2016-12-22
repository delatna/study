class Dog:
    tricks = []                         #클래스 변수(인스턴스간 공유)
    def __init__(self, name):
        self.name = name
    def add_trick(self, trick):
        self.tricks.append(trick)

fido = Dog('Fido')
buddy = Dog('Buddy')

#fido의 트릭에 구르기 추가

fido.add_trick('구르기')

#buddy 의 트릭에 짖기, 잠자기 추가

buddy.add_trick('짖기')
buddy.add_trick('잠자기')

#fido 의 트릭에 걷기 추가

fido.add_trick('걷기')

#fido 의 트릭 확인
fido.tricks

buddy.tricks



Dog.tricks.append("클래스간에 공유한다.이걸로 인스턴스를 만든 모든클래스가 공유하는값")
print(str(buddy.tricks))
    

