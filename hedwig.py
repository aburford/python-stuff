from functools import lru_cache
from sys import setrecursionlimit
setrecursionlimit(999999999)

@lru_cache(None)
def fib(n):
	if n < 3:
		return n
	return fib(n-1) + fib(n-2)
n = 70
print((2*fib(n) - (n+1) % 2) % 10007)

print((2*round((1/2 + 5**.5/2)**(n+1)/5**.5) - (n+1) % 2) % 10007)