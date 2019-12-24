def E(d):
	memo[d] - 1
end
memo = {1: 1}
for d in range(2,10):
	memo[d] = E(d)
end