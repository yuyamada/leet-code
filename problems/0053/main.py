# https://leetcode.com/problems/maximum-subarray/

def solve(nums):
    csum = 0
    osum = nums[0]
    for v in nums:
        csum += v
        osum = max(osum, csum)
        csum = max(csum, 0)

    return osum


nums = [int(s) for s in input().strip().split()]
ans = solve(nums)
print(ans)
