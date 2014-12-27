import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	list_elements = test.rstrip().split(",")

	print ",".join(sorted(set(list_elements)))

test_cases.close()