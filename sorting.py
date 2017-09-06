# Sorting
numbers = [5, 2, 6, 1, 0, 9]

print sorted(numbers)
print sorted(numbers, reverse=True)
print numbers

def Power(number):
    return number*3

print sorted(numbers, key=Power)

names = ['onyxia', 'velen', 'arthas', 'sylvanas', 'neltharion']

def LastLetter(string):
    return string[-1]

print sorted(names)
print sorted(names, reverse=True)
print names

print sorted(names, key=len)
print sorted(names, key=LastLetter)

names.sort()
print names
