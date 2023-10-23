class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in nums:
            for j in nums[nums.index(i)+1:]:
                if i + j == target: 
                    return [nums.index(i), nums.index(j)]
        
        return
