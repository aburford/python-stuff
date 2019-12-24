from functools import lru_cache

@lru_cache(maxsize=None)
def depth(admiree):
	if len(admirers[admiree]) == 0:
		return 1
	return max([depth(admirer) for admirer in admirers[admiree]]) + 1

def min_designers(admirers):
	return max([depth(admiree) for admiree in range(len(admirers))])

cases = int(input())
for t in range(cases):
	n, m = [int(x) for x in input().split()]
	admirers = [set() for _ in range(n)]
	for _ in range(m):
		i, j = [int(x) for x in input().split()]
		admirers[j].add(i)
	print(min_designers(admirers))
