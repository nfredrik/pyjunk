
class Smaug:
    """
    Class array that keeps a fixed number of objects, set at initiation.
    Latest object on index 0.  A 'add' of  object removes the
    oldest stored element
    """
    def __init__(self,size=1):
        self.array =[]
        self.size=size
        assert self.size > 0, "Size of array need to be more than zero"
        
    def __remove(self):
        self.array.pop(-1)
        
    def add(self,value):
        """
        Add an object in first position of array. If number of elements
        has more than set 'self.size', start to remove oldest element.
        """
        self.array.insert(0,value)
        if  len(self.array) > self.size:
            self.__remove()
            
    def __getitem__(self, idx):
        # if key is of invalid type or value, the list values will raise the error
        return self.array[idx]
            
    def get_index(self,idx):
        assert  len(self.array) -1 >= idx, "Index larger than size of array"
        return self.array[idx]
    
    def __getitem__(self, idx):
        # if key is of invalid type or value, the list values will raise the error
        return self.array[idx]
    
    
    def get_current_size(self):
        return len(self.array)
    
    def print_all(self):
        print self.array
        
class MeasureDay:
    """
    Holds day of measurement and an array prices for every hours within 24 hours
    """
    def __init__(self, date, hours):
        self.date = date
        self.hours = hours
        assert len(self.hours) == 24
        
    def get_date(self):
        return self.date
    
    def get_hour(self, h):
        assert hasattr(self, 'hours')
        assert h <= len(self.hours) - 1
        return self.hours[h]
    
    def __getitem__(self, h):
        # if key is of invalid type or value, the list values will raise the error
        return self.hours[h]

MAX_SIZE = 2

"""
Check if this works with integers as objects ....
"""
smaug = Smaug(MAX_SIZE)

smaug.add(1)
smaug.add(2)
smaug.add(3)
smaug.add(4)

"""
Only a 2 objects should remain.
"""
smaug.print_all()

"""
Check with a more complex object, i.e. MeasureDay
"""
bill = Smaug(MAX_SIZE)


bill.add(MeasureDay("2011-11-11",[1,1,1,1,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]))
bill.add(MeasureDay("2012-12-24",[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]))
bill.add(MeasureDay("2012-12-25",[0,37,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]))

print 'current size:', bill.get_current_size()
print bill.get_index(0).get_date(), 'hour1:', bill.get_index(0).get_hour(1)
print bill.get_index(1).get_date(), 'hour1:', bill.get_index(1).get_hour(1)

print bill[0].get_date(), 'hour1:', bill[0][1]
print bill[1].get_date(), 'hour1:', bill[1][1]


print "get it:", bill[0][0]

print 'the end'