#!/usr/bin/env python2
#!-*- coding: utf-8 -*-

import random
import string
import sys
import time

__version__ = '0.1.1'
__doc__ = '''Learn to type 10 fingers'''


LIMITTIMES = 3
STANDARDTIMES = 30


def run(length):
    count = 0
    while True:
        time.sleep(1)
        print "string pattern:"
        str_pattern = ''.join(random.choice(string.printable.split('\t')[0])
                              for i in range(int(length)))
        print str_pattern
        starttime = time.time()
        your_str = raw_input("Enter your string in %d seconds" % LIMITTIMES +
                             " (press Ctrl + C to exit):\n" )
        endtime = time.time()
        yourtime = endtime - starttime

        print "Spent %s seconds" % yourtime

        if yourtime > LIMITTIMES:
            print "Too slow, need to learn more"
            sys.exit(1)

        if your_str == str_pattern:
            count = count + 1
            print "You are great."
            print "your passed times:", count
            print "-------------------------------------------------------"
            if count == STANDARDTIMES:
                print "Congratulation, going to next level"
                print "The number of characters will increase 1"
                count = 0
                length = length + 1
                run(length)
            continue
        else:
            print "Wrong, you need to train more!"
            sys.exit(2)

if __name__ == '__main__':
    run(2)
