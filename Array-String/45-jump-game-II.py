class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        further = 0
        end = 0
        for i in range(len(nums)-1):
            further = max(i + nums[i], further)
            
            if further >= len(nums)-1:
                count += 1
                break
            
            if i == end:
                count += 1
                end = further

        return count
