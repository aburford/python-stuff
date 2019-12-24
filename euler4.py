def rev_str(a_string):
    return a_string[::-1]
def palin(num):
	a = "{}".format(num)
	return a == rev_str(a)
biggest = 0
for x in range(10000, 1, -1):
	for y in range(x, 1, -1):
		product = x * y
		if palin(product) and product > biggest:
			print(x, y, product)
			biggest = product