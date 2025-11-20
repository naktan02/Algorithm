n, m, k = map(int, input().split())
old = abs(n - m)
total = n * m

ans = 0

for g in range(total - 1, 0, -1):
    ok = False
    for i in range(1, g + 1):
        if g % i == 0:
            j = g // i
            if abs(j - i - old) <= k:
                ok = True
                break
    if ok:
        ans += 1
    else:
        break

print(ans)
