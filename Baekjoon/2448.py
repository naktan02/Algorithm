n = int(input())
star = [""] * (n+1)
count = 0
for i in range(n,0,-1):
    star[i]+= " " * count
    count+=1

def draw_star(size,col):
    if size == 3:
        star[col] += "*" * 5
        star[col-1] += "*" + " " + "*"
        star[col-2] += "*"
        return 3
    
    level = draw_star(size//2,col)
    for i in  range(level):
        star[col-i] += " " * (2*i+1)
    draw_star(size//2,col)
    draw_star(size//2,col-level)
    return level*2
draw_star(n,n)
for i in range(1, n + 1):
    print(star[i].ljust(2 * n - 1))