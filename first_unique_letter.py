#!/usr/bin/env python
# -*- coding: utf-8 -

import sys


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	for letter in test:
		if test.count(letter) is 1:
			print letter
			break