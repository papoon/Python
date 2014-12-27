import sys


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	array_line = test.rstrip().split(";")
	array = [0]*int(array_line[0])
	items_array = array_line[1].split(",")

	
	for x in items_array:
		if x not in array:
			array.append(x)
		else:
			print x



test_cases.close