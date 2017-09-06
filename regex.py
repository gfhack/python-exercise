# Regular Expressions
import re

arthas = 'Arthas Menethil456'
uther = 'Uther the Lightbringer'

match = re.search(r'the', uther)

if match:
    print 'matched', match.group()

match = re.search(r'\d+', arthas)

if match:
    print 'matched', match.group()

str = 'purple illidan@stormrage.com monkey dishwasher'
match = re.search('([\w.-]+)@([\w.-]+)', str)
if match:
    print match.group()
    print match.group(1)
    print match.group(2)

str = 'purple alice@bob.com, blah monkey bob@alice.com blah dishwasher'

emails = re.findall(r'[\w\.-]+@[\w\.-]+', str)
for email in emails:
    print email

file = open('names.txt', 'r')

string = re.findall(r'[aeiou]', file.read())

print string