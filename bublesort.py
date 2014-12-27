import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	list_elements = test.rstrip().split("|")

	

	lista_sort = [int(x) for x in list_elements[0].split(" ")if x != '']
	nunber_sort = [int(x) for x in list_elements[1].split(" ")if x != '']

	
	
	
	sorte = False
	for k in range(nunber_sort[0]):
	    #sorte = True
		for i in range(len(lista_sort)-1):
			if lista_sort[i] > lista_sort[i+1]:
				#sorte = True
				lista_sort[i], lista_sort[i+1] = lista_sort[i+1], lista_sort[i]

	for x in lista_sort:
		print x,
	print "\r"

test_cases.close()