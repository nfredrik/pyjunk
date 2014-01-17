# TASK:
#
# Achieve full statement coverage on the Queue class. 
# You will need to:
# 1) Write your test code in the test function.
# 2) Press submit. The grader will tell you if you 
#    fail to cover any specific part of the code.
# 3) Update your test function until you cover the 
#    entire code base.
#
# You can also run your code through a code coverage 
# tool on your local machine if you prefer. This is 
# not necessary, however.
# If you have any questions, please don't hesitate 
# to ask in the forums!

import array
import random


class Queue:
    def __init__(self,size_max):
        assert size_max > 0
        self.max = size_max
        self.head = 0
        self.tail = 0
        self.size = 0
        self.data = array.array('i', range(size_max))

    def empty(self):
        return self.size == 0

    def full(self):
        return self.size == self.max

    def enqueue(self,x):
        if self.size == self.max:
            return False
        self.data[self.tail] = x
        self.size += 1
        self.tail += 1
        if self.tail == self.max:
            self.tail = 0
        return True

    def dequeue(self):
        if self.size == 0:
            return None
        x = self.data[self.head]
        self.size -= 1
        self.head += 1
        if self.head == self.max:
            self.head = 0
        return x

    
    def checkRep(self):
        assert self.tail >= 0
        assert self.tail < self.max
        assert self.head >= 0
        assert self.head < self.max
        if self.tail > self.head:
            assert (self.tail-self.head) == self.size
        if self.tail < self.head:
            assert (self.head-self.tail) == (self.max-self.size)
        if self.head == self.tail:
            assert (self.size==0) or (self.size==self.max)
            
      
            



# Example of random test and the use of Strong Oracle since we are using an alternate
#   implementation, the list l!

   
def random_test():
    N = 1000
    add = 0
    remove = 0
    addFull = 0
    removeEmpty = 0
    q = Queue(N)
    q.checkRep()
    l = []
    for i in range(100000):
        if (random.random() < 0.6):
            z = random.randint(0,10000000)
            res = q.enqueue(z)
            q.checkRep()
            if res:
                l.append(z)
                add += 1
            else:
                assert len(l) == N
                assert q.full()
                q.checkRep()
                addFull+=1
        else:
            dequeued = q.dequeue()
            q.checkRep()
            if dequeued is None:
                assert len(l) == 0
                assert q.empty()
                removeEmpty+=1
            else:
                expected_value = l.pop(0)
                assert expected_value == dequeued
                remove += 1
                    
    while True:
        res = q.dequeue()
        q.checkRep()
        if res is None:
           break
           
        z = l.pop(0)
        assert z == res   
        
        
    assert len(l) == 0  
    
    print "adds: =", str(add)
    print "adds to a full queue: =", str(addFull)
    print "removes", str(remove)
    print"removes from an empty queue: = ", str(removeEmpty)              
        
        
        
        
random_test()

