import sys


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	array_line = test.rstrip().split(",")
	frase = array_line[0]
	end_string = array_line[1]

	if frase[len(frase)-len(end_string):] == end_string:
		print "1"
	else:
		print "0"


test_cases.close