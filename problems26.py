# @lc app=leetcode.cn id=26 lang=python
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
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

# @lc code=end
