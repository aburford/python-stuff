from functools import lru_cache
import sys
sys.setrecursionlimit(1000000)

@lru_cache(maxsize=None)
def total(n):
	if n < 4:
		return [2,11,44][n-1]
	return 2*total(n-1) + 7*total(n-2) + 2*total(n-3)

@lru_cache(maxsize=None)
def one(n):
	if n < 4:
		return [2,16,92][n-1]
	return 2*one(n-1) + 2*total(n-1) + 7*one(n-2) + 8*total(n-2) + 2*one(n-3)

@lru_cache(maxsize=None)
def two(n):
	if n < 4:
		return [1,8,50][n-1]
	return two(n-1) + total(n-1) + 7*two(n-2) + 4*total(n-2) + 2*two(n-3)

@lru_cache(maxsize=None)
def trem(n):
	if n < 4:
		return [0,4,24][n-1]
	return 4*trem(n-2) + 4*total(n-2) + 2*trem(n-3) + 2*total(n-3)

n = int(input())
print(total(n), one(n), two(n), trem(n))