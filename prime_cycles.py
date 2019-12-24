def generate_cycle(cycle, used):
	global count
	if len(cycle) == n and primes[cycle[-1] + cycle[0]]:
		# print(cycle)
		count += 1
	else:
		for num in range(1, n+1):
			if used[num]:
				continue
			if primes[cycle[-1] + num]:
				cycle.append(num)
				used[num] = True
				generate_cycle(cycle, used)
				cycle.pop()
				used[num] = False

n = int(input())

# precompute primes
primes = [True] * 2*n
for i in range(2, int(2*n ** 1/2)):
	if primes[i]:
		for multiple in range(2*i, len(primes), i):
			primes[multiple] = False
used = [True] * 2 + [False] * (n-1)
count = 0
generate_cycle([1], used)
print(count)