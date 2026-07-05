def longest_consecutive(nums):
    max_stk=0
    nums=set(nums)
    for num in nums:
        if num-1 not in nums:
            cur=1
            cur_num=num
            while cur_num+1 in nums:
                cur +=1
                cur_num +=1
            max_stk=max(max_stk,cur)
    return max_stk
