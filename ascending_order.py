import sys


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	numbers_array = test.rstrip().split(" ")
	numbers_array_decimal= [float(x) for x in numbers_array]


	

	sorte = False
	while not sorte:
	    sorte = True
	    for i in range(len(numbers_array_decimal) - 1):
	        if numbers_array_decimal[i] > numbers_array_decimal[i+1]:
	            sorte = False
	            numbers_array_decimal[i], numbers_array_decimal[i+1] = numbers_array_decimal[i+1], numbers_array_decimal[i]

	for x in numbers_array_decimal:
		print x,
	print "\r"



test_cases.close