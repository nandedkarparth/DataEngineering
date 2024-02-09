
s = {'g', 'e', 'k', 's'}

s.add('f')
print('Set after updating:', s)


s.discard('g')
print('\nSet after updating:', s)


s.remove('e')
print('\nSet after updating:', s)

print('\nPopped element', s.pop())
print('Set after updating:', s)

s.clear()
print('\nSet after updating:', s)