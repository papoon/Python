import sys


coins = [5,3,1]
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	list_elements = test.rstrip().split(" ")

	lista = list_elements[:-1]
	index = int(list_elements[len(list_elements)-1])

	if index-1 < len(lista):
		print lista[len(lista)-(index)]

	

test_cases.close()