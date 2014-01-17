from BeautifulSoup import BeautifulSoup 
doc = ['<html><head><title>Page title</title></head>',
       '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
       '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
       '<tr>',
       '<td>DP</td>',
       '<td>3</td>',
       '<td>D2013</td>',
       '<td>DPS</td>',
       '<td>.</td>',
       '<td>D20131021</td>',
       '</td>',      
       '</html>']
soup = BeautifulSoup(''.join(doc))

#print soup.prettify()
alltags = soup.findAll('td')
nisse = [tag.text for tag in alltags]

for i in range(len(nisse)):
    if nisse[i] == 'DPS' and nisse[i+1] == '.':
        print 'hutta!'
        print nisse[i+2]