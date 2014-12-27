#!/usr/bin/env python
# -*- coding: utf-8 -



from math import sqrt

primes = [2]
count = 1
i = 1
while count < 1000:
    i += 2
    for k in range(2, 1+int(sqrt(i+1))):
        if i%k == 0:       
            break
    else:
        count += 1
        primes.append(i)

        

print sum(primes)
