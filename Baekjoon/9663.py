# N-Queen

n =int(input())
result = 0
width = [0]*n
ldiagonal = [0]* (2*n -1)
rdiagonal = [0]* (2*n -1)
def back(cnt):
    global result
    if cnt == n:
        result += 1
        return
    for i in range(n):
        if width[i] == 0 and ldiagonal[cnt + i] == 0 and rdiagonal[cnt -i + n -1] == 0:
            width[i] = 1
            ldiagonal[cnt + i] = 1
            rdiagonal[cnt - i + n -1] = 1
            back(cnt + 1)
            width[i] = 0
            ldiagonal[cnt + i] = 0
            rdiagonal[cnt - i + n -1] = 0

back(0)
print(result)