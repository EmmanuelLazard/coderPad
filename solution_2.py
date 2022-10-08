def solution(nums):
    i = 0
    j = 1
    l = len(nums)
    while i < l:
        if nums[i] == 0:
            while j < l and nums[j] == 0:
               j += 1
            if j == l:
                break
            nums[i] = nums[j]
            nums[j] = 0
        i += 1
        j += 1
    return nums
