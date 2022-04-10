# encoding: utf-8
"""
@author: zxf_要努力
@file: 字节跳动4.py
@time: 2022/4/10 11:03
"""
import sys

def is_exit(nums,product):
    for num in nums:
        if num not in product:
            return False
    return True


def add_ele(product, product_list:set):
    for p in product_list:
        product.add(p)


def remove_ele(product:set, product_list:set):
    for p in product_list:
        product.remove(p)


min_count = float("inf")

def get_min_nums(product_list:list):
    product_list.sort(key=lambda x:-len(x))
    product = set()
    nums = len(product_list)
    
    def dp(track,idx):
        if len(product) == 10:
            global min_count
            min_count = min(min_count,track)
            return
        if idx == nums:
            return
        for i in range(idx,nums):
            set_product_list = set(product_list[i])
            diff_ = set_product_list.difference(product)
            if not diff_:
                continue
            add_ele(product,diff_)
            dp(track+1,idx+1)
            remove_ele(product,diff_)

    dp(0,0)
    return min_count


#000 111 222 345 678 891
if __name__ == '__main__':
    def get_set(nums):
        return list(map(int,list(set(nums))))
    product_price = list(map(get_set,sys.stdin.readline().strip().split(" ")))
    re = get_min_nums(product_price)
    if re == float("inf"):
        print(-1)
    else:
        print(re)
