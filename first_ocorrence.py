#!/usr/bin/env python
# -*- coding: utf-8 -

import sys
import os
test_cases = open(sys.argv[1], 'r')

for test in test_cases:
	if test != "\n":
		line = test.split(",")
		if line[1].rstrip() in line[0].rstrip():
			print line[0].rstrip().index(line[1].rstrip())

	line = None

test_cases.close()
