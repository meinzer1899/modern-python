# f strings
x = 10
print('The answer is %d today' % x)
print('The answer is {0} today'.format(x))
print('The answer is {x} today'.format(x=x))
print(f'The answer is {x} today')
print(f'The answer is {x ** 2 :08d} today')
raise ValueError(f"Expected {x!r} to be a float not a {type(x).__name__}")
