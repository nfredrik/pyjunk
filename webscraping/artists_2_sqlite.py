#! /usr/bin/env python
import urllib2
from BeautifulSoup import BeautifulSoup 
import sqlite3
import sys
from time import time
#db = MySQLdb.connect("localhost","bob","cangetin","bobbelde_models" )
db = sqlite3.connect('./artistdb.sqlite3')
cursor = db.cursor()


cursor.execute('''create table if not exists topranking (id, name, followers, likes, thumb, twitter, facebook, audit_who, audit_ins, audit_upd)''')

url = "http://www.musicrow.com/charts/top-ranking-country-artists"
#url = "http://dn.se"
print url
page = urllib2.urlopen(url)
#fh = open('artist.html','wb')
#fh.write(page.read())
#fh.close()
#print page.read()
#print 'the end'
#sys.exit(0)
soup = BeautifulSoup(page.read())
#print 'title:',soup.title
#print 'head:', soup.head

#print soup.prettify()
nisse =soup.find_all('tr', class_='row even')

print 'type:', type(nisse)
"""
<tr class="row even"><td class="number">1</td><td class="thumbnail" width="56px"><img src="http://a0.twimg.com/profile_images/1825696714/image_normal.jpg" 
class="thumbnail" alt="Taylor Swift" /></td><td>
<font class="artist_name">Taylor Swift</font><br />
<a href="http://www.twitter.com/taylorswift13" class="twitter_link">@taylorswift13</a> <font style="color: #ccc">|</font>
 <a href="http://www.facebook.com/TaylorSwift" class="facebook_link">FB</a></td><td class="twitter_followers">
 <font class="followers actv" >23,224,083</font><br /><font class="small">Followers</font></td>

<tr class="row even">
<td class="number">7</td>
<td class="thumbnail" width="56px"><img src="http://a0.twimg.com/profile_images/2574775869/image_normal.jpg" class="thumbnail" alt="Billy Ray Cyrus" /></td>
<td><font class="artist_name">Billy Ray Cyrus</font><br /><a href="http://www.twitter.com/billyraycyrus" class="twitter_link">@billyraycyrus</a> <font style="color: #ccc">|</font> <a href="http://www.facebook.com/BillyRayCyrus" class="facebook_link">FB</a></td>
<td class="twitter_followers"><font class="followers actv" >1,108,681</font><br /><font class="small">Followers</font></td>
<td class="facebook_likes"><font class="likes noactv" >118,578</font><br /><font class="small">Likes</font></td>

"""
#for row in soup.find_all(attrs={'class': 'row odd'}):  universities=soup.findAll('a',{'class':'institution'})
#for row in soup.find_all( 'tr', {'class': 'row odd'}):
for row in soup.find_all("tr"):
    print row
    sys.exit(0)    
    artist = [text for text in row.stripped_strings]
  
    name = artist[1]
    followers = artist[5]
    likes = artist[7]
  
    thumb = row.select("img")[0]['src']
    twitter = row.select("a")[0]['href']
    facebook = row.select("a")[1]['href']
    tstamp = int(time())
  
    sql = """INSERT INTO top_ranking (id, name, followers, likes, thumb, 
            twitter, facebook, audit_who, audit_ins, audit_upd) VALUES
            (NULL, '%s', '%s', '%s', '%s', '%s', '%s', 'admin', '%d', NULL);
            """ % (name, followers, likes, thumb, twitter, facebook, tstamp)
  
    try:
      cursor.execute(sql)
      db.commit()
    except:
      print 'Failed to store'  
      db.rollback()
      db.close()
      
    
    print 'the end'  
  