#!/usr/bin/env python
import sys

if __name__ == "__main__":
    topCountFollowers = []
    N = 50
    for line in sys.stdin:
        topCountFollowers.append(line.rstrip().split("\t"))
    topCountFollowers.sort(key = lambda x: int(x[1]), reverse = True)
    if len(topCountFollowers) < N:
        N = len(topCountFollowers)
    for i in range(N):
        print '%s\t%s' % (topCountFollowers[i][0], topCountFollowers[i][1])
