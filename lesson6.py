#!/usr/bin/env python3

## Applying Cluster Analysis to a Real Dataset
# Analysing voting history
# identify voting blocks with k-means

# Part 1/2
import csv
from collections import defaultdict, Counter
import glob
from pprint import pprint
from typing import NamedTuple, Dict, DefaultDict, List, Tuple
from lesson4 import k_means, assign_data

NUM_SENATORS: int = 100

with open('congress_data/congress_votes_114-2016_s20.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
# first three lines look like this:
# ['Senate Vote #20 2016-02-10T17:11:00 - H.R. 757: North Korea Sanctions Enforcement Act of 2016']
# ['person', 'state', 'district', 'vote', 'name', 'party']
# ['300002', 'TN', '', 'Yea', 'Sen. Lamar Alexander [R]', 'Republican']
with open('congress_data/congress_votes_114-2016_s20.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    vote_topic = next(reader)
    headers = next(reader)
    # tuple unpacking
    for person, state, district, vote, name, party in reader:
        print(person)

Senator = NamedTuple('Senator', [('name', str), ('party', str), ('state', str)])
VoteValue = float

# load votes which were arranged by topic and accumulate votes by senator
vote_value: Dict[str, VoteValue] = {'Yea': 1, 'Nay': -1, 'Not Voting': 0}
accumulated_record: DefaultDict[Senator, List[VoteValue]] = defaultdict(list)
for filename in glob.glob('congress_data/*.csv'):
    with open(filename, encoding='utf-8') as fn:
        reader = csv.reader(fn)
        vote_topic = next(reader)
        headers = next(reader)
        for person, state, district, vote, name, party in reader:
            senator = Senator(name, party, state)
            accumulated_record[senator].append(vote_value[vote])

# Transform the record into a plain dict that maps to tuple of votes
record: Dict[Senator, Tuple[VoteValue, ...]] = {senator: tuple(votes) for senator, votes in accumulated_record.items()}

# Use k-means to locate the cluster centroids from pattern of votes, assign each senator to the nearest cluster
centroids = k_means(record.values(), k=3, iteration=50)
clustered_votes = assign_data(centroids, record.values())

# Build a reverse mapping from a vote history to a list of senators who votet that way
votes_to_senator: DefaultDict[Tuple[VoteValue, ...], List[Senator]] = defaultdict(list)
for senator, votehistory in record.items():
    votes_to_senator[votehistory].append(senator)
assert sum(len(cluster) for cluster in votes_to_senator.values()) == NUM_SENATORS

# Display the clusters and the members (senators) of each cluster
for i, votes_in_cluster in enumerate(clustered_votes.values(), start=1):
    print(f' ================ Voting Cluster #{i} =============== '.format(i=i))
    print('\n')
    party_totals: Counter = Counter()
    for votes in set(votes_in_cluster):
        for senator in votes_to_senator[votes]:
            party_totals[senator.party] += 1
            print(senator)
    print(party_totals)
