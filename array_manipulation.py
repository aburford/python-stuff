import random
def array_manipulation(n, queries):
	# maintain a list of tuples for each range
	ranges = [[0,n]]
	for q in queries:
		i = 0
		r_start = 1
		r_length = ranges[i][1]
		start, end, inc = q
		while end >= r_start:
			r_end = r_start + r_length - 1
			if start <= r_start:
				if end < r_end:
					# split into two [11000]
					ranges.insert(i + 1, [ranges[i][0], r_end - end])
					ranges[i][0] += inc
					ranges[i][1] = end - r_start + 1
					break
				else:
					# increase everything in range [11111]
					ranges[i][0] += inc
					if end == r_end:
						break
					else:
						i += 1
			elif start <= r_end:
				ranges[i][1] = start - r_start
				if end < r_end:
					# split into three [01110]
					ranges.insert(i + 1, [ranges[i][0] + inc, end - start + 1])
					ranges.insert(i + 2, [ranges[i][0], r_end - end])
					break
				else:
					# split into two [00111]
					ranges.insert(i + 1, [ranges[i][0] + inc, r_end - start + 1])
					if end == r_end:
						break
					else:
						i += 2
			else:
				i += 1
			r_start = r_end + 1
			r_length = ranges[i][1]
		# search through for unnecessary ranges?
	max = 0
	for val, _ in ranges:
		if val > max:
			max = val
	return max
def array_man_slow(n, queries):
	arr = []
	for zero in range(n):
		arr.append(0)
	for q in queries:
		for i in range(q[0] - 1, q[1]):
			arr[i] += q[2]
	return max(arr)
def array_man_test(n, queries):
	max = 0
	for num in range(1, n + 1):
		sum = 0
		for q in queries:
			if num >= q[0] and num <= q[1]:
				sum += q[2]
		if sum > max:
			max = sum
	return max
n = 100000
queries = []
random.seed(1)
for _ in range(1000):
	start = random.randrange(1, n + 1)
	end = random.randrange(1, n + 1)
	if end < start:
		start, end = end, start
	queries.append([start, end, random.randrange(100)])
# print(queries)
# print(array_manipulation(n, queries))
print(array_man_slow(n, queries))
print(array_man_test(n, queries))