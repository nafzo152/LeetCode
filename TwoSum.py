# Hashing

class Solution(object):
    def twoSum(self, nums, target):
       h={}
       for i in range(len(nums)):
            x = target - nums[i]
            if x in h:
                return [h[x], i]
            h[nums[i]]=i
        
nums = [2,7,8,4]
target = 9
sol = Solution()
print(sol.twoSum(nums, target))