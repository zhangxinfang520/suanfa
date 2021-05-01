class Solution:
    def validMountainArray(self, A) -> bool:
       if len(A)<3:
            return False
       #找最大值下表
       a = max(A)
       a_index =[]
       for i in range(len(A)):
            if a ==A[i]:
                a_index.append(i)
       if len(a_index)>1 or a_index[0]==(len(A)-1) or a_index[0]==0:
           return False
       for i in range(a_index[0]):
            if A[i]>=A[i+1]:
                return False
       for i in range(a_index[0],len(A)-1):
            if A[i]<=A[i+1]:
                return False
       return True



