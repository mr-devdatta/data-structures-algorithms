# https://leetcode.com/problems/maximum-subarray/
nums = [-2,1,-3,4,-1,2,1,-5,4]

class solution():
    def sorted(self, nums):
        print(f"Original List => {nums}")
         
        current_sum = 0
        max_sum = nums[0]

        for n in nums:
            current_sum += n
            print(f"current_sum : {current_sum}")
            if current_sum > max_sum:
                max_sum = current_sum
            if current_sum < 0:
                current_sum = 0
            
            print(f"  ---->  current_sum : {current_sum} & max_sum : {max_sum}")

        print("Total : ")
        print(max_sum)
                

obj = solution()
obj.sorted(nums)