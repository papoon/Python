#!/usr/bin/env python
# -*- coding: utf-8 -

import sys


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	soma = 0
	for x in test.rstrip():
		soma = soma + int(x)
	print soma

test_cases.close()