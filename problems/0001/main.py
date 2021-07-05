# https://leetcode.com/problems/two-sum/

def solve(nums, target):
    rest = {}
    for i, v in enumerate(nums):
        if v in rest:
            return [rest[v], i]
        rest[target - v] = i

    return []


nums = [int(s) for s in input().strip().split()]
target = int(input())
ans = solve(nums, target)
print(ans)
