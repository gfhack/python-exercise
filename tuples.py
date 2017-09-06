# Tuples

character = ('Orgrim', 40, 'Orc')

print character

(name, age, race) = character

print name
print age
print race

def ThrowSomeError():
    return (404, 'It`s not here.')

(errorNumber, errorMessage) = ThrowSomeError()

print errorNumber
print errorMessage

# Comprehensions

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

squares = [n * n for n in numbers]

print numbers
print squares

reappear = [n for n in squares if n in numbers]

print reappear

