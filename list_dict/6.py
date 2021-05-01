# -*- coding:utf-8 -*-
#@Time : 2021-03-31 12:16
#@Author: zxf_要努力
#@File : 4.py
'''
一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
 

示例 1：

输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"
示例 2：
输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"
解释：
P     I    N
A   L S  I G
Y A   H R
P     I
示例 3：

输入：s = "A", numRows = 1
输出："A"

'''
class Solution(object):


    def convert(self ,s, numRows):
        if numRows ==1:
            return "".join(s)
        list_str = list(s)
        str_len = len(list_str)
        # temp_list =[[" "] *str_len] * numrows
        temp_list = [[" " for _ in range(str_len)] for _ in range(numRows)]
        # 标记行数
        row_num = 0
        # 列
        colume = 0
        down = True
        for i in range(str_len):
            temp_list[row_num][colume] = list_str[i]
            if down:
                if row_num == numRows - 1:
                    down = False
                    colume += 1
                    row_num -= 1
                else:
                    row_num += 1
            else:
                # colume -= 1
                # row_num -= 1
                if row_num == 0:
                    row_num += 1
                    down = True
                else:
                    row_num -= 1
                    colume += 1
        result = []
        for i in range(numRows):
            for j in range(str_len):
                if temp_list[i][j] != " ":
                    result.append(temp_list[i][j])
        return "".join(result)







str = "ucqxswyqdntdmfrtzlqsekejhzksklfepxchvczysvdgcxbbiswmeaylzifktmoikssfxtgpojxqiysrsqfwqdjqnqcgdqrnlluieazvmwnuufnnxvloyvgmliuqandlyavfauaosnlnvacsvpiumoiawcqxswkqwgxyazntnaikameybnuqbcqaggxachrynqxqqmlfotpqhvokiiammqmvxjvbsoaifzyxnjcberrnmixxsyjhovengbpyqrixqgwdrygxrxkfhicainhwilkqmbpeszdigznzxtzqsjwatycbmjawwmninepfduplucltxmkpvgrrgtuseurageltkcapwpbqromqawixezqkvlfbhwcocpjmrmbpbegvsuluqtuuvkesvjtdhvtjmexfqbvufdpaxcwnwqjtbplyzedicwsodpwtqrpyuearhwgfnpaqelofrsotqiktxipqzeqvlqmuoubbjbrpmixfclbstnosvdkujcpwsdqhxrkiueziowoqjpiecwxxbjtnmkjgncpmvauqgtausokbfugjtfiu"
a = Solution()
print(a.convert(str, 199))

