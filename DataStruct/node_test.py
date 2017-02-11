class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_data(self, new_data):
        self.data = newdata
    def set_next(self, new_next):
        self.next = new_next

temp=Node(93)
b=id(temp)
c=temp.get_data()
print(b)
print(c)
#result

class UnorderedList:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        return self.head==None
    def add(self, item):
        temp=Node(item)
        temp.set_next(self.head)
        self.head=temp
    def pop(self):
        print(self.get_data)

node_add=UnorderedList()
node_add.add(1)
node_add.add(2)
node_add.pop()


