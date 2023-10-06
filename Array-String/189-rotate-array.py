class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) >= k :
            head_part = nums[len(nums)-k:]
            back_part = nums[:len(nums)-k]
            del nums[:len(nums)-k]
            nums.extend(back_part)
        else:
            new_k = k % len(nums)
            head_part = nums[len(nums)-new_k:]
            back_part = nums[:len(nums)-new_k]
            del nums[:len(nums)-new_k]
            nums.extend(back_part)
