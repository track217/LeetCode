'''
268. Missing Number
在一个包含0, 1, 2, ..., n的数组中，找到缺失的那个数，只有一个
例子： nums = [0, 1, 3] return 2.
要求： 线性复杂度

解法：0-n的求和减去数组的求和
'''

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len(nums)*(len(nums)+1)/2- sum(nums)

'''
1. Two Sum
给一个整数数组和一个目标值，在数组中找两个数之和等于目标值，返回它们的索引
每个数只能使用一次，假设只有一个解
例子 nums = [2, 7, 11, 15], target = 9, return [0, 1].
'''





