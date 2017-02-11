#filename : quere.py
#date : 2017-02-03
import random
import time 

class Queue:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)



class Task:
    def __init__(self, time):
        self.pages=random.randrange(1,50)
        self.timestamp=time
    def getPages(self):
        return self.pages
    def getTimestamp(self):
        return self.timestamp
    def waiting_time(self, assignded_time):
        return assignded_time - self.timestamp

class Printer: 
    def __init__(self):
        self.ppm=10
        self.current_task=None
        self.time_remainning=0
    def tick(self):         #뽑은 페이지 수
        if self.current_task != None:
            self.time_remainning=self.time_remainning - 1
            if self.time_remainning < 0:
                self.current_task = None
        else:
            pass
    def busy(self):
        return self.current_task==None
    def start_next(self, new_task):
        self.time_remainning=new_task.getPages()*60/self.ppm
        self.current_task=new_task

def simulation(numSecond):
    printer=Printer()
    queue=Queue()
    waiting_time=[]

    for currentSecond in range(numSecond):
        if newPrintTask():
            task=Task(currentSecond)
            queue.enqueue(task)
        if(not queue.isEmpty()) and (printer.busy()):
            next_task=queue.dequeue()
            waiting_time.append(next_task.waiting_time(currentSecond))
            printer.start_next(next_task)

        printer.tick()

    average_wait=sum(waiting_time)/len(waiting_time)
    print("Average Waiting Time %f secs %d tasks" %(average_wait, queue.size()))
def newPrintTask():
    num=random.randrange(1, 100)
    if num<5:
        return True
    else:
        return False

for i in range(10):
    simulation(3600)

#while(1):
#    time.sleep(3)
#    x=random.random()   #0~1사이의 실수생성
#    if(x<0.1):
#        print(x)

#print("run process")
