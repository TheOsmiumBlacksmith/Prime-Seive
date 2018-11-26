'''
Based on the seive of Eratosthenes, this code gives a list of primes within a given compact interval and also a sublist of those which are Mersenne primes also.
'''

from math import log

def seive(a,b):
	# begin with all numbers in [2,b]
    primes = range(2,b+1)
    # and [a,b]
    atob = range(a,b+1)
    # filter out 1 as it behaves like a prime
    if 1 in atob:
        atob.remove(1)
    # filter out numbers divisible by 2, 3, 4....
    for x in primes:
        for y in atob:
            if (y%x == 0 
            and y != (x or 1)):
                atob.remove(y)
                primes.remove(y)
    # return final filtered list
    return atob

def mersenne(a,b):
    mp = []
    for m in seive(a,b):
    	# add primes which satisfy the condition
        if (log(m+1)/log(2) in range(b)):
            mp.append(m)
    return mp
    
def main():
	# take input of interval
    a = int(input("a = "))
    if a < 1:
        a = 1
    b = int(input("b = "))
    print
    # print the 
    print ("Primes : {}".format(seive(a,b)))
    print
    print ("Mersenne primes : {}".format(mersenne(a,b)))

main()
