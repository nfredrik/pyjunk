# Write test code in this function to achieve 
# full statement coverage on the SplayTree class.

from splay import SplayTree, Node

def test0():

    s = SplayTree()
    
   
    s.insert(3)
    s.insert(2)
    s.insert(1)

    s.find(3)
    s.find(2)
    s.find(1)


def test():
    
    n1  = Node(1)
    n2 =  Node(2)
    
    assert not n1.equals(n2)
    
    s = SplayTree()



    
    assert s.findMin() == None
    assert s.findMax() == None
    assert s.find(1) == None
    assert s.isEmpty()

    s.insert(80)
    s.insert(81)
    s.insert(82)
    
    s.insert(1)
    s.find(-999)    
    s.insert(1)
    
    s.insert(3)
    s.insert(2)
    
    for i in range(20):
        s.insert(i)


    for i in range(40,20,-1):
        s.insert(i)
        
    assert s.findMin() != None
    assert s.findMax() != None
    assert s.find(1) != None
    assert not s.isEmpty()

    s.insert(80)
    s.insert(81)
    s.insert(82)
    s.insert(82)


    s.remove(1)
    s.remove(2)
    s.remove(3)
    
    for i in range(20):
        s.remove(i)



test()

