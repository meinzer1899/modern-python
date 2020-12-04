#!/usr/bin/env python3

## Implementing a Publisher/Subscriber Application
# Practice the skills from previous lessons and apply them
# Start by laying out a data structure for user posts
# Create data structures to model relationships
# Build accessor functions showing an effective use of Pythons data manipulation tools

from typing import NamedTuple, Deque, DefaultDict, Set, Optional, List
from collections import deque, defaultdict
from itertools import islice
import time

User = str
Timestamp = float
Post = NamedTuple('Post', [('timestamp', float),('user', User), ('text', str)])

# deque() is preferred over list() because it supports appendleft()
posts: Deque[Post] = deque()
# defaultdict() with deque() simplifies per-user accumulation of posts
user_posts: DefaultDict[User, deque] = defaultdict(deque)
following: DefaultDict[User, Set[User]] = defaultdict(set)
followers: DefaultDict[User, Set[User]] = defaultdict(set)

def post_message(user: User, text: str, timestamp: Timestamp=None) -> None:
    timestamp = timestamp or time.time()
    post = Post(timestamp, user, text)
    posts.appendleft(post) # track posts from newest to oldest
    user_posts[user].appendleft(post)

def follow(user: User, followed_user: User) -> None:
    following[user].add(followed_user) # called twice, set.add() will eliminate duplicate
    followers[followed_user].add(user)

def posts_by_user(user: User, limit: Optional[int] = None) -> List[Post]:
    return list(islice(user_posts[user], limit))
