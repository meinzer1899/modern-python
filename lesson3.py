#!/usr/bin/env python3

## Improving Reliability with MyPy and Type Hinting

## Part 1/2: Explore type hinting and static type checking
from typing import *
from collections import namedtuple
x: int = 10

def summm(x, y):
    return x + y
summm('hello ', 'world') # summm(10, 'world') would need a test, because it compiles w/o error
def sum_types(x: int, y: int) -> int:
    return x + y
sum_types(1, 2)

from collections import OrderedDict
y: OrderedDict = OrderedDict()

def seq(x: Sequence) -> None:
    print(len(x))
    print(x[2])
    for i in x:
        print(i)
    print()

seq([10, 20, 30])
seq('abcdefg') # def seq(x: Sequence[int]) -> None: will not allow strings
seq((11, 12, 13))
# seq(None) -> detected

info: Tuple[str, ...] = ('Person', 'Peter', 'etc')

Point = NamedTuple('Point', [('x', int), ('y', int)])

## Part 2/2: Examine tools for organizing and analyzing data
from math import fsum
sum([0.1] * 10)
fsum([0.1] * 10)

# Defaultdict creates a new container sto store elements
# with a common feature
from collections import defaultdict, namedtuple
from itertools import zip_longest
m = [
    [10, 20],
    [30, 40],
    [50, 60],
] # 3 rows by 2 columns
list(zip(*m)) # transpoed the matrix (zip-star)
[x for row in m for x in row] # flatten 2-D matrix in 1-D vector (list comprehension)
