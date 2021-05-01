# 给你一个整数数组 arr 。请你将数组中的元素按照其二进制表示中数字 1 的数目升序排序。
#
# 如果存在多个数字二进制中 1 的数目相同，则必须将它们按照数值大小升序排列。
# 请你返回排序后的数组


class Solution:
    def sortByBits(self, arr):
        arr = sorted(arr, reverse=False)
        a = dict()
        repe_list = []
        for i in range(len(arr)):
            if arr[i] in list(a.keys()):
                repe_list.append(arr[i])
            else:
                count = self.get_one(arr[i])
                a[arr[i]] = count
        if len(set(a.values())) == 1:
            return sorted(arr, key=lambda x: x, reverse=False)
        else:
            new_arr_tuple = sorted(a.items(), key=lambda item: item[1], reverse=False)
            if len(new_arr_tuple) == len(arr):
                for i in range(len(arr)):
                    arr[i] = new_arr_tuple[i][0]
                return arr
            else:
                arr01 = []
                for i in range(len(new_arr_tuple)):
                    arr01.append(new_arr_tuple[i][0])
                for i in range(len(repe_list)):
                    arr = self.sort_arr(repe_list[i], arr01)
                return arr

    def sort_arr(self, a, arr):
        if a not in arr:
            return
        index = 0
        for i in range(len(arr)):
            if a == arr[i]:
                index = i + 1
                break;
        arr.insert(index, a)
        return arr

    def get_one(self, a):
        # 计算二进制 1的个数
        # num_list = []
        count = 0
        while (a > 0):
            num = a % 2
            if num == 1:
                count += 1
            # num_list.append(num)
            c = int(a / 2)
            a = c
        return count


a = Solution()
arr = [1633,2181,7558,2650,1920,809,4903,2223,4271,4110,7564,5428,1730,5970,9640,
       3185,7564,5040,4344,9479,2070,6569,9849,73,2961,7991,9419,7946,3293,882,
       4714,3813,278,6121,9244,8248,5424,2377,4270,7656,1983,2928,2876,4746,129,
       5971,522,349,1239,9493,4777,1421,1763,8419,5696,726,6130,9164,5290,6793,
       3670,3090,3395,5597,7557,6246,956,7791,677,2284,7280,5309,8274,1760,
       2383,7003,4094,1681,8885,3010,1551,7419,813,9937,7054,9615,8126,2739,
       3255,334,587,634,3382,3316,4630,6077,4687,2226,8910,8357,1961,1454,6416,
       8838,6295,4523,9736,6165,2849,7877]
res = a.sortByBits(arr)
print(res)
