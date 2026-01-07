# https://leetcode.com/problems/squares-of-a-sorted-array/

import math

nums = [-4,-1,0,3,10]

class solution():

    def sorted(self, nums):
        print(f"Original List => {nums}")
        newList = [int(math.pow(n, 2)) for n in nums]
        newList.sort()
        print(f"Updated List  => {newList}")


obj = solution()
obj.sorted(nums)