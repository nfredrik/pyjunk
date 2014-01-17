#!/usr/bin/python

import urllib
import re
import csv
import gdata.calendar.data
import gdata.calendar.client
import gdata.acl.data
import atom

# 'OMX STOCKHOLM           359.39  -1.45'

class Storage:
    def save(self, date,  index,  deviation):
        self.date =date
        self.index=index
        self.deviation=deviation
        
        
class Calender:
     def __init__(self):
         self.cal_client = gdata.calendar.client.CalendarClient(source='Google-Calendar_Python_Sample-1.0')
         self.cal_client.ClientLogin('fredrik.svard@gmail.com', 'mobil4Nyckelknippa', self.cal_client.source)
         
     def store(self,  date):
        cmd = "google calendar add --cal \"dagar\" \"Susanne dag "
        cmd +=date
        cmd += "\""
        print cmd
        
     def _PrintOwnCalendars(self):
        feed = self.cal_client.GetOwnCalendarsFeed()
        print 'Printing owncalendars: %s' % feed.title.text
        for i, a_calendar in zip(xrange(len(feed.entry)), feed.entry):
          print '\t%s. %s' % (i, a_calendar.title.text,)
            
            
     def _InsertEvent(self, title='Tennis with Beth',
         content='Meet for a quick lesson', where='On the courts',
        start_time=None, end_time=None, recurrence_data=None):
   
        event= gdata.calendar.data.CalendarEventEntry()
        event.title = atom.data.Title(text=title)
        event.content = atom.data.Content(text=content)
        event.where.append(gdata.data.Where(value=where))

        if recurrence_data is not None:
        # Set a recurring event
            event.recurrence = gdata.data.Recurrence(text=recurrence_data)
        else:
          if start_time is None:
            # Use current time for the start_time and have the event last 1 hour
            start_time = time.strftime('%Y-%m-%dT%H:%M:%S.000Z', time.gmtime())
            end_time = time.strftime('%Y-%m-%dT%H:%M:%S.000Z',
                time.gmtime(time.time() + 3600))
            event.when.append(gdata.data.When(start=start_time, end=end_time))
         
        new_event = self.cal_client.InsertEvent(event)
        return new_event       
     
     def _InsertSingleEvent(self, title='dagar',
              content='Susanne dag', where='Ostersund sjukhus',
              start_time=None, end_time=None):
           
            new_event = self._InsertEvent(title, content, where, start_time, end_time,
                recurrence_data=None)
        
            print 'New single event inserted: %s' % (new_event.id.text,)
            print '\tEvent edit URL: %s' % (new_event.GetEditLink().href,)
            print '\tEvent HTML URL: %s' % (new_event.GetHtmlLink().href,)
        
            return new_event
            
class CSV(Storage):
    def display(self):
        print self.date,  self.index,  self.deviation

class textTv:

    def __init__(self):
        self.sock = urllib.urlopen("http://svt.se/svttext/web/pages/202.html")
        self.html = self.sock.read()
        self.sock.close()
        self.index = re.search('OMX STOCKHOLM[ \t]*([\d]*\.[\d]*)[ \t]*([-+][\d]*\.[\d]*)',  self.html)
        print self.index.groups()
    def getindex(self):
        print self.index.group(1)
    def getdeviation(self):
        print self.index.group(2)
        
        
        
        
# main

# Howto get the string from method???

calender = Calender()

calender._PrintOwnCalendars()

turn = csv.reader(open('dagar.csv', 'rb'), delimiter=' ', quotechar='|')

for row in turn:
    test =  ',' .join(row)
    calender.store(test)
    calender._InsertSingleEvent(start_time = "2011-02-22",  end_time = "2011-02-22")
