#!/usr/bin/env python3

## PART 1/2 ##
from random import *
from statistics import *
from collections import *
# Six roulette wheels -- 18 red 18 black 2 greens
choice(['red'] * 18 + ['black'] * 18 + ['green'] * 2)
Counter(choices(['red', 'black', 'green'], [18, 18, 2], k=6))
deck = Counter(tens=16, low=36)
deck = list(deck.elements())
deal = sample(deck, 20)
Counter(deal)
deal = sample(deck, 52)
remainder = deal[20:]
Counter(remainder)
# ^--- this is the big idea with little code

# 5 or more heads from 7 spins of a biased coin
from random import *
population = ['heads', 'tails']
weight = [6, 4]
cumweight = [0.60, 1.00]
choices(['heads', 'tails'], cum_weights=[0.60, 1.00])
choices(['heads', 'tails'], cum_weights=[0.60, 1.00], k=7)
choices(['heads', 'tails'], cum_weights=[0.60, 1.00], k=7).count('heads')
trial = lambda : choices(['heads', 'tails'], cum_weights=[0.60, 1.00], k=7).count('heads') >= 5
trial()
n = 100000
sum(trial() for i in range(n)) / n # approx 0.41

# compare to the analytic approach
from math import factorial as fact
def combination(n ,r):
    return fact(n) // fact(r) // fact(n-r)
combination(10, 2)
ph = 0.6
# 5 heads out of 7 spins
ph ** 5 * (1 - ph) ** 2 * combination(7, 5)
# 6 heads out of 7 spins
ph ** 6 * (1 - ph) ** 1 * combination(7, 6)
# 7 heads out of 7 spins
ph ** 7 * (1 - ph) ** 0 * combination(7, 6)
# add them together
0.26+0.13+0.028 # approx 0.41, theoretical result
# sum(trial() for i in range(n)) / n # Empirical result

from statistics import *
from random import *
n = 100000
sample(range(n), 5)
median(sample(range(n), 5))
sorted(sample(range(n), 5))[2]
# Question
# Probability that the median of 5 samples falls a middle quartile
# Big idea: This is expressible in one short, simple line of code
trial = lambda : n // 4 < median(sample(range(n), 5)) <= 3 * n // 4
trial() # True or False
sum(trial() for i in range(n)) / n # approx 0.79

## PART 2/2 ##
# Bootstrapping to estimate the confidence interval on a sample of data
from statistics import mean, stdev
timings = [7.18, 8.59, 12.24, 7.39, 8.16, 8.68, 6.98, 8.31, 9.06, 7.06, 7.67, 10.02, 6.87, 9.07]
mean(timings)
stdev(timings)
# standard error of the mean relies on a normal distribution
# Resampling makes no such assumptions.
# Here we have an exponential distribution.
# 
# Build a 90% confidence model
from random import choices
def bootstrap(data):
    return choices(data, k=len(data))
bootstrap(timings)
mean(bootstrap(timings))
n = 10000
means = sorted(mean(bootstrap(timings)) for _ in range(n))
means[:20]
means[-20:]
mean(means)
print(f'The observed mean of {mean(timings)}')
print(f'Falls in a 90% confidence interval from {means[500] :.1f} to {means[-500] :.1f}')
# ^---- Big idea with little code
# 90% of the time, the population means going to fall between 7.8 and 9.1
# 10% of that time, there might be a sampling error where it would be outside of that range
