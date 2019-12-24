def insert(string, i, letter):
	return string[:i] + letter + string[i:]

def helper(base, mid, i):
	if mid - i >= 0:
		if mid + i >= len(base):
			base += base[mid - i]
			if mid - i == 0:
				yield base
			else:
				for x in helper(base, mid, i + 1):
					yield x
		else:
			if base[mid - i] == base[mid + i]:
				for x in helper(base, mid, i + 1):
					yield x
			else:
				for x in helper(insert(base, mid - i + 1, base[mid + i]), mid + 1, i + 1):
					yield x
				for x in helper(insert(base, mid + i, base[mid - i]), mid, i + 1):
					yield x
	else:
		if mid + i >= len(base):
			yield base
		else:
			base = base[mid + i] + base
			if mid + i == len(base) - 1:
				yield base
			else:
				for x in helper(base, mid + 1, i + 1):
					yield x
class ShortPalindromes:
	def shortest(self, base):
			half = int(len(base) / 2)
			palins = []
			shortest = 999
			for mid in range(half + 1):
				for palin in helper(base, mid, 1):
					if len(palin) == shortest:
						palins.append(palin)
					elif len(palin) < shortest:
						shortest = len(palin)
						palins = [palin]
			palins.sort()
			return palins[0]