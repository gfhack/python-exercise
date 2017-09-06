# List
names = ['leeroy', 'arthas', 'sylvanas']

print names

print len(names)

copied = names

copied.append('uther')

print names

names.insert(0, 'velen')
names.extend(['illidan', 'varyan'])

print names[0:2]
print names[2:]
print names[:2]
print names[1:-1]

# Loop

for name in names:
    print name

print 'it`s the final countdown'
for i in range(10):
    print i

it = 0
while it < len(names):
    print names[it]
    it += 1

# IF list

if 'arthas' in names:
    print 'found him!'
