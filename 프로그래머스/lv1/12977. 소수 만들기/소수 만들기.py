from itertools import combinations
def solution(nums):
    nums = [sum(x) for x in list(combinations(nums,3))]
    not_list = []
    for i in nums:
        for j in range(2,(i//2)+1):
            if i%j==0:
                not_list.append(i)
    answer = len([x for x in nums if x not in not_list])
    return answer