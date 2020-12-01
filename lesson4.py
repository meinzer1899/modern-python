#!/usr/bin/env python3

## Implementing k-means Unsupervised Machine Learning

## Part 1/2
from math import fsum, sqrt
from pprint import pprint
from typing import Iterable, Tuple, List, Sequence, Dict
from collections import defaultdict
from functools import partial
from random import sample

def transpose(matrix: Iterable[Iterable]) -> Iterable[tuple]:
    'Swap rows with columns for a 2-D array'
    return zip(*matrix)

Point = Tuple[int, ...]
Centroid = Point

points = [
    (10, 41, 23),
    ( 22, 30, 29 ),
    (11, 42, 5),
    (20, 32, 4),
    (12, 40, 12),
    (21, 36, 23),
]
pprint(points)
def mean(data: Iterable[float]) -> float:
    'Accurate arithmetic mean'
    data = list(data)
    return fsum(data) / len(data)

def dist(p: Point, q: Point, fsum=fsum, sqrt=sqrt, zip=zip) -> float:
    'Euclidean distance function for multi-dimensional data'
    return sqrt(fsum([( x - y ) **2 for x, y in zip(p, q)]))

def assign_data(centroids: Sequence[Centroid], data: Iterable[Point]) -> Dict[Centroid, List[Point]]:
    'Assign data to closest centroid'
    d = defaultdict(list)
    for point in data:
        # closest_centroid = min(centroids, key=lambda centroid: dist(point, centroid))
        closest_centroid = min(centroids, key=partial(dist, point)) # we always pass a point as first argument, so we can freeze that by using partial(). Minimum is calculated by the key function we specified there
        d[closest_centroid].append(point)
    return dict(d)

def compute_centroids(groups: Iterable[Sequence[Point]], map=map) -> List[Centroid]:
    'Compute the centroid of each group in X, Y, Z coordinates'
    return [tuple(map(mean, transpose(group))) for group in groups]

def k_means(data: Iterable[Point], k: int=2, iteration: int=50) -> List[Centroid]:
    'Compute k-means to cluster centroids from data points'
    data = list(data)
    centroids = sample(data, k)
    for _ in range(iteration):
        labeled = assign_data(centroids, data)
        centroids = compute_centroids(labeled.values())
    return centroids

if __name__ == '__main__':
    points = [
        (10, 41, 23),
        ( 22, 30, 29 ),
        (11, 42, 5),
        (20, 32, 4),
        (12, 40, 12),
        (21, 36, 23),
    ]
    centroids = k_means(points, k=2)
    d = assign_data(centroids, points)
    pprint(d, width=80)
