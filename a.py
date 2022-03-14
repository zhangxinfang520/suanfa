import sys
'''
3 4
08:00-09:00
09:30-11:00
13:00-15:00
07:00-08:00
08:00-11:00
12:00-13:30
14:00-17:00
'''


def get_second(Date):
    #Date 包含 小时和分中
    hour,minute = Date.split(":")
    return int(hour) * 3600 + int(minute) * 60

def max_count(envs):
    envs = sorted(envs,key=lambda x :(x[0],-x[1]))
    n = len(envs)
    dp = [1] * n
    for i in range(1,n):
        for j in range(0,i):
            if envs[i][0] >= envs[j][1] :
                dp[i] = max(dp[i],dp[j]+1)
    return max(dp)

if __name__ == '__main__':
    M, N = list(map(int,sys.stdin.readline().rstrip().split()))
    res = []
    for i in range(M+N):
         temp = sys.stdin.readline().rstrip().split("-")
         res.append(list(map(get_second, temp)))
    print(max_count(res))


