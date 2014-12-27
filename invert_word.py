#!/usr/bin/env python
# -*- coding: utf-8 -
# import fileinput

# for line in fileinput.input():
# 	print line
# 	print " ".join(line.split(" ")[::-1])
    
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print " ".join(test.rstrip().split(" ")[::-1])

test_cases.close()