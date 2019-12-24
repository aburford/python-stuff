from ctypes import c_bool
a1, n = [int(x) for x in input().split()]
nums = [a1]
bool_array = c_bool * 200000001
visited = bool_array()
visited[a1] = True
next_diff = 1
while not visited[n]:
	while visited[next_diff]:
		next_diff += 1
	next_a = nums[len(nums)-1] + next_diff
	for i in range(len(nums)):
		visited[next_a - nums[i]] = True
	if len(nums) % 100 == 0:
		print('\r%d\t%d' % (len(nums), next_a), end='')
	nums.append(next_a)
	visited[next_a] = True
print(len(nums))