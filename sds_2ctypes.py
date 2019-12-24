from ctypes import c_bool, c_int
a1, n = [int(x) for x in input().split()]
num_array = c_int * 10000
nums = num_array()
nums_i = 0
nums[nums_i] = a1
bool_array = c_bool * 200000001
visited = bool_array()
visited[a1] = True
next_diff = 1
while not visited[n]:
	while visited[next_diff]:
		next_diff += 1
	next_a = nums[nums_i] + next_diff
	for i in range(nums_i + 1):
		visited[next_a - nums[i]] = True
	nums_i += 1
	if nums_i % 100 == 0:
		print('\r%d\t%d' % (nums_i, next_a), end='')
	nums[nums_i] = next_a
	visited[next_a] = True
print(nums_i + 1)