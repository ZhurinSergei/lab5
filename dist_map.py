#!/usr/bin/env python
import sys

if __name__ == "__main__":
    for line in sys.stdin:
        countFollowersForUser = line.rstrip().split("\t")
        print '%s\t%s' % (countFollowersForUser[1], 1) #[1]
