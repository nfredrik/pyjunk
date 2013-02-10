class _Publisher:
    def __init__(self):
        #Make it uninheritable
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

class Publisher(_Publisher):
    def __init__(self):
        self._listOfUsers = []
        self.postname = None

    def register(self, userObj):
        #print'register!'
        if userObj not in self._listOfUsers:
            self._listOfUsers.append(userObj)

    def unregister(self, userObj):
        if userObj in self._listOfUsers:
            self._listOfUsers.remove(userObj)

    def notifyAll(self, obj):
        for objects in self._listOfUsers:
            #print 'hej', objects
            objects.notify(self)
            
    def writeNewPost(self, postname):
        # User writes a post.
        self.postname = postname
        # When submits the post is published and notification is sent to all
        self.notifyAll()

class Subscriber:
    def __init__(self):
        #make it uninheritable
        pass
    def notify(self, postname):
        #OVERRIDE
        pass

#class _Subscriber(_Subscriber):
#    def notify(self,postname):
#        print 'User1 notfied of a new post: %s' % postname



if __name__ == "__main__":
    techForum = Publisher()
    user1 = Subscriber()
   
    techForum.register(user1)
    techForum.writeNewPost("Observer Pattern inn Python")
    #techForum.unregister(user2)
    techForum.writeNewPost("MVC Pattern in Python")
