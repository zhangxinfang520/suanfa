 # -*- coding:utf-8 -*-
#@Time : 2021-08-13 16:27
#@Author: zxf_要努力
#@File : 二分法求平方根.py

def sqrtBI(x,epsilon=1e-4):
    low = 0
    high = x
    guess = (high + low) / 2.0
    counter = 0
    while ((abs(guess ** 2 - x)) > epsilon) and (counter <=100):
        if guess ** 2 < x:
            low =  guess
        else:
            high = guess
        guess = (low + high) / 2.0
        counter +=1
    return guess

print(sqrtBI(100))
        
            

    