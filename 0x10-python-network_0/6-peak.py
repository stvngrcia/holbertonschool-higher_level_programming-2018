#!/usr/bin/python3


def find_peak(nums):
    '''
        Finds the pick in a list of numbers
    '''
    length = len(nums)
    if length < 3:
        return(max(nums))

    for idx in range(1, length):
        if idx + 1 < length:
            if nums[idx + 1] < nums[idx] and nums[idx - 1] < nums[idx]:
                pick = nums[idx]

    return pick
