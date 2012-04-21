class Publisher(object):
    def __init__(self):
        #MAke it uninheritable
        pass
    def register(self):
        #OVERRIDE
        pass
    def unregister(self):
        #OVERRIDE
        pass
    def notifyAll(self):
        #OVERRIDE
        pass

class Producer(Publisher):
    def __init__(self):
        self._listOfUsers = []
        self.postname = None

    def register(self, userObj):
        if userObj not in self._listOfUsers:
            self._listOfUsers.append(userObj)

    def unregister(self, userObj):
        if userObj in self._listOfUsers:
            self._listOfUsers.remove(userObj)

    def notifyAll(self):
        for objects in self._listOfUsers:
            objects.notify(self.postname)
    def writeNewPost(self, postname):
        # User writes a post.
        self.postname = postname
        # When submits the post is published and notification is sent to all
        self.notifyAll()

class Observer:
    def __init__(self):
        #make it uninheritable
        pass
    def notify(self):
        #OVERRIDE
        pass

class theObserver(Observer):
    def notify(self,postname):
        print 'Observer notfied of a new post: %s' % postname


if __name__ == "__main__":
    producer = Producer()
    observer = theObserver()

    producer.register(observer) 
    producer.writeNewPost("Observer Pattern inn Python")
    producer.unregister(observer)
    producer.writeNewPost("MVC Pattern in Python")
