import sys

def find_recusion(i,s):
    if not s[i].isalpha():
        return ""
    n = len(s)
    temp = s[i]
    if temp.lower() not in s[i:]:
        return ""
    i = s.index(temp.lower())
    temp +=s[i]
    while i+1 < n:
        if s[i+1].isdigit() and s[-1].lower() <s[i+1].lower():
            pass
        else:
            i +=1
    return temp


def get_recusion(s):
    if len(s)<=1:
        return 0
    result = []
    for i in range(len(s)):
        #以每一个字母开头
        if not s[i].isalpha():
            continue
        res = find_recusion(i,s)
        if len(res) >0:
            result.append(res)
    return result

if __name__ == "__main__":
    # 读取第一行的n 猪的价值
    s = str(sys.stdin.readline().strip())
    res = get_recusion(s)
    if res ==0:
        print("Not Found")
    for re in res:
        print(re)
