class Publisher:
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

class TechForum(Publisher):
    def __init__(self):
        self._listOfUsers = []
        self.postname = None

    def register(self, userObj):
        if userObj not in self._listOfUsers:
            self._listOfUsers.append(userObj)

    def unregister(self, userObj):
        self._listOfUsers.remove(userObj)
    def notifyAll(self):
        for objects in self._listOfUsers:
            objects.notify(self.postname)
    def writeNewPost(self, postname):
        # User writes a post.
        self.postname = postname
        # When submits the post is published and notification is sent to all
        self.notifyAll()

class Subscriber:
    def __init__(self):
        #make it uninheritable
        pass
    def notify(self):
        #OVERRIDE
        pass

class User1(Subscriber):
    def notify(self,postname):
        print 'User1 notfied of a new post %s' % postname

class User2(Subscriber):
    def notify(self, postname):
        print 'User2 notfied of a new post %s' % postname
class SisterSites(Subscriber):
    def __init__(self):
        self._sisterWebsites = ["Site1","Site2","Site3"]
    def notify(self, postname):
        for site in self._sisterWebsites:
            # Send updates by any means
            print "Sent nofication to site: %s" % site

if __name__ == "__main__":
    techForum = TechForum()
    user1 = User1()
    user2 = User2()

    sites = SisterSites()
    techForum.register(user1)
    techForum.register(user2)
    techForum.register(sites)
    techForum.writeNewPost("Observer Pattern inn Python")
    techForum.unregister(user2)
    techForum.writeNewPost("MVC Pattern in Python")
