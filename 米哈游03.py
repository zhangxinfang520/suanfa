import sys

def x_target(x, y, x2, y2):
    if (x2,y2) in [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]:
        return True
    return False

def is_valid(grap,n,m, x1, y1, x2, y2):
    def dp(grap,i,j):
        if i < 0 or j < 0 or i == n or j == m:
            return float('inf')
        if grap[i][j] == '#':
            return float('inf')
        if x_target(i,j,x2,y2):
            return 0
        t = float('inf')
        temp = grap[i][j]
        grap[i][j] = "#"
        t = min(t,dp(grap,i+1,j)+1)
        t = min(t,dp(grap,i-1,j)+1)
        t = min(t,dp(grap,i,j+1)+1)
        t = min(t,dp(grap,i,j-1)+1)
        grap[i][j] = temp
        return t
    return  dp(grap,x1,y1)





if __name__ == "__main__":
    # 读取第一行的n
    T = int(sys.stdin.readline().strip())
    r = []
    for i in range(T):
        # 读取每一行
        #n行 m列
        n, m = list(map(int,sys.stdin.readline().strip().split()))
        #x1, y1, x2, y2
        x1, y1, x2, y2 = list(map(int, sys.stdin.readline().strip().split()))
        grap = [[0]*m for _ in range(n)]
        for i in range(n):
            str_g = str(sys.stdin.readline().strip())
            for j in range(m):
                grap[i][j] = str_g[j]

        if grap[x1-1][y1-1] == "#":
            print(0)

        else:
            res = is_valid(grap,n,m,x1-1,y1-1,x2-1,y2-1)
            if res == float('inf'):
               r.append(-1)
            else:
                re = (x2-x1) ^ res ^ (y2-y1)
                r.append(re)
    for result in r:
        print(result)
