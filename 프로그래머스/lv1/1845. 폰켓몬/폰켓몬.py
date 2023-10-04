def solution(nums):
    n = len(nums)//2
    nums = list(set(nums))
    answer = min(len(nums),n)
    return answer




