#!/usr/bin/env python
import sys

if __name__ == "__main__":
    countUser = 0
    countAllFollowers = 0.0
    average = 0.0
    for line in sys.stdin:
        countFollowersForUser = line.split("\t")
        currentCountFollowers = data[1]
        countUser += 1
        countAllFollowers = countAllFollowers + int(currentCountFollowers)
    if countUser != 0:
        average = countAllFollowers / countUser
    print '%s\t%s' % (countUser, average)
