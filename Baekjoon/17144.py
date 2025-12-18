import sys
input = sys.stdin.readline
r,c,t = map(int,input().split())
field = [list(map(int,input().split())) for _ in range(r)]

airfind = False
air = [0,0]
for _ in range(t):
    add_temp = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            count = 0
            if field[i][j] == -1:
                if not airfind:
                    airfind = True
                    air[0] = i
                    air[1] = j
                continue
            temp = field[i][j] // 5
            for ny,nx in ((1,0),(0,1),(-1,0),(0,-1)):
                y = i+ny
                x = j+nx
                if 0 <= y < r and 0 <= x < c and field[y][x] != -1:
                    add_temp[y][x]+=temp
                    count+=1
            field[i][j] -= (temp * count)
    for i in range(r):
        for j in range(c):
            if field[i][j] == -1:
                continue
            field[i][j]+=add_temp[i][j]
    temp = field[air[0]][1]
    field[air[0]][1] = 0
    turn = "right"
    x = 2
    y = air[0]
    while True:
        if turn == "right":
            temp, field[y][x] = field[y][x], temp
            x+=1
            if x == c:
                turn = "up"
                x-=1
                y-=1
        elif turn == "up":
            temp, field[y][x] = field[y][x], temp
            y-=1
            if y == -1:
                y+=1
                x-=1
                turn = "left"
        elif turn == "left":
            temp, field[y][x] = field[y][x], temp
            x-=1
            if x == -1:
                x+=1
                y+=1
                turn = "down"
        else:
            temp, field[y][x] = field[y][x], temp
            y+=1
            if y == air[0]:
                break
    temp = field[air[0]+1][1]
    field[air[0]+1][1] = 0
    turn = "right"
    x = 2
    y = air[0] + 1
    while True:

        if turn == "right":
            temp, field[y][x] = field[y][x], temp
            x+=1
            if x == c:
                turn = "down"
                x-=1
                y+=1
        elif turn == "down":
            temp, field[y][x] = field[y][x], temp
            y+=1
            if y == r:
                y-=1
                x-=1
                turn = "left"
        elif turn == "left":
            temp, field[y][x] = field[y][x], temp
            x-=1
            if x == -1:
                x+=1
                y-=1
                turn = "up"
        else:
            temp, field[y][x] = field[y][x], temp
            y-=1
            if y == air[0]+1:
                break

result = 0
for y in range(r):
    for x in range(c):
        if field[y][x] == -1:
            continue
        result+=field[y][x]
print(result)




            
            



