#!/usr/bin/env python
# -*- coding: utf-8 -

import sys





def max_subquence(str1,str2):
	new_string1 = "".join([letter for letter in str1 if letter in str2])
	new_string2 = "".join([letter for letter in str2 if letter in str1])
	st = str(str1)

	indexs = [l for l in str1 if l in str2 and str1.index(l))]
	print indexs
	#print new_string1
	#print new_string2
	
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	if test != "\n":
		strings = test.split(";")
		max_subquence(strings[0],strings[1])