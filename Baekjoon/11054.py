n = int(input())
data = list(map(int, input().split()))

rdp = [1] * n
ldp = [1] * n
for i in range(n):
    for j in range(i):
        if data[i] > data[j]:
            ldp[i] = max(ldp[i], ldp[j] + 1)

for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if data[i] > data[j]:
            rdp[i] = max(rdp[i], rdp[j] + 1)

result = 0
for i in range(n):
    result = max(result, ldp[i] + rdp[i] - 1)
print(result)