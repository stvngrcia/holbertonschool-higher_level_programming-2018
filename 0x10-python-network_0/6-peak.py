#!/usr/bin/python3


def find_peak(nums):
    '''
        Finds the pick in a list of numbers
    '''
    if len(nums) == 0:
        return None
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return nums[0] if nums[0] > nums[1] else nums[1]
    res = list()
    if nums[0] > nums[1]:
        return nums[0]
    if nums[-1] > nums[-2]:
        return nums[len(nums)-1]
    for i in range(1, len(nums)-1):
        pre = nums[i-1]
        cur = nums[i]
        nex = nums[i+1]
        if cur > pre and cur > nex:
            return nums[i]
