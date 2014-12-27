import sys


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	depht_triangule = test.rstrip()

	triangule = [[1]]

	for i in range(int(depht_triangule)-1):
		new_line_triangule = []

		new_line_triangule.append(1)
		if len(triangule[len(triangule)-1]) > 1:
			for x in range(len(triangule[len(triangule)-1])-1):
				new_line_triangule.append(triangule[len(triangule)-1][x] + triangule[len(triangule)-1][x+1])
		new_line_triangule.append(1)
		triangule.append(new_line_triangule)

	for k in triangule:
		for i in k:
			print i,
	print "\r"
	

test_cases.close()
