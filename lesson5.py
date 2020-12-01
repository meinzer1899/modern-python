#!/usr/bin/env python3

## Building Additional Skills for Data Analysis
# Build more sophistication in data extraction, transformation, and analysis
# Lean more defaultdict skills (to pivot and accumulate data)
# Explore csv reader
# Learn how to partially consume iterators
# Review Pythons core idioms and the use of assertions

## Part 1/2
from collections import defaultdict
from pprint import pprint
d = defaultdict(list)
d['raymond'].append('red')
d['rachel'].append('yellow')
d['matthew'].append('black')
print(d)
# defaultdict for grouping (previous lesson) or accumulation (this lesson)

# Model one-to-many: dict(one, list-of-many)
e2s = {
    'one': ['uno'],
    'two': ['dos'],
    'three': ['tres'],
    'trio': ['tres'],
    'free': ['libre', 'gratis'],
}
pprint(e2s)
s2e = defaultdict(list)
for eng, spanwords in e2s.items():
    for span in spanwords:
        s2e[span].append(eng)
pprint(s2e)

e2s = dict(one='uno', two='dos', three='tres')
{span: eng for eng, span in e2s.items() }

## Part 2/2
import glob
glob.glob('*.txt') # newer, alternative way: os.expand_wildcards()

with open('congress_data/congress_votes_114-2016_s20.csv', encoding='utf-8') as f:
    print(f.read())

import csv
with open('congress_data/congress_votes_114-2016_s20.csv', encoding='utf-8') as f:
    for row in csv.reader(f):
        print(row)

# tuple unpacking
t = ('Raymond', 'Hettinger', 54)
type(t)
len(t)
fname, lname, age = t
print(fname)
names = 'raymond rachel matthew'.split()
colors = 'white black cyanmagentared'.split()
# old fashioned (slow, low level)
for i in range(len(names)):
    print(names[i].upper())
# better
for name in names:
    print(name.upper())

# old fashioned (slow, low level)
for i in range(len(names)):
    print(i+1, names[i])
# better
for i, name in enumerate(names, start=1):
    print(i, name)

for color in reversed(colors):
    print(color)

for name, color in zip(colors, names):
    print(name, color)

for color in sorted(colors):
    print(color)

for color in sorted(colors, key=len):
    print(color)

# SELECT DISTINCT city FROM Cities ORDER BY city:
cities = 'houston dallas chicago austin'.split()
for i, city in enumerate(reversed(sorted(set(cities)))):
    print(i, city)
for i, city in enumerate(map(str.upper, reversed(sorted(set(cities))))):
    print(i, city)
