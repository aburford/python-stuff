def lcm(small, big):
	orig = big
	while big % small != 0:
		big += orig
	if orig == 20:
		return big
	else:
		return lcm(big, orig + 1)
print(lcm(1,2))