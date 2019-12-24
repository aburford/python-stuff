from functools import lru_cache

@lru_cache(None)
def x(n):
	if n == 2:
		return 1
	return 2*x(n-1) + 2*b(n-1)

@lru_cache(None)
def b(n):
	if n == 2:
		return 0
	if n == 3:
		return 1
	return x(n-2) + b(n-2) + b(n-1)

# count all spanning trees of fan with n nodes
@lru_cache(None)
def st(n):
	return b(n) + x(n)

n = 6
total = x(n) + b(n)
print(total)