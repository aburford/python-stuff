from copy import deepcopy

# can position num go in sq
def valid(grid, sq, num):
	if sq[0] > 0:
		if grid[sq[0]-1][sq[1]] == num:
			return False
		if sq[1] > 0 and grid[sq[0]-1][sq[1]-1] == num:
			return False
		if sq[1] < c - 1 and grid[sq[0]-1][sq[1]+1] == num:
			return False
	if sq[0] < r - 1:
		if grid[sq[0]+1][sq[1]] == num:
			return False
		if sq[1] > 0 and grid[sq[0]+1][sq[1]-1] == num:
			return False
		if sq[1] < c - 1 and grid[sq[0]+1][sq[1]+1] == num:
			return False
	if sq[1] > 0 and grid[sq[0]][sq[1]-1] == num:
		return False
	if sq[1] < c - 1 and grid[sq[0]][sq[1]+1] == num:
		return False
	return True

def valid_permutations(grid, region, sq_i, nums):
	sq = region[sq_i]
	if grid[sq[0]][sq[1]] != 0:
		if sq_i == len(region) - 1:
			yield grid
		else:
			for perm in valid_permutations(grid, region, sq_i + 1, nums):
				yield perm
	else:
		for i in range(len(nums)):
			if valid(grid, sq, nums[i]):
				next_grid = deepcopy(grid)
				next_grid[sq[0]][sq[1]] = nums[i]
				next_nums = deepcopy(nums)
				next_nums.remove(nums[i])
				if sq_i == len(region) - 1:
					yield next_grid
				else:
					for perm in valid_permutations(next_grid, region, sq_i + 1, next_nums):
						yield perm

# grid is 2d list, region_i is index for next region to fill in
def solve(grid, region_i):
	region = regions[region_i]
	# remove existing numbers from nums
	nums = list(range(1, len(region)+1))
	for sq in region:
		if grid[sq[0]][sq[1]] != 0:
			nums.remove(grid[sq[0]][sq[1]])
	for perm in valid_permutations(grid, region, 0, nums):
		if region_i == len(regions) - 1:
			yield perm
		else:
			for soln in solve(perm, region_i + 1):
				yield soln
	
def parse_region(r):
	_, *r = r.split()
	return [[int(num) - 1 for num in sq.strip('()').split(',')] for sq in r]

r, c = [int(x) for x in input().split()]
grid = []
for _ in range(r):
	grid.append([int(x) if x != '-' else 0 for x in input().split()])
region_count = int(input())
regions = []
for _ in range(region_count):
	regions.append(parse_region(input()))
regions.sort(key=lambda x: len(x))
for solution in solve(grid, 0):
	for r in solution:
		print(' '.join([str(x) for x in r]))
	break