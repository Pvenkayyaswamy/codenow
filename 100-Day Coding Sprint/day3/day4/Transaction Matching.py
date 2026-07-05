def twoSum(nums, target):
    hist={}
    for i,num in enumerate(nums):
        diff=target-num
        if diff in hist:
            return [hist[diff] , i]
        else:
            hist[num]=i
    return []
