def insert(string, i, letter):
	return string[:i] + letter + string[i:]
def double_insert(base, mid, i, offset, right):
	return insert(insert(base, mid + i + offset, base[mid - i]), mid - i + offset, right)
def helper(base, mid, i, debug_level=1):
	# for _ in range(debug_level):
	# 	print('\t', end='')
	# print(base, mid, i)
	if mid - i >= 0:
		if mid + i >= len(base):
			base += base[mid - i]
			if mid - i == 0:
				yield base
			else:
				yield from helper(base, mid, i + 1, debug_level + 1)
		else:
			# both sides are in bounds
			if base[mid - i] == base[mid + i]:
				yield from helper(base, mid, i + 1, debug_level + 1)
			else:
				check_everything = True
				if check_everything:
					yield from helper(insert(base, mid - i + 1, base[mid + i]), mid + 1, i + 1, debug_level + 1)
					yield from helper(insert(base, mid + i, base[mid - i]), mid, i + 1, debug_level + 1)
				else:
					if base[mid + i + 1] == base[mid - i]:
						yield from helper(insert(base, mid - i + 1, base[mid + i]))
				# for offset in range(2):
				# 	yield from helper(double_insert(base, mid, i, offset, base[mid + i]), mid + 1, i + 2)
				# if base[]
				# yield from helper(double_insert(base, mid, i, 0, base[mid + i]), mid + 1, i + 2, debug_level + 1)
				# yield from helper(double_insert(base, mid, i, 1, base[mid + i]), mid + 1, i + 2, debug_level + 1)
	else:
		if mid + i >= len(base):
			yield base
		else:
			base = base[mid + i] + base
			if mid + i == len(base) - 1:
				yield base
			else:
				yield from helper(base, mid + 1, i + 1, debug_level + 1)

def shortest(base):
	global solution
	half = int(len(base) / 2)
	for mid in range(half + 1):
		print(mid)
		for palin in helper(base, mid, 1):
			# print('Palin returned:', palin)
			if solution != 0:
				if len(palin) < len(solution):
					solution = palin
				elif len(palin) == len(solution) and palin < solution:
					solution = palin
			else:
				solution = palin
	return solution
solution = 0
print('Solution:', shortest("ALRCAGOEUAOEURGCOEUOOIGFA"))
