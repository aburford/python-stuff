from itertools import permutations

n = int(input())

def is_prime_cycle(cycle):
	for i in range(len(cycle)):
		if not primes[cycle[i]+cycle[i-1]]:
			return False
	return True

# precompute primes
primes = [True] * 2*n
for i in range(2, int(2*n ** 1/2)):
	if primes[i]:
		for multiple in range(2*i, len(primes), i):
			primes[multiple] = False

count = 0
for perm in permutations(range(2, n+1)):
	perm = [1] + list(perm)
	if is_prime_cycle([1] + list(perm)):
		count += 1
		print(perm)

print(count)
