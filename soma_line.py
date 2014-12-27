#!/usr/bin/env python
# -*- coding: utf-8 -

import sys

test_cases = open(sys.argv[1], 'r')
soma = [int(s.rstrip()) for s in test_cases]
print sum(soma)

test_cases.close()