# -*- coding:utf-8 -*-
#@Time : 2021/8/26 19:13
#@Author: zxf_要努力
#@File : test.py


def lengthfLongestSubstring(s):
	n = len(s)
	occ = set()
	rk,ans = -1,0
	for i in range(n):
		if i != 0:
			occ.remove(s[i-1])
		while rk+1 < n and s[rk+1] not in occ:
			occ.add(s[rk+1])
			rk +=1
		ans = max(ans,rk-i+1)
	return ans


if __name__ == '__main__':
	s = "asdsdcsfs"
	print(lengthfLongestSubstring(s))
