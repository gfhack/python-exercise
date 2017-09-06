# String

string = 'some string'

print string[1]

print string + ' plus other string'

print 'the value of PI is ' + str(3.14)

print r'raw\t\ntext'

print 'string'.upper()

print 'first last'.startswith('first')
print 'first last'.startswith('t')
print 'first last'.endswith('last')
print 'first last'.endswith('w')

stringArray = 'lets split some string shall we?'.split(' ')
print stringArray

newString = '-'.join(stringArray)
print newString.replace('split', 'join')

print newString[:]
print newString[:5]
print newString[1:5]
print newString[1:]
print newString[-3:]
print newString[:-4]
print newString[-3:-4]