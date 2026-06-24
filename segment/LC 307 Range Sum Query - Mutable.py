#Fenwick Tree (Bit Indexed Tree - BIT)
class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.BIT = [0] * (self.n+1)
        self.nums = nums
        for i in range(1,self.n+1):
            self.BIT[i] += nums[i-1]
            parent = i + (i & -i)
            if parent <= self.n:
                self.BIT[parent] += self.BIT[i]

    def update(self, index: int, val: int) -> None:
        i = index+1
        delta = val - self.nums[index]
        self.nums[index] = val
        while i <= self.n:
            self.BIT[i] += delta
            i += i & -i       
        
    def prefixSum(self, i:int):
        s = 0
        i = i + 1
        while i > 0:
            s += self.BIT[i]
            i -= i & - i
        return s

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum(right) - self.prefixSum(left-1)
# segment tree
# class NumArray:

#     def __init__(self, nums: List[int]):
#         self.n = len(nums)
#         self.tree = [None] * self.n
#         def total(l,r):
#             if l > r:
#                 return 0
#             m = (l + r) // 2
#             val = nums[m] + total(l,m-1) + total(m+1,r)
#             self.tree[m] = [nums[m], val]
#             return val
#         total(0,self.n-1)
#         # print(self.tree)

#     def update(self, index: int, val: int) -> None:
#         def change(l,r):
#             if l > r:
#                 return 0
#             m = (l + r) // 2            
#             node = self.tree[m]
#             if index < l or index > r:
#                 return node[1]            
        
#             if index == m:                
#                 self.tree[m] = [val, node[1] + val - node[0]]
#                 return self.tree[m][1]

#             node[1] = node[0] + change(l,m-1) + change(m+1,r)
#             return node[1]            
#         change(0,self.n-1)
#         # print((index,val), self.tree)
        

#     def sumRange(self, left: int, right: int) -> int:
#         def total(l,r,left,right):
#             if l > r or right < l or left > r:
#                 return 0
#             m = (l+r)//2
#             node = self.tree[m]
#             if left == l and r == right:
#                 return node[1]
#             if right < m:
#                 return total(l,m-1,left,right)
#             if left > m:
#                 return total(m+1,r,left,right)
#             return total(l,m-1,left,m-1) + node[0] + total(m+1,r,m+1,right)
            
#         return total(0,self.n-1,left,right)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)