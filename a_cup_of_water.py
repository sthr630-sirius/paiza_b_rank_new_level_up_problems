n, x = map(int, input().split())
water = []
for _ in range(n):
    water.append(int(input()))

max_ans = 0

for bit in range(1<< n):
    ans = 0
    for i in range(n):
        if 1 & bit >> i:
            ans += water[i]

    if ans <= x:
        max_ans = max(max_ans, ans)

print(max_ans)