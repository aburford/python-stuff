# Euler Project #1
def sum(factors, limit):
	sum = 0
	for num in range(limit):
		coprime = True
		for factor in factors:
			if num % factor == 0:
				coprime = False
		if not coprime:
			sum += num
	return sum
print(sum([3,5], 1000))