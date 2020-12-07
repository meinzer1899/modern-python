#!/usr/bin/env python3

# Implementing a Publisher/Subscriber Application
# Practice the skills from previous lessons and apply them
# Start by laying out a data structure for user posts
# Create data structures to model relationships
# Build accessor functions showing an effective use of Pythons data
# manipulation tools

from typing import NamedTuple, Deque, DefaultDict, Set, Optional, List
from collections import deque, defaultdict
from itertools import islice
from heapq import merge
from sys import intern  # interning
import time

User = str
Timestamp = float
Post = NamedTuple('Post', [('timestamp', float),
                           ('user', User), ('text', str)])

# deque() is preferred over list() because it supports appendleft()
posts = deque()  # type: Deque[Post]
# defaultdict() with deque() simplifies per-user accumulation of posts
user_posts = defaultdict(deque)  # type: DefaultDict[User, deque]
following = defaultdict(set)  # type: DefaultDict[User, Set[User]]
followers = defaultdict(set)  # type: DefaultDict[User, Set[User]]


def post_message(user: User, text: str, timestamp: Timestamp = None) -> None:
    user = intern(user)
    timestamp = timestamp or time.time()
    post = Post(timestamp, user, text)
    posts.appendleft(post)  # track posts from newest to oldest
    user_posts[user].appendleft(post)


def follow(user: User, followed_user: User) -> None:
    user, followed_user = intern(user), intern(followed_user)
    # called twice, set.add() will eliminate duplicate
    following[user].add(followed_user)
    followers[followed_user].add(user)


def posts_by_user(user: User, limit: Optional[int] = None) -> List[Post]:
    return list(islice(user_posts[user], limit))


def posts_for_user(user: User, limit: Optional[int] = None) -> List[Post]:
    # we want to merge the resulting deque lists into one list
    relevant = merge(*[user_posts[followed_user]
                       for followed_user in following[user]], reverse=True)
    return list(islice(relevant, limit))


def search(phrase: str, limit: Optional[int] = None) -> List[Post]:
    # Pre-Indexing would increase search speed
    # Add time sensitive caching of search queries
    return list(islice((post for post in posts if phrase in post.text), limit))
