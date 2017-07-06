'''
268. Missing Number
在一个包含0, 1, 2, ..., n的数组中，找到缺失的那个数，只有一个
例子： nums = [0, 1, 3] return 2.
要求： 线性复杂度
'''

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len(nums)*(len(nums)+1)/2- sum(nums)
