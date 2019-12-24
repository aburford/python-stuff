# well, I can't figure one out...
import math as m
import gmpy
min_x = 0
min_d = 0
# preload data
squares = []
for i in range(2, 100000000):
	squares.append(i**2)
print('preloaded')
def is_square(num):
	# sqrt = m.sqrt(num)
	# return int(sqrt) == sqrt
	return gmpy.is_square(gmpy.mpz(num))
	# return num in squares
for D in range(1, 1001):
	if not is_square(D):
		for square in squares:
			# "efficiency" check
			if (square - 1) % D == 0:
				y_squared = (square - 1) / D
				if is_square(y_squared):
					if square > min_x:
						print(D, y_squared, square)
						min_x = square
						min_d = D
					break
			if square == squares[-1]:
				print('No solution found for D:', D)
		# for y in range(1, 100000):
		# 	x_squared = y * y * D + 1
		# 	if x_squared in squares:
		# 		if x_squared > min_x:
		# 			print(D, y, x_squared)
		# 			min_x = x_squared
		# 			min_d = D
		# 		break
		# 	if y == 99999:
		# 		print('No solution found:', D)
print(min_d)