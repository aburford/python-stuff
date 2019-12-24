arr = [x for x in range(1,101)]
total = 0
def sum(arr):
	sum = 0
	for i in arr:
		sum += i
	return sum
for num in range(len(arr)):
	total += arr.pop(num) * sum(arr)
	arr.insert(num, num + 1)
print(total)