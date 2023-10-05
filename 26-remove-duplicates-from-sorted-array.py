class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in nums:
            for j in nums[nums.index(i)+1:]:
                if i == j:
                    nums.remove(i)


        return len(nums)
