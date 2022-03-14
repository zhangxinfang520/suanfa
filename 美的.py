# -*- coding:utf-8 -*-
#@Time : 2021/9/18 14:59
#@Author: zxf_要努力
#@File : 美的.py


class Solution:
    def justifyFill(self, words, M):
        n = len(words)
        if n == 1:
            return words[0] + " " * (M-len(words[0]))
        temp = []
        dict = {}
        i = 0
        for word in words:
            if temp:
                if temp[-1][1] + len(word)  >= M:
                    i +=1
                    temp.append([word,len(word)+1])
                else:
                    temp.append([word,temp[-1][1] + len(word)+1])
            else:
                temp.append([word,len(word)+1])
            if i in dict:
                dict[i] += [word]
            else:
                dict[i] = [word]
        res = []
        for key,list_word in dict.items():
            if len(list_word) == 1:
                res.append(list_word[0] + " " * (M-len(list_word[0])))
            else:
                res.append(self.get_str(list_word,M))
        return res

    def get_str(self,list_word,M):
        n = len(list_word)
        needpad = M - sum(len(s) for s in list_word)
        if needpad % (n-1) == 0:
            y_ = needpad // (n-1)
            s_ = ""
            for s,_ in enumerate(list_word):
                if s != (n-1):
                    s_ += (list_word[s] + " "*y_)
                else:
                    s_ +=list_word[s]
            return s_
        else:
            left = needpad % (n-1)
            y_ = needpad // (n-1)
            temp_str = ""
            for i,index in enumerate(list_word):
                if left > 0:
                    temp_str +=(list_word[i] + " "*(y_+ 1))
                    left -= 1
                else:
                    if i != (n-1):
                        temp_str += (list_word[i] + " " * y_)
                    else:
                        temp_str += list_word[i]
            return temp_str





if __name__ == '__main__':
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    print(Solution().justifyFill(words, 16))


