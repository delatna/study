class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []            #인스턴스 변수
    def add_trick(self, trick):
        self.tricks.append(trick)

#나머지는 이전과 동일하게

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


