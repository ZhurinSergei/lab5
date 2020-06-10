#!/usr/bin/env python
import sys

if __name__ == "__main__":
    for line in sys.stdin:
        userIDFollowerID = line.rstrip().split(" ")
        print '%s\t%s' % (userIDFollowerID[0], 1)
