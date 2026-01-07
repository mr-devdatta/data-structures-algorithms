# https://leetcode.com/problems/rotate-array/

nums = [1,2,3,4,5,6,7]
k = 3
 
class solution():

    def rotate(self, nums, k:int):
        print(f"Original List => {nums}")
        #nums = nums[k+1:] + nums[:k+1]
        nums = nums[-k:] + nums[:-k]
        print(f"Updated List  => {nums}")


obj = solution()
obj.rotate(nums, k)

 