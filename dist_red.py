#!/usr/bin/env python
import sys

if __name__ == "__main__":
    countFollowers = None
    distributionСount = 0
    for line in sys.stdin:
        data = line.split("\t")
        currentUserID = int(data[0])
        currentCountFollower = int(data[1])
        if countFollowers == currentUserID:
            distributionСount += currentCountFollower
        else:
            if countFollowers:
                print '%s\t%s' % (countFollowers, distributionСount)
            distributionСount = currentCountFollower
            countFollowers = currentUserID
    print '%s\t%s' % (countFollowers, distributionСount)
