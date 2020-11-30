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

# Statistical significance of the difference of two means
# Example: two populations visiting my website (male and female), doing different things. Question to answer: were the different things by chance (Zufall) or do they have real meaning
# Here: drug and placebo results
from random import shuffle
from statistics import mean
drug = [7.1, 8.5, 6.4, 7.7, 8.2, 7.6, 8.4, 5.1, 8.1, 7.4, 6.9, 8.4]
placebo = [8.2, 6.1, 7.1, 7.1, 4.9, 7.4, 8.1, 7.1, 6.2, 7.0, 6.6, 6.3]
mean(drug)
mean(placebo)
observ_diff = mean(drug) - mean(placebo)
print(f'The observed difference is {mean(drug) - mean(placebo): .1f}')
# If there is non-significant observed difference, then we could be able to shuffle randomly between the two groups without difference in the mean
# Null-hypothesis is that there is no real difference between the druf
# and the placebo. Which means that any observed difference was just due to
# chance and noise.
combination = drug + placebo
half_database = len(drug)
combination[:half_database]
combination[half_database:]
# If the reshuffle (permuting, relabeling) the participant, is the new mean diff the same or more extreme than be observed
def trial():
    shuffle(combination)
    drug = combination[:half_database]
    placebo = combination[half_database:]
    new_diff = mean(drug) - mean(placebo)
    return new_diff >= observ_diff
n = 10000
print(f'p-value = {sum(trial() for _ in range(n)) / n}')
print('usually, 5% or less (p <= 0.05) to be confident')
print('So we reject our null hypothesis, and conclude observation was _not_ due to chance')

# Single server queue simulation
# Model performance of the system
from random import expovariate, gauss
from statistics import mean, median, stdev
# import done
# Find out: How long does a person usually have to wait, whats the maximum wait time
# to model the performance of the system
def simulate(average_arrival_interval = 5.6, average_service_time = 5.0, stdev_service_time = 0.5):
    num_waiting = 0
    arrivals = []
    starts = []
    arrival = service_end = 0.0
    for _ in range(20000):
        if arrival <= service_end:
            # service is currently busy, we have to wait
            num_waiting += 1
            # Simulate arrival time with expovariate: Poisson distribution with average of 5.6 seconds
            arrival += expovariate(1.0 / average_arrival_interval)
            arrivals.append(arrival)
        else:
            num_waiting -= 1
            # does the service can be consumed immediately or do we have to wait
            service_start = service_end if num_waiting else arrival
            # simulate service start time. To simulate variability we use Gauss, but other methods may be more accurate depending on our system
            service_time = gauss(average_service_time, stdev_service_time)
            service_end = service_start + service_time
            starts.append(service_start)
    return [start - arrival for arrival, start in zip(arrivals, starts)]

waits = simulate()
print(f'Mean wait: {mean(waits) :.1f}. Stdev wait: {stdev(waits) :.1f}.')
print(f'Median wait: {median(waits) :.1f}. Max wait: {max(waits) :.1f}.')

# Improve average_service_time by 4% from 5.0 to 4.8
# recudes wait time by 50%
waits = simulate(average_service_time=4.8)
print(f'Mean wait: {mean(waits) :.1f}. Stdev wait: {stdev(waits) :.1f}.')
print(f'Median wait: {median(waits) :.1f}. Max wait: {max(waits) :.1f}.')
