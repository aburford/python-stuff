def print_tabbed(txt, tabs):
	for _ in range(tabs):
		print('\t', end='')
	print(txt)
def partitions(num, max_part, debug_level=0):
	if num == 1:
		return 1 
	# print_tabbed(f"{num} {max_part}", debug_level)
	sum = 0
	if max_part > num - 1:
		max_part = num - 1
		sum = 1
	for split in range(1, max_part + 1):
		# print_tabbed(split, debug_level)
		sum += partitions(num - split, split, debug_level + 1)
		if debug_level == 0:
			print(sum / 190569292)
	return sum
print(partitions(100, 99))
