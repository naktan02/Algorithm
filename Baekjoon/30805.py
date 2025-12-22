import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

MAXV = 100

# nextA[i][v] = i 이상에서 값 v가 처음 나오는 인덱스, 없으면 -1
nextA = [[-1] * (MAXV + 1) for _ in range(n + 1)]
nextB = [[-1] * (MAXV + 1) for _ in range(m + 1)]

# A 전처리
for v in range(1, MAXV + 1):
    nextA[n][v] = -1
for i in range(n - 1, -1, -1):
    nextA[i] = nextA[i + 1][:]      # 한 칸 뒤 복사
    nextA[i][A[i]] = i              # 현재 값 갱신

# B 전처리
for v in range(1, MAXV + 1):
    nextB[m][v] = -1
for j in range(m - 1, -1, -1):
    nextB[j] = nextB[j + 1][:]
    nextB[j][B[j]] = j

# 그리디로 사전순 최대 공통 부분수열 만들기
i = j = 0
ans = []

while i < n and j < m:
    picked = False
    for v in range(MAXV, 0, -1):  # 큰 값부터
        ni = nextA[i][v]
        nj = nextB[j][v]
        if ni != -1 and nj != -1:
            ans.append(v)
            i = ni + 1
            j = nj + 1
            picked = True
            break
    if not picked:
        break

print(len(ans))
if ans:
    print(*ans)
