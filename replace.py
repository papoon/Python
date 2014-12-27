#!/usr/bin/env python
# -*- coding: utf-8 -

# import sys

# test_cases = open(sys.argv[1], 'r')

# for test in test_cases:
# 	if test != "\n":
# 		line = test.split(",")
# 		print "".join([l for l in line[0] if l not in line[1] or l == " "])

# test_cases.close()

numero_linhas = 5
numero_colunas = 5

l = 2
c = 2

matriz = [["#" if x == c and i == l else "" for x in xrange(numero_colunas)] for i in xrange(numero_linhas) ]
print "\n".join([("| {} "*5).format(*row)+"|" for row in matriz])

for row in matriz:
	if "#" in row:
		index = row.index("#")
		row.insert(index-1,"#")
		row.insert(index,"#")

print "\n".join([("| {} "*5).format(*row)+"|" for row in matriz])


    