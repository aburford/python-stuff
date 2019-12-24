import random

prices = [random.randint(0, 100) for _ in range(10)]
prices = [4,5,3,2,1]
low_index = 0
high_index = 1
maximum = prices[high_index] - prices[low_index]
print(maximum)
for p in range(1,len(prices)):
	print(low_index, high_index)
	if prices[p] < prices[low_index]:
		low_index = p
		high_index = p + 1
		if high_index < len(prices) and prices[high_index] - prices[low_index] > maximum:
			maximum = prices[high_index] - prices[low_index]
	elif prices[p] > prices[high_index]:
		high_index = p
		if prices[high_index] - prices[low_index] > maximum:
			maximum = prices[high_index] - prices[low_index]
print(prices)
print(maximum)