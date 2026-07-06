def topKFrequent(nums, k):
    count={}
    for num in nums:
        count[num] = count.get(num, 0)+1
    
    buk =[[] for _ in range(len(nums)+1)]
    for num,fre in count.items():
        buk[fre].append(num)

    res = []
    for i in range(len(buk)-1,0,-1):
        for num in buk[i]:
            res.append(num)
            if len(res) == k:
                return res
    return []
