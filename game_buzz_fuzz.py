#!/usr/bin/env python
# -*- coding: utf-8 -
import fileinput
import sys

# lines = open(sys.argv[1], 'r')
# for line in lines:
# 	fizz_buzz()

def fizz_buzz(x,y,z):

	x = int(x)
	y = int(y)
	for i in xrange(1,int(z)+1):

		if i%x == 0 and i%y == 0:
			print "FB",
		elif i%x == 0:
			print "F",
		elif i%y == 0:
			print "B",
		else:
			print i,
	print "\n"
	


for line in fileinput.input():
	x_y_z = line.rstrip().split(" ")
	fizz_buzz(x_y_z[0],x_y_z[1],x_y_z[2])