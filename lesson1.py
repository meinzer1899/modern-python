#!/usr/bin/env python3

## PART 1/2 ##
# f strings
x = 10
print('The answer is %d today' % x)
print('The answer is {0} today'.format(x))
print('The answer is {x} today'.format(x=x))
print(f'The answer is {x} today')
print(f'The answer is {x ** 2 :08d} today')
raise ValueError(f"Expected {x!r} to be a float not a {type(x).__name__}")

# Counter Objects
from collections import Counter
d = {}
# d['dragons'] throws KeyError
d = Counter()
d['dragons'] 
d['dragons'] += 1
d
c = Counter('red green red blue red blue green'.split())
c.most_common(1)
list(c.elements())
list(c)
list(c.values())
list(c.items())

# Resampling
from statistics import mean, median, mode, stdev, pstdev
mean([50, 52, 53])
median([50, 52, 53])
median([51, 50, 52, 53])
mode([51, 50, 52, 53, 51, 51])
stdev([51, 50, 52, 53, 51, 51])
pstdev([51, 50, 52, 53, 51, 51])

s = [10, 20, 30]
t = [40, 50, 60]
u = s + t
u
u[:2]
u[-2:]
u[:2] + u[-2:]
dir(list)

s = 'abracadabra'
i = s.index('c')
i
s[i]
s.count('c')
s.count('a')
sorted(t, reverse=True)

# Lambdas
# lambda -> synonym for 'make function'
lambda x: x**2 # function <lambda> at ptr
(lambda x: x**2)(5)
# promise (asynchronous functions)
x = 5
y = 2
f = lambda : x ** y # stores function with parameters x and y
# do stuff ...
f() # only now function is executed

# Chained Comparison
x > 6 and x < 20
6 < x < 20 # similar to above line

## PART 2/2
from random import *
from statistics import mean, stdev
data = [gauss(100, 15) for i in range(1000)]
mean(data)
stdev(data)
data = [expovariate(20) for i in range(1000)]
mean(data)
stdev(data)

from random import choice, choices, sample, shuffle
outcomes = ['win', 'lose', 'draw', 'play again', 'double win']
choice(outcomes)
choices(outcomes, k=10)
from collections import Counter
Counter(choices(outcomes, k=10))
Counter (choices (outcomes, k=10000))
Counter(choices(outcomes, [5, 4, 3, 2, 1], k=10000)) # 5 times as many win and so on
shuffle(outcomes)
outcomes
sample(range(1, 57), k=6)
sample(outcomes, k=1)[0]
sample(outcomes, k=len(outcomes))
