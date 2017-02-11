# Lecture/Datastructure/linkedlist.py
# DATE : 2017-01-29 (일)


class Node:
    def __init__(self, initdata):
        self.data=initdata
        self.next=None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self, newdata):
        self.data=newdata
    def setNext(self, newnext):
        self.next=newnext

temp=Node(93)
b=id(temp)
c=temp.getData()
print(b)
print(c)
#result
#4330406800
#93

class UnorderedList:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        return self.head==None
    def add(self, item):
        temp=Node(item)
        temp.setNext(self.head)
        self.head=temp
    def search(self,item):
        current=self.head
        found=False
        while current != None and not found:
            if(current.getData()==item):
                found=True
            else:
                current=current.getNext()
        return found
    def remove(self, item):
        current=self.head
        previous=None
        found=False
        while not found:
            if current.getData()==item:
                found=True
            else:
                previous=current
                current=curretn.getNext()
        if previous==None:
            self.head=current.getNext()
        else:
            previous.setNext(current.getNext())
    def pop(self):
        current=self.head
        while current.getNext().getNext()!=None:
            current=current.getNext()
        value=current.getNext().getData()
        current.setNext(None)
        return value
    def queue(self):
        current=self.head
        value=current.getData()
        self.head=current.getNext()
        return value


mylist=UnorderedList()

print(mylist.isEmpty())

mylist.add(10)
mylist.add(11)
mylist.add(12)
mylist.add(13)
mylist.add(14)
mylist.add(15)

a=mylist.search(10)
b=mylist.search(30)
print(a)
print(b)
print(mylist.pop())
print(mylist.queue())
