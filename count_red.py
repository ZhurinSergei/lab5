#!/usr/bin/env python
import sys

if __name__ == "__main__":
    currentUserID = None
    currentCountFollower = 0
    for line in sys.stdin:
        userIDCountFollower = line.split("\t")
        userID = int(userIDCountFollower[0])
        countFollower = int(userIDCountFollower[1])
        if currentUserID == userID:
            currentCountFollower += countFollower
        else:
            if currentUserID:
                print '%s\t%s' % (currentUserID, currentCountFollower)
            currentCountFollower = countFollower
            currentUserID = userID
    print '%s\t%s' % (currentUserID, currentCountFollower)
