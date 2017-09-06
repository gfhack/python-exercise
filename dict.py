# Dict

hashTable = {}
hashTable['first'] = 'morse'
hashTable['second'] = 'code'

print hashTable

print 'first' in hashTable

print hashTable.get('second')

# Loop

for key in hashTable:
    print key, hashTable[key]

print hashTable.values()
print hashTable.items()

for key, value in hashTable.items():
    print key, ' - ', value

text = 'The first is %(first)s, the second is %(second)s' % hashTable

print text

# DEL

simpleList = ['very', 'simple', 'list']
print simpleList
del simpleList[0]
print simpleList

print hashTable
del hashTable['first']
print hashTable
