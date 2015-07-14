
import docx
import collections

number = [str(i) for i in range(0,10)] + [chr(i) for i in range(65,91)]
#letter ='GHIJKL'
letter ='L'
g_serie = ['A{}{};'.format(l, n) for l in letter for n in number]

lollo = collections.namedtuple('log', 'text logId')
nisse = lollo(text='hej hej', logId='AG0')

def get_text(file='demo2.docx'):
    doc = docx.Document(file)
    fulltext = list()
    for para in doc.paragraphs:
        fulltext.append(para.text.encode('ascii', 'replace'))
    return fulltext


all_logIds = list()

try:
    ll = get_text()
    for number in g_serie:
        for row in ll:
            if number in str(row):
                #print(row)
                tmp = str(row).split(';')
                all_logIds.append(lollo(logId=number.strip(';'), text=tmp[-1]))
                #all_logIds.append(lollo(logId=number, text=tmp))
except UnicodeEncodeError as e:
    pass


# for x, y in all_logIds:
#     print(y,':::::::', x)


subset = set([i for i in g_serie for x, y in all_logIds if i.strip(';') == y])
alla = set(g_serie)


print('-'*20)
print('in Test spec: Not allocated', alla.difference(subset))

print('-'*20)

import os

all_cfiles = [file for file in os.listdir('.') if file.endswith('.c')]

used = list()


for file in all_cfiles:
    with open(file, 'r') as fh:
        tot = fh.readlines()
        for g in g_serie:
            g= g.strip(';')
            for i, row in enumerate(tot):
                if g in row:
                    strangen = row.strip()
                    try:
                        if '"' in tot[i+1]: 
                            strangen+= tot[i+1].strip()
                    except:
                        pass 
                    used.append(lollo(logId=g, text=strangen))

#print(used)

# for x, y in used:
#     print(y,'!!!!!!', x)



for g in g_serie:
    testspec = ''
    koden = ''
    g = g.strip(';')
    print('-'*20)    
    # check test spec
    for x, y in all_logIds:
        if g == y:
            testspec = x 
    # check what is implemented
    for x, y in used:
        if g == y:
            koden = x
            
    print('logid', g,'testpec:', testspec)
    print('koden:', koden)



