import sys
# test_cases = open(sys.argv[1], 'r')

# def longest_common_substring(s1, s2):
# 	m = [[0] * (1 + len(s2)) for i in xrange(1 + len(s1))]
# 	longest, x_longest = 0, 0
# 	for x in xrange(1, 1 + len(s1)):
# 		for y in xrange(1, 1 + len(s2)):
# 			if s1[x - 1] == s2[y - 1]:
# 				m[x][y] = m[x - 1][y - 1] + 1
# 				if m[x][y] > longest:
# 					print m
# 					longest = m[x][y]
# 					x_longest = x
# 			else:
# 				m[x][y] = 0
# 	return s1[x_longest - longest: x_longest]



# for test in test_cases:
# 	if test != "\n":

# 		sub_strigs = test.rstrip().split(";")
# 		string_left = sub_strigs[0]
# 		string_right = sub_strigs[1]

# 		sub_string = [string_right[0]]

# 		for x,y in string_right[1:],enumerate(string_left):
# 			if x in string_left:
# 				for i in sub_string:
# 					if string_left.index(i) > string_left.index(string_left[y]):
# 						continue
# 					else:
# 						sub_string[:-1] = x

# test_cases.close()

# test_cases = open(sys.argv[1], 'r')
# for test in test_cases:
# 	problem = test.rstrip().split(";")
# 	word = problem[0]
# 	sub_strings = problem[1].split(",")

# 	#tuples_words = [[i,next(it)] for i in it]
# 	#tuples_words = [[x,y] for x, y in zip(*[iter(sub_strings)]*2)]
# 	tuples_words = zip(*[iter(sub_strings)]*2)
# 	for x,v in tuples_words:
# 		word = word.replace(x,v)

# 	print word
# test_cases.close()
# def left(lista):
# 	if lista:
# 		for x in lista[0]:
# 			print x,
# 		lista.remove(lista[0])

# def down(lista):
# 	if lista:
# 		for x in range(len(lista)):
# 			print lista[x].pop(),

# def right(lista):
# 	if lista:
# 		for x in range(len(lista[0])-1,-1,-1):
# 			print lista[len(lista)-1][x],
# 		lista.remove(lista[len(lista)-1])

# def up(lista):
# 	if lista:
# 		for x in range(len(lista)-1,-1,-1):
# 			if lista[x]: print lista[x].pop(0),
		
		
	
	

# test_cases = open(sys.argv[1], 'r')
# for test in test_cases:
# 	problem = test.rstrip().split(";")
# 	linhas = int(problem[0])
# 	colunas = int(problem[1])
# 	numeros = problem[2].split(" ")

# 	tuples_words = zip(*[iter(numeros)]*colunas)
# 	list_words = [list(x) for x in tuples_words]

# 	#print numeros
# 	#print list_words

# 	while list_words:
# 		left(list_words)
# 		down(list_words)
# 		right(list_words)
# 		up(list_words)

# 	 	pass
# 	print "\r"

# test_cases.close()
lista = []
def push(item):
	lista.append(item)

def pop():
	return lista.pop()

def lene():
	return len(lista)

def clean():
	lista[:] = []

def item(x):
	return lista[x]


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	problem = test.rstrip().split(" ")

	for x in problem:
		push(x)

	for x in  xrange(lene()):
		if x % 2 ==0:
			print pop()


	print lista
	clean()


test_cases.close


