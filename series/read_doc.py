
import docx
import collections

number = [str(i) for i in range(0,10)] + [chr(i) for i in range(65,91)]
letter ='GHIJKL'
#letter ='GH'
g_serie = ['A{}{};'.format(l, n) for l in letter for n in number]


#w_serie = g_serie + h_serie


lollo = collections.namedtuple('log', 'text logId')
nisse = lollo(text='hej hej', logId='AG0')



def old_get_text(file='demo2.docx'):
    doc = docx.Document(file)
    fulltext = list()
    for para in doc.paragraphs:
        fulltext.append(para.text)
    return '\n'.join(fulltext).encode('ascii', 'replace')   # avoid exception with this

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

#print(all_logIds)

for x, y in all_logIds:
    print(y,':::::::', x)

# Find not allocated LogIds
# old_allocated = list()
# for i in g_serie:
#     ii = i.strip(';')
#     for x, y in all_logIds:
#         #print(i,y)
#         if ii == y:
#             old_allocated.append(i)


subset = set([i for i in g_serie for x, y in all_logIds if i.strip(';') == y])
alla = set(g_serie)

#print(alla)

print('-'*20)
print('Not allocated', alla.difference(subset))