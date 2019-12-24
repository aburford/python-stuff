a1, n = [int(x) for x in input().split()]
nums = [a1]
visited = {a1}
next_diff = 1
file = open('answers.txt', 'w')
while n not in visited:
	if len(nums) % 100 == 0:
		print('\r%d\t%d' % (len(nums), nums[len(nums)-1]), end='')
	if len(nums) == 10000:
		break
	while next_diff in visited:
		next_diff += 1
	next_a = nums[len(nums)-1] + next_diff
	for i in range(len(nums)):
		diff = next_a - nums[i]
		if diff not in visited:
			file.write('1 %d %d\n' % (next_a - nums[i], len(nums)+1))
			visited.add(next_a - nums[i])
	if next_a not in visited:
		file.write('1 %d %d\n' % (next_a, len(nums)+1))
		visited.add(next_a)
	nums.append(next_a)
print(len(nums))
file.close()