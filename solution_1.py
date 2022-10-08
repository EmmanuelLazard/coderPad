def solution1(nums):
    i = cpt = 0
    new = []
    l = len(nums)
    while i < l:
        if nums[i] == 0:
            cpt += 1
        else:
            new.append(nums[i])
        i += 1
    while cpt>0:
        new.append(0)
        cpt -=1
    return new
    