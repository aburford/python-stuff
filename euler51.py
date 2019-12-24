import math as m
# start building list of primes in ascending order
# for each new prime, go down list of previous primes checking for chains of similar numbers
def combinations(constants, num, level, start):
	combs = []
	upper_bound = len(num) - constants + level
	for i in range(start, upper_bound):
		temp, num[i] = num[i], '*'
		if level == constants:
			combs.append(num[::])
			num[i] = temp
		else:
			combs += combinations(constants, num, level + 1, i + 1)
			num[i] = temp
	return combs
def combinations_esoteric(constants, num, level, start):
	combs = []
	for i in range(len(num)):
		temp, num[i] = num[i], '*'
		combs.append(num[::])
		# search for duplicates
		dups = []
		for j in range(i + 1, len(num)):
			if num[j] == temp:
				dups.append(j)
		replacements = []
		for consts in range(len(dups)):
			replacements += combinations(consts, [temp for dup in dups], 0, 0)
		# print(replacements)
		for replacement in replacements:
			for k in range(len(dups)):
				num[dups[k]] = replacement[k]
				combs.append(num[::])
			# reset values
			for dup in dups:
				num[dup] = temp
		num[i] = temp
		# print(i, num)
	return combs
num = 3
primes = [['2']]
max_length = 0
solutions = 0
# while num < 56999:
while solutions < 8:
	prime = True
	for factor in range(3, m.floor(m.sqrt(num)) + 1):
		if num % factor == 0:
			prime = False
			break
	if prime == True:
		if len(str(num)) > len(primes[0]):
			primes = []
		chars = list(str(num))
		primes.append(chars)
		# start searching
		# constants is the number of digits that are the same
		# find num of primes in each chain
		# print(chars, len(chars))
		# for constants in range(len(chars) - 1):
		# 	# print('\t', constants)
		# 	for comb in combinations(constants, chars, 0, 0):
		# 		# print('\t\t', comb)
		# 		# comb = [*, *, 3, *] or something like that
		# 		chain_length = 0
		# 		for wildcard in range(10):
		# 			# replace all * with the wildcard number
		# 			replaced = [str(wildcard) if char == '*' else char for char in comb]
		# 			# print('\t\t\t', replaced)
		# 			if replaced in primes:
		# 				chain_length += 1
		# 			if chain_length > max_length:
		# 				max_length = chain_length
		# 				solution = comb
		
		for comb in combinations_esoteric(1, chars, 0, 0):
			# print('\t\t', comb)
			# comb = [*, *, 3, *] or something like that
			chain_length = 0
			for wildcard in range(10):
				# replace all * with the wildcard number
				replaced = [str(wildcard) if char == '*' else char for char in comb]
				# print('\t\t\t', replaced)
				if replaced in primes:
					chain_length += 1
				if chain_length > max_length:
					max_length = chain_length
					solution = comb
					solutions += 1
					print(solution)
	num += 2
print(solution)