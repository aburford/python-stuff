from functools import lru_cache

@lru_cache(maxsize=None)
def count(n, last, prev):
	if n == 2:
		return 0 if prev == 0 else 1
	return sum([count(n-1, prev, i) for i in range(8-last-prev)])

total = 0
# loop over possible sum of last two nums in sequence
for last_two in range(8):
	for x in range(last_two+1):
		total += count(77, x, last_two-x)
print(total)