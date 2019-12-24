# dp = dict()
# for n in range(2, 78):
#     for a in range(8):
#         for b in range(8):
#             dp[n, a, b] = 0
dp = [[[0]*8 for a in range(8)] for n in range(2, 80)]
for a in range(1, 8):
    for b in range(8):
        dp[2][a][b] = 1

for n in range(3, 78):
    for a in range(8):
        for b in range(8):
            if a+b > 7: continue
            for c in range(8-a-b):
                dp[n][b][c] += dp[n-1][a][b]

print(sum(dp[77][a][b] for a in range(8) for b in range(8)))