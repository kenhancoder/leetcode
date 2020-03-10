# -*- coding: utf-8 -*-


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp_ls = list(set(nums))
        temp_ls.sort(key=nums.index)
        nums[:] = temp_ls
        return len(temp_ls)
