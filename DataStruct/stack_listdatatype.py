#file name : stack_listdatatype.py
#data : 2017-02-01
class stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

if __name__ == '__main__': #단독 실행시에만 실행되는 조건!!(모듈로 import 시에는 적용안됨.)
    s=stack()
    print(s.is_empty())

    s.push(4)
    s.push("Lee")

    print(s.pop())
    print(s.peek())
    print(s.size())
    print(s.pop())
    #print(s.pop()) #indexError:pop from empty list

    ##result
    #python stack-listdatatype.py
    #None
    #Lee

