import numpy as np
from scipy.stats import norm
def factorial(x):
	if x == 0:
		return 1
	for num in range(2, x):
		x *= num
	return x

def binompdf(n, p, x):
	return p**x * (1 - p)**(n - x) * factorial(n) / (factorial(x) * factorial(n - x))

def binomcdf(n, p, x):
	sum = 0
	for num in range(x + 1):
		sum += binompdf(n, p, num)
	return sum
n = 200
conservative_sd = np.sqrt(0.5 * (1 - 0.5) / n)
for x in range(50, 150):
	p_hat = x / n
	sd = np.sqrt(p_hat * (1 - p_hat) / n)
	print(x)
	print(x, ',', binompdf(n, 0.5, x), ',', norm.cdf((.50 - p_hat) / sd), ',', norm.cdf((0.50 - p_hat) / conservative_sd))