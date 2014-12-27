import sys


coins = [5,3,1]
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	total = int(test.rstrip())

	soma = 0
	next_coin = 0
	nunber_coins_totoal = 0

	while soma != total:
		if soma + coins[next_coin] <= total:
			soma = soma + coins[next_coin]
			nunber_coins_totoal = nunber_coins_totoal +1
			
		else:
			next_coin = next_coin +1
			
	print nunber_coins_totoal

	

test_cases.close()