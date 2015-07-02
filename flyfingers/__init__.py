#!/usr/bin/env python2
#!-*- coding: utf-8 -*-
# Thurs Jun 2015

import datetime
import random
import string
import sys
import time

__version__ = '0.1.1'
__doc__ = '''Learn to type 10 fingers'''


def run(length):
    count = 0
    while True:
        time.sleep(1)
        print "string pattern:"
        str_pattern = ''.join(random.choice(string.printable.split('\t')[0])
                              for i in range(int(length)))
        print str_pattern
        starttime = datetime.datetime.now()
        your_str = raw_input("Enter your string in 3 seconds (press Ctrl +" +
                             "C to exit):\n")
        endtime = datetime.datetime.now()
        yourtime = endtime - starttime

        print "spent %s seconds" % yourtime.total_seconds()

        if yourtime.total_seconds() > 3:
            print "so slow, need to learn more"
            sys.exit(1)

        if your_str == str_pattern:
            count = count + 1
            print "You are great."
            print count
            print "-------------------------------------------------------"
            if count == 30:
                print "Congratulation, going to next level"
                count = 0
                length = length + 1
                run(length)
            continue
        else:
            print "Wrong, you need to train more!"
            sys.exit(2)

if __name__ == '__main__':
    run(2)
