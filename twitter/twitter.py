#! /usr/bin/env python
import tweetstream
import simplejson
import urllib
import time
import datetime
import sched

class twit: 
    def __init__(self,uname,pswd,filepath):
        self.uname=uname
        self.password=pswd
        self.filepath=open(filepath,"wb")

    def main(self):
        i=0
        s = sched.scheduler(time.time, time.sleep)
        output=self.filepath

        #Grab every tweet using Streaming API
        with tweetstream.TweetStream(self.uname, self.password) as stream:
            for tweet in stream:
                if tweet.has_key("text"):
                    try:
                        #Write tweet to file and print it to STDOUT
                        message=tweet['text']+ "\n"
                        output.write(message)
                        print tweet['user']['screen_name'] + ": " + tweet['text'], "\n"

                        ################################
                        #Timestamp code
                        #Timestamps should be placed once every hour
                        s.enter(10, 1, t.timestamp, (s,))
                        s.run()
                    except KeyError:
                        pass
    def timestamp(self,sc):
        now = datetime.datetime.now()
        current_time= now.strftime("%Y-%m-%d %H:%M")
        print current_time
        self.filepath.write(current_time+"\n")


if __name__=='__main__':
    t=twit("nfredrik","hoppa2lo","tweets.txt")
    t.main()