import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	list_elements = test.rstrip().split(";")

	grid_size = int(list_elements[0])
	nunbers_for_sudoku = list_elements[1].split(",")

	sudoku = [list(int(i) for i in x) for x in zip(*[iter(nunbers_for_sudoku)]*grid_size)]

	#tuples_sudoku = zip(*[iter(nunbers_for_sudoku)]*grid_size)
	#sudoku = [list(int(i) for i in x) for x in tuples_sudoku]

	soma = 0
	for x in sudoku:
		soma = soma +sum(x)

	
	if soma == grid_size * 9:
		bool = True
	else:
		bool = False

	print bool
test_cases.close()